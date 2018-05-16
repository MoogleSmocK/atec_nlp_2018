# coding=utf-8
import os
os.chdir('/Users/jie/Desktop/蚂蚁ATEC/1_Code')
import pandas as pd
import numpy as np
import re
import json
import jieba
import codecs
jieba.add_word("花呗")
jieba.add_word("借呗")
jieba.add_word("余额宝")

INPUT_FILE_PATH = '../0_Data/atec_nlp_sim_train.csv'
OUTPUT_FILE_PATH1 = '../0_Data/punc_remove_corpus.txt'

ret = []

def seg(text):
    seg_list = jieba.cut(text)
    return " ".join(seg_list)

def punc_remove():
    punctuation = re.compile(u"[-~!@#$%^&*()_+`=\[\]\\\{\}\"|;':,./<>?·！@#￥%……&*（）——+【】、；‘：“”，。、《》？「『」』]")
    with codecs.open(OUTPUT_FILE_PATH,'w','utf-8') as o_f:
        with codecs.open(INPUT_FILE_PATH1,'r','utf-8') as i_f:
            for line in i_f.readlines():
                #print line
                line_split = line.strip().split('\t')
                q1, q2 = line_split[1], line_split[2]
                q1 = punctuation.sub('',q1)
                q2 = punctuation.sub('',q2)
                o_f.write(q1 + '\n' + q2 + '\n')
    return

punc_remove()

OUTPUT_FILE_PATH2 = '../0_Data/split_corpus.txt'
def cut_words():
    count = 0
    with codecs.open(OUTPUT_FILE_PATH2,'w','utf-8') as o_f:
        with codecs.open(OUTPUT_FILE_PATH1,'r','utf-8') as i_f:
            for line in i_f.readlines():
                line = line.strip()
                for word in jieba.cut(line):
                    o_f.write(word + ' ')
                o_f.write('\n')
    return
cut_words()

WORD2VEC_FILE_PATH = '../0_Data/30_word2vec.model'
import gensim
def word2vec_train():
    sentences = gensim.models.word2vec.LineSentence(OUTPUT_FILE_PATH2)
    model = gensim.models.Word2Vec(sentences,size=50,sg=1)
    model.save(WORD2VEC_FILE_PATH)
    return
word2vec_train()

from gensim.models import Word2Vec
model = Word2Vec.load(WORD2VEC_FILE_PATH)

words = model.most_similar(u'花呗')
for word in words:
    print word[0], word[1]
