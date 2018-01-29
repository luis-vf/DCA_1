# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 00:11:22 2018

@author: Luis
"""

asm = open("test1.mif","r")

a = asm.readlines()
isa =[]

for i in range(len(a)):
    if 'CONTENT BEGIN' in a[i]:
        isa[1:len(a)-i-1] = a[i+1:len(a)]

del isa[len(isa)-2:len(isa)]
for i in range(len(isa)):    
    isa[i] = str.split(isa[i].replace(':','').replace(';',''))
    isa[i][1] = bin(int(('0x'+ isa[i][1]),16)).replace('0b','')