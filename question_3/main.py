# %%
import os
import cv2
import csv
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout, RandomRotation
from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy

# %%
# 1 = Real People
# 0 = Fake People
# data = tf.keras.utils.image_dataset_from_directory(r"../question_1/dataset")
data = tf.keras.utils.image_dataset_from_directory(r"../question_1/real_and_fake_face_small")
data = data.map(lambda x, y: (x/255, y))
# %%
data_iterator = data.as_numpy_iterator()
batch = data_iterator.next()

# %%
batch[0].shape

# %%
batch[1]

# %%
fig, ax = plt.subplots(ncols=4, figsize=(20,20))
for idx, img in enumerate(batch[0][:4]):
    ax[idx].imshow(img)
    ax[idx].title.set_text(batch[1][idx])

# %%
batch[0].max()

# %%
len(data)

# %%
train_size = 4
validation_size = 2
test_size = 1

# %%

train_data = data.take(train_size)
val_data = data.skip(train_size).take(validation_size)
test_data = data.skip(train_size+validation_size).take(test_size)


# %%
data_augmentation = Sequential([
    RandomRotation(0.2),
])

model = Sequential()

model.add(data_augmentation)

model.add(Conv2D(16, (3, 3), 1, activation="relu", input_shape=(1,256,256,3)))
model.add(MaxPooling2D())

# model.add(Dropout(0.2))

model.add(Conv2D(32, (3, 3), 1, activation="relu"))
model.add(MaxPooling2D())

model.add(Conv2D(16, (3, 3), 1, activation="relu"))
model.add(MaxPooling2D())

model.add(Flatten())

model.add(Dense(256, activation="relu"))
model.add(Dropout(0.2))
model.add(Dense(1, activation="sigmoid"))

# %%
model.compile("adam", loss=tf.losses.BinaryCrossentropy(), metrics=["accuracy"])

# %%
model.build((1,256,256,3))
model.summary()

# %%
logdir = "logs"

# %%
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir)

# %%
history = model.fit(train_data, epochs=16, validation_data=val_data, callbacks=[tensorboard_callback])

# %%
fig = plt.figure()
plt.plot(history.history["loss"], color="teal", label="loss")
plt.plot(history.history["val_loss"], color="orange", label="val_loss")
fig.suptitle("Loss", fontsize=20)
plt.legend(loc="upper left")
plt.show()

# %%
test_loss, test_acc = model.evaluate(test_data)
# %%
print(test_loss, test_acc)

# %%
precision = Precision()
recall = Recall()
accuracy = BinaryAccuracy()

for batch in test_data.as_numpy_iterator():
    X, y = batch
    y_predict = model.predict(X)
    precision.update_state(y, y_predict)
    recall.update_state(y, y_predict)
    accuracy.update_state(y, y_predict)

# %%
print(f"Precision:{precision.result().numpy()}, Recall:{recall.result().numpy()}, Accuracy:{accuracy.result().numpy()}")
# %%

results = []
directory = r"../rd_test_dataset"
for filename in os.listdir(directory):
    img = cv2.imread(directory + "/" + filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resize = tf.image.resize(img, (256,256))
    y_predict = model.predict(np.expand_dims(resize/255, 0))
    results.append([filename,"Real" if round(y_predict[0][0]) == 1 else "Fake"])

with open("results_new.csv", "w") as f:
    write = csv.writer(f)
    write.writerow(["File Name", "Prediction"])
    write.writerows(results)

# %%
