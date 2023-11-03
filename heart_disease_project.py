# -*- coding: utf-8 -*-
"""heart disease project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZtrWtjpcaf1upmCZH0Bj39DYZGolHS2e
"""

import pandas as pd

df = pd.read_csv('/content/heart disease.csv')
print(type(df))

df.head()

df.dtypes

df.head()
print("df.shape -->", df.shape)
print("Rows     -->", df.shape[0])  ##axis 0---row
print("Columns  -->", df.shape[1])   ###column

df.head()

df.tail()
df.columns

df.describe()

df.info()

import matplotlib.pyplot as plt
print("matplotlib is imported")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('heart disease.csv')
df.head()

x = df['age']
y = df['target']

plt.xlabel('age')                                   
plt.ylabel('target')
plt.title('target Vs age')

plt.bar(x, y, color = "purple")

plt.show()

x = df['age']
y = df['thal']

plt.xlabel('age')                                   
plt.ylabel('thal')
plt.title('thal Vs age')

plt.scatter(x, y, marker = "*")

# marker {'o','+','x','^','*','_'}

plt.show()

x = df['age']
y = df['target']

plt.xlabel('age')                                   
plt.ylabel('target')
plt.title('target Vs age')
plt.plot(x, y)
plt.savefig("testImage2.jpg", dpi=300)
plt.show()

x = df['age']
y = df['target']

plt.xlabel('age')                                   
plt.ylabel('target')
plt.title('target Vs age')

plt.bar(y, x, color = "green")

plt.show()

!pip install pycaret &> /dev/null
print ("Pycaret installed sucessfully!!")

from pycaret.utils import version
version()

from pycaret.datasets import get_data

dataSets = get_data('index')

heartdiseaseDataSet = get_data("heart_disease")
print(type(heartdiseaseDataSet))

import pandas as pd
heartdiseaseDataSet = pd.read_csv("heart disease.csv")

heartdiseaseDataSet.columns

heartdiseaseDataSet.describe()

print("type(heartdiseaseDataSet)-->",type(heartdiseaseDataSet))

print("heartdiseaseDataSet.shape -->", heartdiseaseDataSet.shape)
print("Rows     -->", heartdiseaseDataSet.shape[0])  ##axis 0---row
print("Columns  -->", heartdiseaseDataSet.shape[1])   ###column

heartdiseaseDataSet.head()

heartdiseaseDataSet.loc[10:100 , ['target','age']]

heartdiseaseDataSet.iloc[20:30, 1:5]

heartdiseaseDataSet.mean()

heartdiseaseDataSet.max()

heartdiseaseDataSet.isnull().sum()

heartdiseaseDataSet.dropna(axis = 'columns')

heartdiseaseDataSet.fillna(0)

import matplotlib.pyplot as plt
x = heartdiseaseDataSet['age']

plt.xlabel('age')                                   
plt.ylabel('target')
plt.title('target Vs age')

plt.hist(x, color = "red", bins=50)

plt.show()

import matplotlib.pyplot as plt

## Scatter plot
import matplotlib.pyplot as plt
x = heartdiseaseDataSet['age']
y = heartdiseaseDataSet['thal']

plt.xlabel('age')                                   
plt.ylabel('thal')
plt.title('thal Vs age')

plt.scatter(x, y, marker = "*",color = "red")

plt.show()

import matplotlib.pyplot as plt
x=tuple(range(768))
x = heartdiseaseDataSet['age']
y = heartdiseaseDataSet['target']

plt.xlabel('age')                                   
plt.ylabel('target')
plt.title('target Vs age')
plt.subplot(121)
plt.hist(x, color = "red", bins=50)
#########################################################################
x = heartdiseaseDataSet['age']
y = heartdiseaseDataSet['target']

plt.xlabel('age')                                   
plt.ylabel('target')
plt.title('target Vs age')
plt.subplot(122)
plt.scatter(x, y, marker = "*",color = "red")

plt.show()

"""## RANDOM FOREST MODEL"""

from pycaret.classification import *

heartdiseaseDataSet = get_data("heart disease")
s = setup(data=heartdiseaseDataSet, target='target', silent=True)

rfModel = create_model('rf')
plot_model(rfModel, plot='confusion_matrix')

"""## ADA BOOST CLASSIFIER"""

from pycaret.classification import *

heartdiseaseDataSet = get_data("heart disease")
s = setup(data=heartdiseaseDataSet, target='target', silent=True)

adaModel=create_model('ada')
plot_model(adaModel, plot='confusion_matrix')

"""## DECISION TREE CLASSIFIER"""

from pycaret.classification import *

heartdiseaseDataSet = get_data("heart disease")
s = setup(data=heartdiseaseDataSet, target='target', silent=True)

dtModel=create_model('dt')
plot_model(dtModel, plot='confusion_matrix')

"""## LINEAR DISCRIMINANT ANALYSIS"""

from pycaret.classification import *

heartdiseaseDataSet = get_data("heart disease")
s = setup(data=heartdiseaseDataSet, target='target', silent=True)

ldaModel=create_model('lda')
plot_model(ldaModel, plot='confusion_matrix')

sm = save_model(rfModel, 'rfModelFile')

sm = save_model(adaModel, 'adaModelFile')

sm = save_model(dtModel, 'dtModelFile')

sm = save_model(ldaModel, 'ldaModelFile')

rfModel = create_model('rf', verbose=True)
plot_model(rfModel, plot='feature')

adaModel = create_model('ada', verbose=True)
plot_model(adaModel, plot='feature')

dtModel = create_model('dt', verbose=True)
plot_model(dtModel, plot='feature')

ldaModel = create_model('lda', verbose=True)
plot_model(ldaModel, plot='feature')

from pycaret.classification import *
s = setup(data=heartdiseaseDataSet, target='target', silent=True)

cm = compare_models()

from pycaret.datasets import get_data
from pycaret.classification import *

heartDiseaseDataSet = get_data("heart disease")
s = setup(data = heartDiseaseDataSet, target='target', silent=True)
cm = compare_models()

s = setup(data=heartdiseaseDataSet, target='target', normalize = True, normalize_method = 'zscore', silent=True)
cm = compare_models()

s = setup(data=heartdiseaseDataSet, target='target', feature_selection = True, feature_selection_threshold = 0.6, silent=True)
cm = compare_models()