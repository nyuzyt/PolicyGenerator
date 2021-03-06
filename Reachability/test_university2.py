__author__ = 'vishlesh'

from PolicyGenerator.subnet import *
from PolicyGenerator.Reachability.TraverseSourceInfoGraph import *

# usage enter No. of hosts in the network should be given to s.createSubnets(number of End host)
s = Subnet()
subnetList = s.createSubnets(1000)
print(subnetList)
print("total no. of subnets created:",len(subnetList))

destinationGraph = [(60,50),(100,100)]
totalPolicyUnits = 2

destinationInfoObj = DestInfo()
sourceInfoObj = SourceInfo()
list_PolicyUnits = destinationInfoObj.traverseDestInfoGraph(destinationGraph,totalPolicyUnits,subnetList)
print(len(list_PolicyUnits),"total policy units")
policies = []
sourceGraph = [(17,50),(100,100)]

policies=sourceInfoObj.traverseSourceInfoGraph(sourceGraph,list_PolicyUnits,subnetList)

for each_policy in list_PolicyUnits:
    print(each_policy.getDestAccessPoints())
    print(each_policy.getAction())

print(len(policies),"total no. of end point reachability policies")

for each_policy in policies:
    print("srcIP:",each_policy.getSource())
    print("dstIP:",each_policy.getDest())
    print(each_policy.getAction())

