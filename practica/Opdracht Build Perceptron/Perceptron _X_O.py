# - inputMatrix * weightMatrix + bias
# - outputMatrix (2 x 1) geeft kruisje of rondje
# - softmax toevoegen: uitslag tussen 0 en 1 voor beide velkden in de outputMatrix
# - trainen met 4 x goede inputMatrix met bijbehorende 4 x gelabelde outPutMatrix
# - trainen in epochs mbv learningRate
# - resultaten opslaan en beste resultaat kiezen adhv GradientDescent (RMSE)
# - testen met getraind netwerk en zowel goede als gemankeerde inputMatrix
# - eventueel terug naar trainen als yhat nog niet optimaal


# Definieer rondje/onvolmaakt rondje/kruisje en onvolmaakt kruisje in een grid van 3 x 3 pixels
# Doel is om obv de varierende invulling van de pixels 
# van de pixels te herkennen of iets een O, een X is of geen van beide
# Creer de invoer met een 2D array
# definieer het neurale net:
#   Input node (9 x/ getOutput)
#   Link (18 x/inputnode/outputnode/weights/+getOutput)
#   Output node (2 x -)
# Ieder input set wordt middels vermenigvuldiging, per input node
# met zijn weight (initiele zelf te kiezen, bijvoorbeeld 1 voor X1 .. x9) 
# en als output doorgegeven naar de outputnode.
# In de outputnode wordt de sofmax function gebruikt op basis de uitkomst  met weights en bias
# De uitkomst van node 1 en node 2 moet 1 zijn;
# Backpropagation

# train het model door 1 set van 9 pixelwaardes per keer
# in te voeren. 
# De output =
# De waardes van de uitkomst van de softmax

# na x trainingsepochs moet de output zijn:
# een overzicht van de de weights tov de 
# volgende stappen zijn het toevoegen van Matrices en vectore, toevoegen hidden layer
# en numpy


# import random

# inputmat = [[1,1,1,1,0,1,1,1,1]]

# low = 0
# high =5
# cols = 1
# rows = 9

# new = [random.choices(range(low,high), k=cols) for _ in range(rows)]
# print(new)

# outputCircle = [[0]]

# for i in range(len(inputmat)):
 
#     # iterating by column by B
#     for j in range(len(new[0])):
 
#         # iterating by rows of B
#         for k in range(len(new)):
#             outputCircle[i][j] += inputmat[i][k] * new[k][j]
 
# for r in outputCircle:
#     print(r)
cirkel = [
    [1,1,1]
    [1,0,1]
    [1,1,1]]

print(cirkel)

def flatten(matrix):
    # 9 x 1 
    flatMatrix =[[]]

def transpose(matrix):
    transposeMatrix = matrix

    return transposeMatrix

def multiply(inputMatrix, weightMatrix):
    transposeMatrix = matrix

    return transposeMatrix


def classify(inputMatrix):
    
    predictionMatrix = [[]]

    flatMatrix = flatten(inputMatrix
                         
                         transposedMatrix = flatMatrix)

    weighMatrix[[]]

    return predictionMatrix

Test_cirkel = [
    [1,1,1]
    [1,0,1]
    [1,1,1]
]

# outcome should return 2 x 1 terug obv 3x3
classify
