# You are given a classifier that reports high accuracy on the validation set:
 
## a. Would you be happy with these results or would you like to do more analysis.

I wouldn't be happy so fast, the main importance is on the test set's accuracy, real world problem will not be equally divided as in the validation set, also understanding the architecture and the structure of the classifier is important,and again we need to see wheather there is overfitting on the data.

## b. If so, what type of analysis would you perform?

First step is looking to the structure of the classifier, this will give us some clue about any pressure points that we can act on and prevent overfitting. These actions might be using cross validation, enlarging the training data, removing unnecessary features therefore reducing the dimention and regularization. Also validation_loss metric will give a good clue on overfitting, it should decrease alongside the validation_accuracy. But in the end the real importance is on the test set. If testing accuracy is significantly lower than validation accuracy then we should act on it and take the forementioned actions.