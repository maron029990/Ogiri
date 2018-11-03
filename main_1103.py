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

"""シリアル設定"""
model = word2vec.Word2Vec.load("DataBase/word2vec.gensim.model")
t=Tokenizer()
Serial = serial.Serial('COM3', 57600, timeout = 10)
serial_control.func_init(Serial)



#関数たち
def Machiuke():
    serial_control.func_taiki(Serial)
    print('おだいをにゅうりょくしてください。endでしゅうりょうします。')
    UserInput = input('>> ')
    odai='こんな'+UserInput+'はいやだ'
    print(odai)
    return UserInput

def MakeAns(odai):
    serial_control.func_think(Serial)
    print('かんがえちゅう…')
    time.sleep(5)
    Atarimae=model.wv.most_similar(positive=['強い',odai],negative=['ジャイアン'],topn=3)
    bokes=model.wv.most_similar(positive=['弱い',Atarimae[0][0]],negative=['強い'],topn=5)
    boke=bokes[0][0]
    answer=odai+'なのに'+boke
    serial_control.func_hirameki(Serial)
    print('ひらめきました!!!')
    time.sleep(3)
    serial_control.func_init(Serial)
    return answer

def DisplayAns(UserInput,answer):
    odai='こんな'+UserInput+'はいやだ' 
    print(odai)
    serial_control.func_ans(Serial)
    time.sleep(3)
    print(answer)
    time.sleep(4)
    
def EstLauLev():
    print('お笑いレベル推定中')
    serial_control.func_eval(Serial)
    print('おもろい:1 おもんない:2')
    level= input('>> ')
    print('評価は…？')
    serial_control.func_ans(Serial)
    time.sleep(3)
    if level=='1':
       print('おもろい！')
       time.sleep(3)
       serial_control.func_happy(Serial)
    else:
       print('おもんない…') 
       time.sleep(3)
       serial_control.func_sad(Serial)
    return level

def RefParam(level):
    print('またひとつ面白くなりました。さようなら。')    
    serial_control.func_thank(Serial)


while 1:
    #待ち受け
    user_input=Machiuke()
    if user_input=='end':#endで終了
        serial_control.func_init(Serial)
        Serial.close()
        break

    #受付
    sys_ans=MakeAns(user_input)

    #回答
    DisplayAns(user_input,sys_ans)
    
    #評価
    Level=EstLauLev()

    #挨拶
    RefParam(Level)

        

    