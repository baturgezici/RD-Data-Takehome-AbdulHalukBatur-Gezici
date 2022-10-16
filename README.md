# Running question_3/main.py
        First of all put the data into two seperate directory according to their classes.
        The directory that contains these two directories will be fed into function:

        ```data = tf.keras.utils.image_dataset_from_directory(r"../question_1/real_and_fake_face_small")```

        Than according to our data size that we see with ```batch[1]``` we will change our ```train_size```, ```validation_size``` and ```test_size``` variables.
        
        For the rest of the code we don't need to change any other variable if we are using the program for binary classification.
        
