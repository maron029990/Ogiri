from gensim.models import word2vec
#from janome.tokenizer import Tokenizer
import numpy as np
import csv



e=0.9

def ReadCSV(name,Mat,colum):
    csv_file = open(name, "r", encoding="utf-8", errors="", newline="" )
    Read = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    k=0
    for row in Read:
        for i in range(colum):
            Mat[k][i]=row[i]
        k=k+1
    return Mat


RewardMatBoke=np.zeros((28,52))
RewardMatBoke=ReadCSV("DataBase/RewardMatBoke.csv",RewardMatBoke,52)
ProbMatBoke=np.zeros((28,52))
ProbMatBoke=ReadCSV("DataBase/ProbMatBoke.csv",ProbMatBoke,52)
ChoiceMatBoke=np.zeros((28,52))
ChoiceMatBoke=ReadCSV("DataBase/ChoiceMatBoke.csv",ChoiceMatBoke,52)

RewardMatWhat=np.zeros((28,4))
RewardMatWhat=ReadCSV("DataBase/RewardMatWhat.csv",RewardMatWhat,4)
ProbMatWhat=np.zeros((28,4))
ProbMatWhat=ReadCSV("DataBase/ProbMatWhat.csv",ProbMatWhat,4)
ChoiceMatWhat=np.zeros((28,4))
ChoiceMatWhat=ReadCSV("DataBase/ChoiceMatWhat.csv",ChoiceMatWhat,4)
model = word2vec.Word2Vec.load("DataBase/word2vec.gensim.model")

#arr = np.array([[0, 1, 2,3,4,5,6,7,8,9], [10,11,12,13, 14, 15,16,17,18,19]])

i=0

while(True):
    while(True):
        k=0
        print('お題を入力してください。【おわり】で終了します。')
        UserInput = input('>> ')
        try:
            S=model.similarity(UserInput,'おかゆ')
        except KeyError:
            print("その単語は知りません。別の単語を入力してね。")
            k=1
        if k==0:
            break
    
    if UserInput=='おわり':
        break

    csv_file = open("DataBase/dataset_odai_ref.csv", "r", encoding="utf-8", errors="", newline="" )
    odai_ref = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    k=0
    MaxS=-1
    for row in odai_ref:
        try:
            S=model.similarity(UserInput,row[0])
        except KeyError:
            print("odai_ref単語は知りません。栗栖に報告してください。")

        #print(S)
        if S>MaxS:
            MaxS=S
            word0=row[0]
            #print(row[0])
            index_odai=k
        k=k+1
    
    print(word0)
    
    i=i+1
    R=np.random.rand()
    if R>e:
        index=np.argmax(ProbMatBoke, axis = 1)
        index_keyoshi=index[index_odai]
        index=np.argmax(ProbMatWhat, axis = 1)
        index_what=index[index_odai]
    else:
        index_keyoshi=np.random.randint(52)
        index_what=np.random.randint(4)
    k=0
    print(index_keyoshi)
    csv_file = open("DataBase/dataset_keyoshi.csv", "r", encoding="utf-8", errors="", newline="" )
    keyoshi = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    for row in keyoshi:
        if k==index_keyoshi:
            boke=row[0]
            print(boke)
        k=k+1
    
    csv_file = open("DataBase/dataset_odai_ref.csv", "r", encoding="utf-8", errors="", newline="" )
    odai_ref = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    k=0
    if index_what<3:
        for row in odai_ref:
            if k==index_odai:
                example=row[index_what+1]
                if UserInput==word0:
                    what=example
                else:
                    try:
                        what=model.wv.most_similar(positive=[example,UserInput],negative=[word0],topn=5)
                    except KeyError:
                        print("以下のwhat単語データはコーパスにありません。栗栖に報告してください。")
                        print(example)
                    what=what[0][0]
            k=k+1
        answer=what+'が'+boke
    else:
        answer=UserInput+'なのに'+boke

    print(answer)
    
    ChoiceMatBoke[index_odai,index_keyoshi]=ChoiceMatBoke[index_odai,index_keyoshi]+1
    ChoiceMatWhat[index_odai,index_what]=ChoiceMatWhat[index_odai,index_what]+1
    
    print('評価を入力してください。おもしろい：２、まあいいんちゃう：１、おもんない：０（全角）')
    UserInput = input('>> ')
    if UserInput=='２':
        RewardMatBoke[index_odai,index_keyoshi]=RewardMatBoke[index_odai,index_keyoshi]+1
        RewardMatWhat[index_odai,index_what]=RewardMatWhat[index_odai,index_what]+1
    if UserInput=='１':
        RewardMatBoke[index_odai,index_keyoshi]=RewardMatBoke[index_odai,index_keyoshi]+0.5
        RewardMatWhat[index_odai,index_what]=RewardMatWhat[index_odai,index_what]+0.5
    
    ProbMatBoke[index_odai,index_keyoshi]=RewardMatBoke[index_odai,index_keyoshi]/ChoiceMatBoke[index_odai,index_keyoshi]
    ProbMatWhat[index_odai,index_what]=RewardMatWhat[index_odai,index_what]/ChoiceMatWhat[index_odai,index_what]

    if i==100:
        break

f = open('DataBase/ProbMatBoke.csv', 'w')
writer = csv.writer(f, lineterminator='\n')
writer.writerows(ProbMatBoke)
f.close()

f = open('DataBase/RewardMatBoke.csv', 'w')
writer = csv.writer(f, lineterminator='\n')
writer.writerows(RewardMatBoke)
f.close()

f = open('DataBase/ChoiceMatBoke.csv', 'w')
writer = csv.writer(f, lineterminator='\n')
writer.writerows(ChoiceMatBoke)
f.close()

f = open('DataBase/ProbMatWhat.csv', 'w')
writer = csv.writer(f, lineterminator='\n')
writer.writerows(ProbMatWhat)
f.close()

f = open('DataBase/RewardMatWhat.csv', 'w')
writer = csv.writer(f, lineterminator='\n')
writer.writerows(RewardMatWhat)
f.close()

f = open('DataBase/ChoiceMatWhat.csv', 'w')
writer = csv.writer(f, lineterminator='\n')
writer.writerows(ChoiceMatWhat)
f.close()