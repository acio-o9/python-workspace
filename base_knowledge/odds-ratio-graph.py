#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
# 正事象を0.01 ~ 1までの間 で定義
p = np.arange(0.005, 1, 0.005)

p


# In[ ]:


# オッズ比を計算
oddsRatio = p/(1-p)
oddsRatio


# In[ ]:


import matplotlib.pyplot as plt
# 正事象とオッズ比の関係図を描画
plt.plot(p, oddsRatio)
plt.xlabel('p')
plt.ylabel('oddsRatio')
plt.show()


# In[ ]:


# 対数オッズを計算
import math
lo = []
for yi in oddsRatio:
    lo.append(math.log(yi))


# In[ ]:


# 正事象と対数オッズの関係図を描画
plt.plot(p, lo)
plt.xlabel('p')
plt.ylabel('odds ration logarithm')
plt.show()


# In[ ]:




