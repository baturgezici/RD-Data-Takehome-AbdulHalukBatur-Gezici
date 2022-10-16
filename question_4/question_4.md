#  Now, consider the case where you had to manage a dataset with millions images rather than a few hundred. How will you change your dataset building and storing methods for

## a. Faster access, given that data data lives on the cloud infrastructure like S3

        First of all instead of storing images into databse, I would store image paths into database, because file system storage is faster than database storage. With sendfile() like methods I can obtain the image faster and asynchronously.


## b. Faster data re-sampling, to create custom datasets

        Again database storage might be a problem with this. With file storage I can directly access and manipulate the data as the way I want.


## c. Faster data-loader access for faster training

        By using file storage and creating related databases as shallow as possible, this way while finding desired images, each query will run faster, also optimized queries would be importand but since you asked dataset building and storing methods I am passing on this example.

<b>Also increasing memory and using strong CPU are key factors for all these 3 questions.</b>