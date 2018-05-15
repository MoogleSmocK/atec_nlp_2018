## import the package needed

import jieba.posseg as pseg
import jieba
import sys
from data_process import t_2_s
import math
from read_train  import read_the_two_part

## add the keywords in segment besides their pos

jieba.add_word('花呗',57419,'n')
jieba.add_word('借呗',23730,'n') 
jieba.add_word('支付宝',3275,'n') 
jieba.add_word('淘宝网',13,'n') 
jieba.add_word('淘宝',1467,'n') 

## edit_distance function

## edit distance
## to enter the two string
def edit_distance(words_a,words_b):
    length_a = len(words_a)
    length_b = len(words_b)
    matrix = [[i] for i in range(length_a + 1)]
    for i in range(length_a + 1 ):
        for j in range(1,length_b+1):
            if i ==0:
                matrix[0].append(j)
            else:
                if words_a[i-1] == words_b[j-1] :count = 0
                else:count = 1
                matrix[i].append(min(matrix[i][j-1]+1,matrix[i-1][j]+1,count+matrix[i-1][j-1]))
    return matrix[length_a][length_b]


## cos sentence_distance function rely on the word

#### sentence distance
#### use cos to calculate
#### to enter the two word list
def wordsvec_distance(list1,list2):
    total_words = list(set(list1+list2))
    numerator = 0
    denominator1 = 0
    denominator2 = 0
    for word in total_words:
        numerator += list1.count(word) * list2.count(word)
        denominator1 +=  list1.count(word) * list1.count(word)
        denominator2 +=  list2.count(word) * list2.count(word)
    return numerator / ( math.sqrt(denominator1) * math.sqrt(denominator2))

## the number of the same word

### number of the same word occur
def same_word_count(list1,list2):
    res = len(set(list1) & set(list2))
    return res

### number of the total word occur
def total_word_cout(list1,list2):
    res = len(set(list1) | set(list2))
    return res

## segment and choose the matching pos

flag_pos = ['n' , 'v' , 'a'   ,'ad'  ]
def segment_pos(sequence,flag_pos):
    word_seqs = []
    for each_seq in sequence:
        temp= pseg.cut(each_seq)
        seq_temp = [words.word for words in temp if words.flag in flag_pos]
        word_seqs.append( seq_temp )
    return word_seqs

## usage of temp choosing feature

## length of two sequence , edit distance of two sequence
## sentence distance of two word list , length of two word list
## the number of the same words , the number of total word  

