import numpy as np
import pandas as pd
import csv
import os 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import pickle

folder = os.path.join(os.getcwd(), 'data' + '\\')
df = pd.DataFrame(columns=['Company','Timestamp','Label','Headline'])
for i in os.scandir(folder):
    path = folder + i.name
    a = pd.read_csv(path,sep=',',names=['Company','Timestamp','Label','Headline'],skiprows=[0])
    df = pd.concat([df,a])
df_x=df["Headline"]
df_y=df["Label"]
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)
cv1 = CountVectorizer()
x_traincv=cv1.fit_transform(x_train)

x_testcv=cv1.transform(x_test)

x_testcv.toarray()

nn = MLPClassifier()

y_train=y_train.astype('int')

nn.fit(x_traincv,y_train)

predictions=nn.predict(x_testcv)

a=np.array(y_test)

count=0

for i in range (len(predictions)):
    if predictions[i]==a[i]:
        count=count+1
pickle.dump(nn, open("nnmodel.h5", 'wb'))

print('The accurate rate of neural network is: '+ str(count/len(predictions)))



