import sys
import math
import operator
import time
import random

train_set = []
test_set = []
correct = 0
labels = [0,90,180,270] # Problem Specific
confusion = {y: {x: 0 for x in labels} for y in labels}

def main(train, test, k):
	now = time.time()
	print "Loading pixels...."
	train_set = load_file(train)
	test_set = load_file(test)
	knn(train_set, test_set, k)
	print "Time Elapsed: "+str(time.time()-now)

# Problem Specific Methods Begin

def confusion_accuracy(actual, predicted, label, output_file):
	global correct
	confusion[actual][predicted] += 1
	if actual == predicted:
		correct += 1
	output_file.write(label+" "+str(predicted)+"\n")
	print "Predicted: " + str(predicted)
	print "Actual : " + str(actual) + "\n\n"

def print_confusion():
	print "\t".join([str(x) for x in confusion.keys()])
	print "----"*8
	for x in confusion.values():
		print "\t".join([str(y) for y in x.values()])
	print"\n\n"

def load_file(file_name):
	given = open(file_name, 'r')
	return convert_pixels([x.split(' ') for x in given])

def convert_pixels(vector):
	trains = []
	pixels = []
	global method_used
	for vec in vector:
		trains.append([vec[0], int(vec[1])])
		pic = []
		for x in xrange(2,len(vec[2:]),3):
			if vec[x+1]:
				pix = 0.299*int(vec[x])
				pix = pix+(0.587*int(vec[x+1]))
				pix = pix+(0.114*int(vec[x+2]))
				pic.append(pix)
			else:
				pass
		pixels.append(pic)
	return [trains, pixels]

# problem specific methods end

#####################################

# KNN begins

def knn(train, test, k):
	global correct
	results = open("knn_ouput.txt", 'w')
	for x in range(0,len(test[1])):
		distances = get_distances(train[1],test[1][x])
		distances.sort(key=operator.itemgetter(1))
		neighbors = [train[0][y] for y in [z[0] for z in distances[:int(k)]]]
		response = get_response(neighbors)
		confusion_accuracy(test[0][x][1], response, test[0][x][0], results)
	results.close()
	print_confusion()
	print "Accuracy: " + str((correct*100/len(test[1]))) + " %"

# Manhattan distance
def get_distances(train, test):
	diffs = [[y,sum([abs(test[x] - j) for x,j in enumerate(l)])] for y,l in enumerate(train)]	
	return diffs

def get_response(neighbors):
	classifier = {}
	for x in neighbors:
		if x[1] in classifier:
			classifier[x[1]] += 1
		else:
			classifier[x[1]] = 1
	return max(classifier.iterkeys(), key=(lambda key: classifier[key]))

# KNN ends

if __name__ == "__main__": main(sys.argv[1], sys.argv[2], sys.argv[3])