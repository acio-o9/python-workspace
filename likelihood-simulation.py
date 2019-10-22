#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
尤度について動きを確認する

サッカーのPKを例として、選手がゴールを決めたかどうかを定義する
- 0は、ゴールしなかった
- １は、ゴールした
'''
import numpy as np


# In[ ]:


# 正事象（ゴールを決める確率）の配列を定義
pList = np.arange(0, 1, 0.005)


# In[ ]:


# PKの結果を定義
#pkResult = [0, 1, 1, 1, 0, 1, 1, 1]
pkResult = [0, 0, 0, 1, 0, 0, 0, 1]

goalCount = pkResult.count(1)
missCount = pkResult.count(0)

print('goal count:', goalCount)
print('miss count:', missCount)


# In[ ]:


likelihood = pList**goalCount * (1-pList)**missCount


# In[ ]:


import matplotlib.pyplot as plt
plt.plot(pList, likelihood)
plt.xlabel('p')
plt.ylabel('likelihood')
plt.show()


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

class LikelihoodSimulator(object):
    """
    最適な尤度を観測する
    
    パラメータ
    ----------------
    result 事象のあるなしを表す結果配列
        [0, 1, 1, 0, 1, 0]
    """
    
    def __init__(self, result):
        """
        コンストラクタ
        """
        self.result = result
        self.pList = np.arange(0, 1, 0.005)
        
        # 尤度を決定する
        self.positiveEventCount = result.count(1)
        self.negativeEventCount = result.count(0)
        self.likelihood = pList**self.positiveEventCount * (1-pList)**self.negativeEventCount
    
    def showEventStatus(self):
        """
        入力された結果情報の内訳を出力する
        """
        print('total event count:', len(self.result))
        print('positive event count:', self.positiveEventCount)
        print('negative event count:', self.negativeEventCount)
    
    def showLikelihoodGraph(self):
        """
        正事象ごとの尤度を描画する
        """
        plt.plot(self.pList, self.likelihood)
        plt.xlabel('p')
        plt.ylabel('likelihood')
        plt.show()

        self.getMaxLikelihood()

    def getMaxLikelihood(self):
        """
        尤度が最大になる正事象を返す
        """
        maxl = -1
        maxp = 0

        for p, l in zip(self.pList, self.likelihood):
            if (maxl < l):
                maxl = l
                maxp = p

        print('max likelihood: %.10f' % maxl)
        print('then p:', maxp)


# In[ ]:


res = [1,1,1,1,0,0,1,0,1,1,1,1,1,0,0,1,1]
simulator = LikelihoodSimulator(res)
simulator.showEventStatus()
simulator.showLikelihoodGraph()


# In[ ]:


res = [0,0,0,0,0,0,0]
simulator = LikelihoodSimulator(res)
simulator.showEventStatus()
simulator.showLikelihoodGraph()


# In[ ]:


res = [0,0,0,0,0,0,0,1,1,1,1]
simulator = LikelihoodSimulator(res)
simulator.showEventStatus()
simulator.showLikelihoodGraph()


# In[ ]:




