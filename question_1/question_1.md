# Design & build a small dataset (about 100+ images) to differentiate between real and fake face images. Please explain

## Considerations that went into deciding what data to collect.
        I wanted a dataset that mid size so I can fork faster and also create a Deep Classifier
         with high accuracy, so I find a dataset that contains 2041 file.

## How you went about collecting the data.
        I chose one ready dataset that has similar fake images to one that you provide, and 
        created one dataset, for the one I created I took the fake images from 
        "https://this-person-does-not-exist.com/en" and real images from 
        "https://www.istockphoto.com" sites, I want to show that I can easily create my own 
        dataset, but the one I created has some different angles and I guess the 
        Classifier learned the angle, so I want to show the 2 results.

## Besides fake/real labels, what other labels would you consider? Explain a simple method to sample a uniform dataset in the i.i.d sense, given the labels.
        Ethnicity, type of injuires(if the person has), age and sex could be some other label examples. 
        For sampling of the dataset, we can use sample() method of pandas library which takes 
        N as an argument that N >= (number of labels). This is a version of random sampling

## What API (e.g Pandas, etc.) you used to store and organize meta information about the dataset.
        I used selenium to reach websites and navigate in them, I used urllib to download the image.

## Please share your mini-dataset as a zip file.
        filename: dataset.zip