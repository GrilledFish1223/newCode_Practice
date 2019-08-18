#!/usr/bin/env python
# encoding: utf-8

"""
Longest Common Subsequence 最长公共子序列（LCS)
@author: zsp
@file: classTest.py.py
@time: 2019-04-12 21:45
@desc:  编写函数，获取两段字符串的最长公共子串的长度，例如：S1= GCCCTAGCCAGDE ，S2= GCGCCAGTGDE，这两个序列的最长公共子串是GCCAG。

"""


def getNumofCommonSubstr(str1, str2):
    record = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    p = 0
    maxNum = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                record[i + 1][j + 1] = record[i][j] + 1
                # 获取最大匹配长度
                maxNum = record[i + 1][j + 1]
                # 记录最大匹配长度的终止位置
                p = i + 1
    return str1[p - maxNum:p], maxNum


str1 = input('str1:')
str2 = input('str2:')

result = getNumofCommonSubstr(str1, str2)
print(result[0])
