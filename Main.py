'''
Created on 2017. 10. 17.

@author: MiJeong Lee(01413522)
'''
from MyInputReader import MyInputReader
from MyMetrics import f1score
trainX, trainy, validX, validy = MyInputReader('big_i')

from TrainProcedure import TrainProcedure

hello = TrainProcedure('B',trainX, trainy, validX, validy, f1score,'f1')
p,l = hello.predictResults()
print(f1score(p, l))
hello.trainNetwork()

p,l= hello.predictResults()
print(f1score(p, l))
#python Main.py