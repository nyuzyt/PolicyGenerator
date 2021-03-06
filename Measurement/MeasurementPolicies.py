__author__ = 'vishlesh'

import random
import ipaddress
from PolicyGenerator.Policy import *
from PolicyGenerator.Measurement.createTree import *

class MeasurementPolicies():
    def __init__(self):
        self.listPolicies = []

    def generateMeasurementPolicies(self, subnetsList, set_destIPs, resources):
        #assert isinstance(set_sourceIPs,set)
        assert isinstance(set_destIPs,set)
        resourcesLeft = resources
        while(resourcesLeft>0):
            randomNo = random.randint(0,len(subnetsList)-1)
            sourceIP = subnetsList[randomNo]
            #print("subnetIP selected as rootNode sourceIP:",sourceIP)
            subnetsList.pop(randomNo)
            #randomNo = random.randint(0,len(subnetsList)-1)
            destIP = set_destIPs.pop()
           # subnetsList.pop(randomNo)
            c = CreateTree()
            print(sourceIP,destIP)
            tree = c.createTree(sourceIP,destIP)
            print("height:",tree.height(),
                  "root node srcIP :",tree.rootNode.srcIP,
                  "root node dstIP :",tree.rootNode.dstIP,
                  "total nodes in tree :",tree.elements_count)
            while(1):
                noPolicy = random.randint(1,resourcesLeft)
                if(noPolicy<tree.elements_count):
                    print("no of Policy:",noPolicy,"total elements:",tree.elements_count,
                          "resources left",resourcesLeft)
                    break

            listNodes = self.randomPickNodes(noPolicy,tree)
            resourcesLeft = resourcesLeft - noPolicy
            self.addMeasurementPolicies(listNodes)
        return self.listPolicies

    def addMeasurementPolicies(self,listNodes):

        for each_node in listNodes:
            assert isinstance(each_node,Node)
            p=Policy()
            p.setDest(each_node.dstIP)
            a = Action(3)   # action type: count
            p.setAction(a)
            p.setSource(each_node.srcIP)
            self.listPolicies.append(p)


    def randomPickNodes(self, noNodes, tree):
        """
        :param noNodes: number of nodes to pick
        :param tree: binary tree
        :return:
        """
        list1 = tree.inorder_non_recursive()
        #print(len(list1),"list of all elements in tree")
        returnList = []
        while(noNodes>0):
            node = random.choice(list1)
            returnList.append(node)
            noNodes=noNodes-1
        return returnList


