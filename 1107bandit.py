
import numpy as np
import csv



e=0.5

RewardMat=np.zeros((2,10))
ProbMat=np.zeros((2,10))
arr = np.array([[0, 1, 2,3,4,5,6,7,8,9], [10,11,12,13, 14, 15,16,17,18,19]])
i=0

while(True):
    i=i+1
    R=np.random.rand()
    if R>1-e:
        index=np.argmax(ProbMat, axis = 1)
        index=index[0]
        print(arr[0,index])
    else:
        index=np.random.randint(9)
        print(arr[0,index])
    
    print('お題を入力してください')
    UserInput = input('>> ')
    if UserInput=='1':
        RewardMat[0,index]=RewardMat[0,index]+1
        ProbMat[0,index]=RewardMat[0,index]/i
    else:
        ProbMat[0,index]=RewardMat[0,index]/i

    if i==20:
        break

print(RewardMat)
print(ProbMat)