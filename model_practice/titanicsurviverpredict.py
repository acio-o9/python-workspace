# -*- coding: utf-8 -*-
"""TitanicSurviverPredict.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NWdGBiECHfa2BOf02maaLmxzhjDzswMg
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
FIXED_RESULT = 1 # use random_state for fixed result

train_data = pd.read_csv('drive/My Drive/train_data/titanic_train.csv')
train_data.head()

train_data.isnull().sum()

# preprocessing
sex_mapping = {'male': 1, 'female': 0}
train_data['Sex'] = train_data['Sex'].map(sex_mapping)
train_data.head()

# guess Age by Sex and Pclass for no Age 
guess_ages = np.zeros((2,3))

for i in range(0, 2):
    for j in range(0, 3):
        guess_df = train_data[(train_data['Sex'] == i) & (train_data['Pclass'] == j+1)]['Age'].dropna()
        age_guess = guess_df.median()
        guess_ages[i, j] = int( age_guess/0.5 + 0.5 ) * 0.5

for i in range(0, 2):
    for j in range(0, 3):
        # fill guess_ages
        train_data.loc[ (train_data.Age.isnull()) & (train_data.Sex == i) & (train_data.Pclass == j+1), 'Age'] = guess_ages[i, j]

train_data['Age'] = train_data['Age'].astype(int)
train_data.head()

train_data['AgeBand'] = pd.cut(train_data['Age'], 5)
train_data[['AgeBand', 'Survived']].groupby(['AgeBand'], as_index=False).mean().sort_values(by='AgeBand', ascending=True)

train_data.loc[ train_data['Age'] <= 16, 'Age'] = 0
train_data.loc[ (train_data['Age'] > 16) & (train_data['Age'] <= 32), 'Age'] = 1
train_data.loc[ (train_data['Age'] > 32) & (train_data['Age'] <= 48), 'Age'] = 2
train_data.loc[ (train_data['Age'] > 48) & (train_data['Age'] <= 64), 'Age'] = 3
train_data.loc[ train_data['Age'] > 64, 'Age']
train_data.head()

train_data['FamilySize'] = train_data['SibSp'] + train_data['Parch'] + 1
train_data[['FamilySize', 'Survived']].groupby(['FamilySize'], as_index=False).mean().sort_values(by='Survived', ascending=False)

train_data['IsAlone'] = 0
train_data.loc[train_data['FamilySize'] == 1, 'IsAlone'] = 1
train_data[['IsAlone', 'Survived']].groupby('IsAlone').mean().sort_values(by='Survived', ascending=False)

train_data['Embarked'].isnull().sum()

print('total size:', len(train_data))
train_data[['Embarked', 'Survived']].groupby('Embarked').count()

168+77+644

# null record fills frequency value 'S'
train_data.loc[train_data.Embarked.isnull(), 'Embarked'] = 'S'
train_data[['Embarked', 'Survived']].groupby('Embarked').count()

train_data[['Embarked', 'Survived']].groupby('Embarked', as_index=False).mean().sort_values(by='Survived', ascending=False)

embarked_mapping = {"C": 1, "Q": 2, "S": 3}
train_data['Embarked'] = train_data['Embarked'].map(embarked_mapping).astype(int)

feature_label = [
                 'Pclass',
                 'Sex',
                 'Age',
                 'IsAlone',
                 'Fare',
                 'Embarked',
]
X = pd.DataFrame(train_data[feature_label])
y = pd.DataFrame(train_data.iloc[:, 1]) # Survived
X.head()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=FIXED_RESULT)
print(X_train.shape)
print(X_test.shape)

# modeling
from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(n_estimators=500, random_state=FIXED_RESULT)
forest.fit(X_train, y_train)
# prediction
forest.score(X_test, y_test)

