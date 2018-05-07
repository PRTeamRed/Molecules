from sklearn.neighbors import KNeighborsClassifier
# from ged4py.algorithm import graph_edit_dist
import inputReader
import matplotlib.pyplot as plt
import networkx as nx
import csv


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


def main(k):
    # get data
    graphs = inputReader.get_graphs()
    # showGraph(graphs[10071])
    train_labels = readTxtFile('train.txt')
    print(train_labels)
    valid_labels = readTxtFile('valid.txt')
    print(valid_labels)

    # Design Model
    knn = KNeighborsClassifier(n_neighbors=k, metric='pyfunc', func=graph_edit_dist)

    # Training
    knn.fit(graphs, train_labels)

    # Testing
    accuracy = knn.score(graphs, valid_labels)

    print("Accuracy: {}%".format(accuracy))


if __name__ == '__main__':
    main(5)
