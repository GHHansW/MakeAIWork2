
import random


def multiply(inputmat):
   
    size = len(inputmat[0])

    weightMatrix = [[round(random.uniform(0,1),2)] for _ in range(size)]
    print(weightMatrix)
    
    outputMatrix=[[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*weightMatrix)] 
        for A_row in inputmat]

    return outputMatrix
   
# inputMatrix = [[1,1,1,1,0,1,1,0,1],[0,1,0,1,0,1,0,1,0],[1,0,1,0,1,0,1,0,1],[0,1,0,1,1,1,0,1,0]]

# for i in inputMatrix():  

print(multiply(inputmat=[[1,1,1,1,0,1,1,1,1]]))
    
# multiply(inputmat=[[0,1,0,1,0,1,0,1,0]])
# multiply(inputmat=[[1,0,1,0,1,0,1,0,1]])
# multiply(inputmat=[[0,1,0,1,1,1,0,1,0]])

        

# # def softmax(outputshapes):
# #     temp = [math.exp(v) for v in outputshapes]
# #     total = sum(temp)
# #     return[t/total for t in temp]


# # act =softmax(outputshape)
# # print(act)

# # for a in act:
# #     print(f"{a: }")
# # print(f"total:{sum(act)}")











