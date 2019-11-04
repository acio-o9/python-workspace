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


features = ['Pclass', "Sex", "SibSp", "Parch"]
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

