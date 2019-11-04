#!/usr/bin/env python
# coding: utf-8

# ランダムフォレストを使用して、タイタニックの生存クラス予測モデルを作成する
# 
# タイタニックのデータをkaggleから取得する。
# 
# ```
# cd ./datasets/titanic
# kaggle competitions download -c titanic
# unzip titanic.zip
# ```

# In[ ]:


import pandas as pd
import numpy as np

import os

for dirname, _, filenames in os.walk('./datasets/titanic'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[ ]:


# データの準備
train_data = pd.read_csv('./datasets/titanic/train.csv')
train_data.head()


# In[ ]:


# 年齢を年齢帯に変更する
# pandas.cutを使用して連続値を離散値として扱うようにする
train_data['AgeBand'] = pd.cut(train_data['Age'], 5)
train_data[['AgeBand', 'Survived']].groupby(['AgeBand'], as_index=False).mean().sort_values(by='AgeBand', ascending=True)


# In[ ]:


# AgeBandの境界値で年齢帯に変更する
train_data.loc[ train_data['Age'] <= 16, 'Age'] = 0
train_data.loc[ (train_data['Age'] > 16) & (train_data['Age'] <= 32), 'Age'] = 1
train_data.loc[ (train_data['Age'] > 32) & (train_data['Age'] <= 48), 'Age'] = 2
train_data.loc[ (train_data['Age'] > 48) & (train_data['Age'] <= 64), 'Age'] = 3
train_data.loc[ train_data['Age'] > 64, 'Age'] = 4
train_data.head()


# In[ ]:


# データの欠損値を埋める
# 一番多い年齢帯を中央値として欠損値を補う
train_data.isnull().sum()


# In[ ]:


train_data.groupby('Age').size()


# In[ ]:


# 一番ウェイトの大きい年齢帯1（16 - 32歳）で欠損値を埋める
train_data['Age'] = train_data['Age'].fillna(1)


# In[ ]:


train_data.groupby('Age').size()


# In[ ]:


features = ['Pclass', "Sex", "SibSp", "Parch", 'Age']
y = train_data.Survived
X = pd.get_dummies(train_data[features])

# トレーニング用とテスト用に、データを分割する
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

print('train_data count : ', len(X_train))
print('test_data count : ', len(X_test))


# RandomForestClassifierのパラメータ
# 
# - n_estimators：用意する決定木の数 
# - max_depth：使用する決定木の深さ
# - random_state：シード値

# In[ ]:


# モデルの生成
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
rfc.fit(X_train, y_train)
rfc.predict_proba(X_test[:5]).argmax(axis=1)


# In[ ]:


# 精度を確認する
rfc.score(X_test, y_test)

