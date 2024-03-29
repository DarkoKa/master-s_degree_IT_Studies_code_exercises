# -*- coding: utf-8 -*-
"""DryBeanClassification

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15LiKT4WnFL2u1zpamPw9PXvyAs2b1DCR
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# Mount the drive
# import Google drive
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

#!ls /content/drive/MyDrive/ColabNotebooks/datas/Dry_Bean_Dataset.xlsx
file_path = '/content/drive/MyDrive/ColabNotebooks/datas/Dry_Bean_Dataset.xlsx'

data = pd.read_excel(file_path)

data.head()

data.info()

data.columns

data.shape

data.describe().T

data.isnull().sum()

data['Class'].unique()

data['Class'].value_counts()

labelencoder = LabelEncoder()
data["Class"] = labelencoder.fit_transform(data['Class'])

data = data.drop_duplicates()

x = data.iloc[:,0:16]
y = data.iloc[:,16:]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.33, random_state = 42)

standardscaler = StandardScaler()
x_train  = standardscaler.fit_transform(X_train)
x_test = standardscaler.fit_transform(X_test)

# KNN
knn_classifier = KNeighborsClassifier(n_neighbors = 35)
knn_classifier.fit(x_train, y_train)
y_predict = knn_classifier.predict(x_test)
y_predict

acc = accuracy_score(y_test, y_predict)
print(acc)