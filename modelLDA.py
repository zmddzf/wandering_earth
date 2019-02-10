# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 22:04:51 2019

@author: zmddzf
"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import jieba
import pyLDAvis
import pyLDAvis.sklearn

# 读取评论数据
hComments = []
with open('hComments.txt', 'r', encoding="utf-8") as f1:
    for line in f1:
        hComments.append(" ".join(jieba.cut(line)))

mComments = []
with open('mComments.txt', 'r', encoding="utf-8") as f2:
    for line in f2:
        mComments.append(" ".join(jieba.cut(line)))
        
lComments = []
with open('lComments.txt', 'r', encoding="utf-8") as f3:
    for line in f3:
        lComments.append(" ".join(jieba.cut(line)))

# 合并评论数据
comments = hComments + mComments + lComments
df = pd.DataFrame(comments)

# 关键词提取和向量转化
tfVectorizer = CountVectorizer(strip_accents = 'unicode',
                                max_features = 1000,
                                max_df = 0.5,
                                min_df = 10
                                )
tf = tfVectorizer.fit_transform(df[0])

# 初始化lda
lda = LatentDirichletAllocation(n_topics = 3,
                                max_iter =50,
                                learning_method = 'online',
                                learning_offset = 50,
                                random_state = 0)
lda.fit(tf)  # 训练

# 可视化lda
data = pyLDAvis.sklearn.prepare(lda, tf, tfVectorizer)
pyLDAvis.show(data)