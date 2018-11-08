from gensim.models import word2vec
from janome.tokenizer import Tokenizer
import numpy as np
import csv


model = word2vec.Word2Vec.load("DataBase/word2vec.gensim.model")
e=0.9

RewardMat=np.zeros((39,52))
ProbMat=np.zeros((39,52))
ChoiceMat=np.zeros((39,52))



#arr = np.array([[0, 1, 2,3,4,5,6,7,8,9], [10,11,12,13, 14, 15,16,17,18,19]])

i=0

while(True):
    print('お題を入力してください')
    UserInput = input('>> ')
    csv_file = open("DataBase/dataset_odai_ref.csv", "r", encoding="utf-8", errors="", newline="" )
    odai_ref = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    k=0
    MaxS=-1
    for row in odai_ref:
        S=model.similarity(UserInput,row[0])
        print(S)
        if S>MaxS:
            MaxS=S
            word0=row[0]
            word1=row[1]
            print(row[0])
            print(row[1])
            index_odai=k
        k=k+1
    
    what=model.wv.most_similar(positive=[word1,UserInput],negative=[word0],topn=5)

    i=i+1
    R=np.random.rand()
    if R>e:
        index=np.argmax(ProbMat, axis = 1)
        index_keyoshi=index[index_odai]
    else:
        index_keyoshi=np.random.randint(51)
    k=0
    print(index_keyoshi)
    csv_file = open("DataBase/dataset_keyoshi.csv", "r", encoding="utf-8", errors="", newline="" )
    keyoshi = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    for row in keyoshi:
        if k==index_keyoshi:
            boke=row[0]
            print(boke)
        k=k+1

    answer=what[0][0]+'が'+boke
    print(answer)
    
    ChoiceMat[index_odai,index_keyoshi]=ChoiceMat[index_odai,index_keyoshi]+1
    print('評価を入力してください')
    UserInput = input('>> ')
    if UserInput=='2':
        RewardMat[index_odai,index_keyoshi]=RewardMat[index_odai,index_keyoshi]+1
    if UserInput=='1':
        RewardMat[index_odai,index_keyoshi]=RewardMat[index_odai,index_keyoshi]+0.5
    
    ProbMat[index_odai,index_keyoshi]=RewardMat[index_odai,index_keyoshi]/ChoiceMat[index_odai,index_keyoshi]

    if i==30:
        break

print(RewardMat)
print(ProbMat)