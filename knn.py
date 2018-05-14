from sklearn.neighbors import KNeighborsClassifier
from ged4py.algorithm import graph_edit_dist
import inputReader
import matplotlib.pyplot as plt
import networkx as nx
import csv
import operator

def readTxtFile(path):
    labels = {}
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            labels[int(row[0])] = row[1]
    return labels


def showGraph(graph):
    plt.subplot(121)
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()


def main():
    # get data
    graphs = inputReader.get_graphs()
    # showGraph(graphs[10071])
    # train_labels is a key:value list
    train_labels = readTxtFile('train.txt')
    train_label_keys = train_labels.keys()  # Not neccessary, but for readability
    # valid_labels is a key:value list
    valid_labels = readTxtFile('valid.txt')
    valid_label_keys = valid_labels.keys()  # Not neccessary, but for readability


    """ ********* graph_edit_dist is not recognized by KNeighborsClassifier.
         Dont know how to get recognized for the moment...  *********
    
    # Design Model
    knn = KNeighborsClassifier(n_neighbors=k, metric='pyfunc', algorithm=graph_edit_dist)
    """
    
    
    # Generate predictions
    predictions=[]
    k = 1
    for valid_label_key in valid_label_keys:
        # Get the k nearest neighbors (i.e. train_label_keys) through GED distance algorithm
        kNN_GED = getkNN_GED(graphs, train_label_keys, valid_label_key, k)
        # Get the label occuring the most among the k nearest neighbors
        result_label = getResponse(train_labels, kNN_GED)
        predictions.append((valid_label_key, result_label))
    # Get the accuracy. Compares test_label with prediction_label. How well is the testing set?
    labels_score = getAccuracy(valid_labels, predictions)
    print('Accuracy: ' + repr(labels_score) + '%')
    
    """

    # Training
    knn.fit(graphs, train_labels)

    # Testing
    accuracy = knn.score(graphs, valid_labels)

    print("Accuracy: {}%".format(accuracy))
    """


def getkNN_GED(graphs, train_label_keys, valid_label_key, k):
    # Returns the k nearest neighbors (i.e. train_label_keys) through GED distance algorithm
    
    distances = []
    # compute distance between each training instance and the test instance
    # and store tuple of result and corresponding training instance
    # into array of distances.
    for train_label_key in train_label_keys:
        # compare two graphs
        dist = graph_edit_dist.compare(graphs[valid_label_key], graphs[train_label_key])
        distances.append((train_label_key, dist))
    # sort list of tuples of distances in ascending order
    # regarding the second item of the tuples, i.e. the distances
    distances.sort(key=operator.itemgetter(1))
    kNN = []
    for x in range(k):
        kNN.append(distances[x][0])
    # return the k first training instances (the k most similar)
    return kNN


def getResponse(train_labels, kNN):
    # Returns the label occuring the most among the k nearest neighbors
    
    # classVotes is a key:value list
    classVotes = {}
    for key in kNN:
        # extract the label of training instance
        label = train_labels[key]
        # if the label appears in list of classVotes
        if label in classVotes:
            # add vote to label
            classVotes[label] += 1
        else:
            classVotes[label] = 1
    # sort the classVotes according to the number of votes in a descending order
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


def getAccuracy(valid_labels, predictions):
    # Returns the accuracy of predictions (list of (valid_label_key, result_key)) in %, which is the ratio
    # of the total correct (test-label-)predictions out of all predictions made
    correct = 0
    for x in range(len(predictions)):
        # if test label is equal to prediction label
        if valid_labels[predictions[x][0]] is predictions[x][1]:
            correct += 1
    # return ratio
    return (correct/float(len(predictions)))*100.0



if __name__ == '__main__':
    main()
