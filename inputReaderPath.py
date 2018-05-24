from os import listdir
from os.path import isfile, join
import networkx as nx
import xml.etree.ElementTree as ET

"""
return a dictonary with the file name as key and the graph as value
"""

gxl_path = 'gxl/'
validation_path = 'testmolecules/gxl'


def get_graphs(path):
    graphs = {}
    for g in get_files(path):
        key = int(g[:-4])
        graphs[key] = create_graph(ET.parse(join(path, g)))

    return graphs


def get_files(path):
    return [f for f in listdir(path) if isfile(join(path, f))]



def create_graph(xml_tree):
    """
    Creates a graph out of a given ElementTree

    :param xml_tree:
    :return: the tree as networkx graph
    """
    g = nx.Graph()
    for node in xml_tree.findall(".//node"):
        node_id = node.get('id')
        attributes = {}
        for attr in node.getchildren():
            attr_name = attr.get('name')
            attr_dict = {}
            attributes[attr_name] = attr_dict
            for attrVal in attr.getchildren():
                attr_dict[attrVal.tag] = attrVal.text.strip()

        g.add_node(node_id, attr=attributes)

    for edge in xml_tree.findall(".//edge"):
        start = edge.get("from")
        end = edge.get("to")
        attributes = {}
        for attr in edge.getchildren():
            attr_name = attr.get('name')
            attr_dict = {}
            attributes[attr_name] = attr_dict
            for attrVal in attr.getchildren():
                attr_dict[attrVal.tag] = attrVal.text.strip()

        g.add_edge(start, end, attr=attributes)

    return g

graph_dict = get_graphs(gxl_path)
if __name__ == '__main__':
    print(get_graphs(validation_path))

