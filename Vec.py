from gensim.models import word2vec
from janome.tokenizer import Tokenizer
import numpy as np
import sys
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


model = word2vec.Word2Vec.load("DataBase/word2vec.gensim.model")
#調べる情報を配列に収納
capital_name = []
capital_name.append(["のび太","強い","Nobita","Strong"])
capital_name.append(["ジャイアン","優しい","Gian","Kind"])
capital_name.append(["東京","田舎","Tokyo","Inaka"])
capital_name.append(["忍者","派手","Ninja","Hade"])
 
length = len(capital_name)
data = []
 
j = 0
while j < length:
    print(capital_name[j][1])
    data.append(model[capital_name[j][0]])
    data.append(model[capital_name[j][1]])
    j += 1
 
pca = PCA(n_components=2)
pca.fit(data)
data_pca= pca.transform(data)
 
length_data = len(data_pca)
 
i = 0
j = 0
while i < length_data:
    #点プロット
    plt.plot(data_pca[i][0], data_pca[i][1], ms=5.0, zorder=2 ,marker="x")
    plt.plot(data_pca[i+1][0], data_pca[i+1][1],ms=5.0, zorder=2 ,marker="x")
 
    #線プロット
    plt.plot((data_pca[i][0], data_pca[i+1][0]),(data_pca[i][1],data_pca[i+1][1]),c="b",linewidth=0.5,zorder=1,linestyle="--")
 
    #文字プロット
    plt.annotate(capital_name[j][2],(data_pca[i][0], data_pca[i][1]),size=7)
    plt.annotate(capital_name[j][3],(data_pca[i+1][0], data_pca[i+1][1]),size=7)
 
    j += 1
    i += 2
 
plt.show()