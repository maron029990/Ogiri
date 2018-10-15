from gensim.models import word2vec
from janome.tokenizer import Tokenizer


model = word2vec.Word2Vec.load("DataBase/word2vec.gensim.model")
t=Tokenizer()

while(True):
    print('お題を入力してください')
    UserInput = input('>> ')
    odai='こんな'+UserInput+'はいやだ'
    print(odai)

    bokes=model.wv.most_similar(positive=['意地悪',UserInput],negative=['のび太'],topn=5)
    i=0
    while(i<5): 
        boke=bokes[i][0]
        print(boke)
        token=t.tokenize(boke)[0]
        print(token.part_of_speech.split(',')[0])
        answer=UserInput+'なのに'+boke
        print(answer)
        i=i+1
        
