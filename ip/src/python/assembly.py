# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:51:26 2018

@author: Luis
"""

asm = open("test0.txt","r")

a = asm.readlines()

asm_dict = {}
for x in range(len(a)):
    a[x] = a[x].replace('\n','')
    a[x] = a[x].replace(',','')
    asm_dict[x] = str.split(a[x])

def extract(string, start='(', stop=')'):
        return string[string.index(start)+1:string.index(stop)]

#checks to see if mips function is a key in dictionary
b = (asm_dict[0][0] in mips_dict.keys())
if b == True:
    print("swag")

mips_dict = {
    #standard rtype instructions
    "add": ["$rd","$rs","$rt"],
    "addu": ["$rd","$rs","$rt"],
    "sub": ["$rd","$rs","$rt"],
    "subu": ["$rd","$rs","$rt"],
    "and": ["$rd","$rs","$rt"],
    "or": ["$rd","$rs","$rt"],
    "xor": ["$rd","$rs","$rt"],
    "nor": ["$rd","$rs","$rt"],
    "slt": ["$rd","$rs","$rt"],
    "sltu": ["$rd","$rs","$rt"],
    "sll": ["$rd","$rs","shamt"],
    "srl": ["$rd","$rs","shamt"],
    "sra": ["$rd","$rs","shamt"],
    "sllv": ["$rd","$rs","$rt"],
    "srlv": ["$rd","$rs","$rt"],
    "srav": ["$rd","$rs","$rt"],
    #2 PARAMETER RTYPE
    "jalr": ["$rd","$rs"],
    "mult": ["$rs","$rt"],
    "multu": ["$rs","$rt"],
    #1 parameter rtype
    "mfhi": ["$rd"],    
    "mflo": ["$rs"],
    "mthi": ["$rd"], 
    "mtlo": ["$rs"],
    "jr" : ["$rs"],

    #jtype
    "j": ["addr"],
    "jal": ["addr"],
    
    #itype
    "beq":["$rs","$rt","imm"],
    "bne":["$rs","$rt","imm"],
    "blez":["$rs","imm"],
    "bgtz":["$rs","imm"],
    "bltz":["$rs","imm"],
    "bgez":["$rs","imm"],

    "addi":["$rt","$rs","imm"],
    "addiu":["$rt","$rs","imm"],
    "slti":["$rt","$rs","imm"],
    "sltiu":["$rt","$rs","imm"],
    "ori":["$rt","$rs","imm"],
    "xori":["$rt","$rs","imm"],

    "lw":["$rt","imm","$rs"],
    "lwl":["$rt","imm","$rs"],
    "lwr":["$rt","imm","$rs"],
    "lh":["$rt","imm","$rs"],
    "lui":["$rt","imm","$rs"],
    "lbu":["$rt","imm","$rs"],
    "lhu":["$rt","imm","$rs"],
    "lb":["$rt","imm","$rs"],
    "sb":["$rt","imm","$rs"],
    "sh":["$rt","imm","$rs"],
    "sw":["$rt","imm","$rs"],
}