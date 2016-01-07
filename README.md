# Python KNN Classifier

# About KNN:
K-Nearest Neighbors algorithm (or k-NN for short) is a non-parametric method used for classification and regression.[1] In both cases, the input consists of the k closest training examples in the feature space. The output depends on whether k-NN is used for classification or regression:

In k-NN classification, the output is a class membership. An object is classified by a majority vote of its neighbors, with the object being assigned to the class most common among its k nearest neighbors (k is a positive integer, typically small). If k = 1, then the object is simply assigned to the class of that single nearest neighbor.

In k-NN regression, the output is the property value for the object. This value is the average of the values of its k nearest neighbors. (Reference Wikipedia)

# Aim of building the classifier:
Task at hand is to create a classiﬁer that decides the correct orientation of a given image. The training and test data is of format:

				photo_id correct_orientation r11 g11 b11 r12 g12 b12 ...

Where r,g,b is understandably the red, green, blue values of each pixel. There are totally 192 features (whew!!)

Settings for KNN along with results and screenshots of the output we got :

Input dataset : 

Train: 36976 images 
Test: 943 images

Image Type : Pixels and gray scale.

Given below, results we obtained with different combinations of settings for KNN :

	            K = 5, Gray scale and Euclidean : 
	            Accuracy : 59 %

	            K = 20, Gray scale and Manhattan :
	            Accuracy : 61

	            K = 20,  pixel original scale and Euclidean :
	            Accuracy : 60 % ( Not persistent though)

	            K = 5 , pixel original scale and Manhattan :
	            Accuracy : 52 %

	            K = 10, Gray scale  and Manhattan :
	            Accuracy : 61

	            K= 10, pixel original scale and Manhattan :
	            Accuracy : 53 %

	            K = 20, pixel original scale and Manhattan :
	            Accuracy :  53 %

	            K = 50, Gray scale and Manhattan :
	            Accuracy : 61 %

# Problems faced when optimizing KNN code:

The main concern with optimizing the KNN classifier is to select the right number of neighbors K and the distance function to be considered.

# Techniques we implemented but didn’t work well and we removed them from code: 

Given the size of the input training set (about 37000) and the feature vector (192), the training for each test set will take a large amount of time. Hence, we reduced the feature set by converting them into pixel values. These are single integers formed by shifting 8 bits from initial red value adding green value and again shifting 8 bits and adding the blue value. By this method there is almost no loss in information and the feature vector is effectively reduced to 63. This did reduce time a lot than the full 192 vector, the shifting and adding values did incur an overhead and strangely it gave us very bad results on accuracy of the classifier, maybe due to the drastic differences. So we changed this and converted the values to gray pixels reducing 3:1 (red,green,blue = 1 gray pixel)

# Conclusion :
In terms of values of K When we tried picking very small values for K that is 1 or 2 then the knn classifier was over fitting the dataset. Because it was trying to build individual data points with their own individual decision boundaries. So, the classifier was performing better on training dataset that is was giving better accuracies on it whereas on test dataset the accuracy was getting reduced.

When we tried picking very large value for K that is 50 or more then the knn classifier was under fitting the dataset. Because, it is not fitting the input data properly. So, the classifier was not performing better on train as well as test dataset.

# Choosing Gray scale vs. original pixel values : 

The pixel values did not work because the distances were very erratic. So the accuracy was lesser. We then changed the RGB to grayscale by normalizing the red, green and blue pixels with gamma values (0.299, 0.587 and 0.114). The accuracies and speed of execution improved then.

# Choosing between Manhattan and Euclidean : 

We got good results with Manhattan than Euclidean .

So, we figured out the best results that we are getting is with below combinations : 

k: 10

image encoding: gray scale

distance measure: Manhattan

accuracy: 61 % and is constant

Execution time : 402.38 seconds


(Based on the problem statement in CS B551 Elements of Artificial Intelligence by Professor David J Crandall , Indiana University, Bloomington)