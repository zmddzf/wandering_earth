# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 20:53:50 2019

@author: zmddzf
"""
import jieba
import jieba.analyse
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def filter_punctuation(sent):
    """
    过滤标点符号
    :param sent: 句子，字符串
    :return afterfilt: 过滤后的字符串
    """
    afterfilt = re.sub("[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%\【】\，\、\。\·\；\：\‘\“\”\']", "", sent)
    sent = afterfilt
    return afterfilt
    
def filter_emoji(sent):
    """
    过滤emoji表情
    :param sent: 句子，字符串
    :return: 过滤后的字符串
    """
    restr = ''
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    sent = co.sub(restr, sent)
    return co.sub(restr, sent)

# 读取影评数据，jieba分词处理
with open('hComments.txt', 'r', encoding="utf-8") as f1:
    hComments = " ".join(jieba.analyse.extract_tags(f1.read(), topK=100))

with open('mComments.txt', 'r', encoding="utf-8") as f2:
    mComments = " ".join(jieba.analyse.extract_tags(f2.read(), topK=100))

with open('lComments.txt', 'r', encoding="utf-8") as f3:
    lComments = " ".join(jieba.analyse.extract_tags(f3.read(), topK=100))
    
# 处理影评数据
hComments = filter_punctuation(hComments)
hComments = filter_emoji(hComments)

mComments = filter_punctuation(mComments)
mComments = filter_emoji(mComments)

lComments = filter_punctuation(lComments)
lComments = filter_emoji(lComments)

# 初始化词云图对象
wc = WordCloud(
    font_path='simhei.ttf',     # 字体
    background_color='white',   # 背景颜色
    width=1000,
    height=600,
    max_font_size=50,            # 字体大小
    min_font_size=10,
    mask=plt.imread('earth.jpg'), # 背景图片
    max_words=1000
)


wc.generate(lComments)
wc.to_file('lComments.png')

wc.generate(mComments)
wc.to_file('mComments.png')

wc.generate(hComments)
wc.to_file('hComments.png')
