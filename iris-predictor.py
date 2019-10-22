#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn import datasets
import numpy as np

# Irisデータセットをロード
iris = datasets.load_iris()
iris


# In[ ]:


iris.feature_names


# In[ ]:


from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

scaler = StandardScaler()

# 使用するデータを準備
X = iris.data
y = iris.target

# ４：１にデータを分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=1)

# トレーニングデータでscalerを更新
scaler.fit(X_train)

# トレーニングデータの標準偏差で、データを標準化
X_train_std = scaler.transform(X_train)
X_test_std = scaler.transform(X_test)


# In[ ]:


from sklearn.linear_model import LogisticRegression

# ロジスティック回帰モデルを生成
lr = LogisticRegression(C=100.0, random_state=1, solver='lbfgs', multi_class='ovr', max_iter=20)

# オリジナルのデータを用いてトレーニングを実施
lr.fit(X_train, y_train)

# テストデータの予測を取得
predict = lr.predict_proba(X_test).argmax(axis=1)

errorCount = (y_test != predict).sum()
print('Accuracy: %.5f' % (1 - (errorCount / len(y_test))))
 
lr.score(X_test, y_test)


# In[ ]:


# ロジスティック回帰モデルを生成
lr = LogisticRegression(C=100.0, random_state=1, solver='lbfgs', multi_class='ovr', max_iter=20)

# 標準化データを用いてトレーニングを実施
lr.fit(X_train_std, y_train)

# 正答率
lr.score(X_test_std, y_test)


# In[ ]:




