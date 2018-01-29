# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 18:17:40 2018

@author: Luis
"""

mif = open('dict.txt','r')
s =  mif.readlines()
stuf = {}
b= {}
a = {}
for i in range(len(s)):
    s[i] = s[i].replace('\n','').replace('[','').replace(']','').replace(':',' ').replace(',',' ')
    stuf[i] = str.split(s[i])
    
    
for {} in stuf:
    stuf.remove({})
    
#for j in range(len(stuf)):
  #  b[j] = stuf[j][1]