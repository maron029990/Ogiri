# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 19:09:06 2018

@author: 010180079
"""

from gensim.models import word2vec
from janome.tokenizer import Tokenizer
import time
import serial
import serial_control
import threading

"""シリアル設定"""
model = word2vec.Word2Vec.load("DataBase/word2vec.gensim.model")
t=Tokenizer()
Serial = serial.Serial('COM3', 57600, timeout = 10)
serial_control.func_init(Serial)

"""状態をあらわすグローバル変数"""
global S 



def Machiuke():
    print('お題受付')
    print('おだいをにゅうりょくしてください')
    UserInput = input('>> ')
    odai='こんな'+UserInput+'はいやだ'
    print(odai)
    return UserInput

def MakeAns(odai):
    print('考え中')
    print('かんがえちゅう…')
    time.sleep(5)
    Atarimae=model.wv.most_similar(positive=['素早い',odai],negative=['忍者'],topn=3)
    print(Atarimae[0][0])
    bokes=model.wv.most_similar(positive=['遅い',Atarimae[0][0]],negative=['素早い'],topn=5)
    i=0
    while(i<5): 
        boke=bokes[i][0]
        print(boke)
        token=t.tokenize(boke)[0]
        print(token.part_of_speech.split(',')[0])
        answer=odai+'なのに'+boke
        print(answer)
        i=i+1
    
    return answer

def DisplayAns(UserInput,answer):
    odai='こんな'+UserInput+'はいやだ'
    print(odai)
    time.sleep(5)
    print(answer)
    time.sleep(5)
    
def EstLauLev():
    print('お笑いレベル推定中')
    time.sleep(5)
    level=4
    print('お笑いレベルは大ウケです')
    return level

def RefParam(level):
    print('またひとつ面白くなりました')    


S=0


while 1:
    if S==0:
        thread_1 = threading.Thread(target=serial_control.func_taiki(Serial))
        thread_1.start()
        user_input=Machiuke()
        if user_input=='end':
            break
        S=1
        
    if S==1:
        thread_2 = threading.Thread(target=serial_control.func_think(Serial))
        thread_2.start()
        sys_ans=MakeAns(user_input)
        S=2
    
    if S==2:
        thread_3 = threading.Thread(target=serial_control.func_hirameki(Serial))
        thread_3.start()
        DisplayAns(user_input,sys_ans)
        S=3
            
    if S==3:
        thread_4 = threading.Thread(target=serial_control.func_ans(Serial))
        thread_4.start()
        Level=EstLauLev()
        S=4
    
    if S==4:
        thread_5 = threading.Thread(target=serial_control.func_thank(Serial))
        thread_5.start()
        RefParam(Level)
        S=0
        
Serial.close()
    