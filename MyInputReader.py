'''
Created on 2017. 10. 16.

@author: MiJeong Lee(01413522)
'''

def MyInputReader(dataset):
    fileLocations = {
       'small_b': ['inputs/trainBalanced.pos','inputs/trainBalanced.neg','inputs/validBalanced.pos','inputs/validBalanced.neg'],
       'small_i': ['inputs/trainImbalanced.pos','inputs/trainImbalanced.neg','inputs/validImbalanced.pos','inputs/validImbalanced.neg'],
       'big_i': ['inputs/trainImbalancedBig.pos','inputs/trainImbalancedBig.neg','inputs/validImbalanced.pos','inputs/validImbalanced.neg']
    }
    
    def text_reader(dataset):
        list_dataset =[]
        for text in dataset :
            open_file = open(text,'r')
            data = open_file.readlines()
            list_dataset.append(data)
        return list_dataset
        
    def vector(dataset):
        list_dataset = text_reader(dataset)
        A = [1, 0, 0, 0]
        C = [0, 1, 0 ,0]
        G = [0, 0, 1, 0]
        T = [0, 0, 0, 1]
        trainX = []
        trainy = []
        validX = []
        validy = []
        
       
        for number in range(0, len(list_dataset)) :
            data = list_dataset[number]
            for i in range(0,len(data)) :
                sequence = data[i]
                vector =[]
                for j in range(0, len(sequence)-1) : # reading by line, also counted blank line so subtract -1
                    if sequence[j] == 'A' :
                        vector.append(A)
                    elif sequence[j] == 'C' :
                        vector.append(C)
                    elif sequence[j] == 'G' :
                        vector.append(G)
                    else :
                        vector.append(T)
            
                #trainX and validX
                if number ==0 or number == 1: #If it is first two files, which are train text
                    trainX.append(vector)
                else :
                    validX.append(vector) #If it is last two files, which are valid text
                
                #trainy and validy
                if number == 0 : #if it is pos train file
                    trainy.append(1)
                elif number == 1: #if it is nev train file
                    trainy.append(0)
                elif number == 2: #if it is pos valid file
                    validy.append(1)
                else :  #if it is neg valid file
                    validy.append(0)    
        
        return trainX, trainy, validX, validy
    
    files = fileLocations[dataset]
    return vector(files)
