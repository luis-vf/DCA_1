# - :[- coding: utf-8 - :[-
"""
Created on Mon Jan 29 17:03:39 2018

@author: Luis
"""

mif = open('test0 -mason.mif' , 'r')

mifstr =  mif.readlines()

code = {}

r_dict = {
    #standard rtype instructions
    "100000": [ "add" , "$rd" , "$rs" , "$rt"] , 
    "100001": [ "addu" , "$rd" , "$rs" , "$rt"] , 
    "100010": [ "sub" , "$rd" , "$rs" , "$rt"] , 
    "100011": [ "subu" , "$rd" , "$rs" , "$rt"] , 
    "100100": [ "and" , "$rd" , "$rs" , "$rt"] , 
    "100101": [ "or" , "$rd" , "$rs" , "$rt"] , 
    "100110": [ "xor" , "$rd" , "$rs" , "$rt"] , 
    "100111": [ "nor" , "$rd" , "$rs" , "$rt"] , 
    "101010": [ "slt" , "$rd" , "$rs" , "$rt"] , 
    "101011": [ "sltu" , "$rd" , "$rs" , "$rt"] , 
    "000000": [ "sll" , "$rd" , "$rt" , "shamt"] , 
    "000010": [ "srl" , "$rd" , "$rt" , "shamt"] , 
    "000011": [ "sra" , "$rd" , "$rt" , "shamt"] , 
    "000100": [ "sllv" , "$rd" , "$rs" , "$rt"] , 
    "000110": [ "srlv" , "$rd" , "$rs" , "$rt"] , 
    "000111": [ "srav" , "$rd" , "$rs" , "$rt"] , 
    #2 PARAMETER RTYPE
    "001001": [ "jalr" , "$rd" , "$rs"] , 
    "011000": [ "mult" , "$rs" , "$rt"] , 
    "011001": [ "multu" , "$rs" , "$rt"] , 
    #1 parameter rtype
    "010000": [ "mfhi" , "$rd"] ,     
    "010010": [ "mflo" , "$rs"] , 
    "010001": [ "mthi" , "$rd"] ,  
    "010011": [ "mtlo" , "$rs"] , 
    "001000": [ "jr" , "$rs"] , 
}
j_dict = {
    #jtype
    "000010": [ "j" , "addr"] , 
    "000011": [ "jal" , "addr"]
   }
i_dict ={
    #itype
    "000100":["beq" , "$rs" , "$rt" , "imm"] , 
    "000101" :["bne" , "$rs" , "$rt" , "imm"] , 
    "000110" :["blez" , "$rs" , "00000" , "imm"] , 
    "000111" :["bgtz","000111" , "$rs" , "00000" , "imm"] , 
    
    #itype
    "001000"  :["addi", "$rt" , "$rs" , "imm"] , 
    "001100" :["andi" , "$rt" , "$rs" , "imm"] , 
    "001001" :["addiu" , "$rt" , "$rs" , "imm"] , 
    "001010" :["slti" , "$rt" , "$rs" , "imm"] , 
    "001011" :["sltiu" , "$rt" , "$rs" , "imm"] , 
    "001101" :["ori" , "$rt" , "$rs" , "imm"] , 
    "001110" :["xori" , "$rt" , "$rs" , "imm"] , 

    "100011" :["lw" , "$rt" , "imm" , "$rs"] , 
    "100010" :["lwl" , "$rt" , "imm" , "$rs"] , 
    "100110" :["lwr" , "$rt" , "imm" , "$rs"] , 
    "100001" :["lh" , "$rt" , "imm" , "$rs"] , 
    "001111" :["lui" , "$rt" , "imm"] , 
    "100100" :["lbu" , "$rt" , "imm" , "$rs"] , 
    "100101" :["lhu" , "$rt" , "imm" , "$rs"] , 
    "100000" :["lb" , "$rt" , "imm" , "$rs"] , 
    "101000" :["sb" , "$rt" , "imm" , "$rs"] , 
    "101001" :["sh" , "$rt" , "imm" , "$rs"] , 
    "101011" :["sw" , "$rt" , "imm" , "$rs"]
 } 
ri_dict ={  
     #ri type
    "00000" :["bltz" , "$rs" , "imm"] , 
    "00001" :["bgez" , "$rs" , "imm"] , 
    "10000" :["bltzal" , "$rs" , "imm"] , 
    "10001":["bgezal" , "$rs" , "imm"]
}

R =['000000','sssss','ttttt','ddddd','mmmmm','ffffff']
RI= ['000001', 'sssss', 'RRRRR', 'CCCCCCCCCCCCCCCC']
I = ['EEEEEE', 'sssss', 'ttttt', 'CCCCCCCCCCCCCCCC']
J = ['EEEEEE','AAAAAAAAAAAAAAAAAAAAAAAAAA']

def checktype(opcode):
    if "000000" in opcode:
        return 'R'
    elif "000001" in opcode:
        return 'RI'
    elif opcode in i_dict.keys():
        return 'I'
    elif opcode in j_dict.keys():
        return 'J'
    else:
        return 'fake opcode'
def getR(mc):
    s = mc[6:11]
    t = mc[11:16]
    d = mc[16:21]
    shamt = mc[21:26]
    f = mc[26:32]
    x = r_dict[f]
    for i in range(len(r_dict[f])):
        if(r_dict[f][i] == '$rs'):
            x[i] = '$' + str(int(s,2))
        elif(r_dict[f][i] == '$rd'):
            x[i] = '$' + str(int(d,2))
        elif(r_dict[f][i] == '$rt'):
            x[i] = '$' + str(int(t,2))
        elif(r_dict[f][i] == 'shamt'):
            x[i] = str(int(shamt,2))
    return x[0]+ ' '+', '.join(x[1:len(x)])


def sign(i):
    if i >= 2047:
        return str(i-2048)
    else:
        return str(i)
    
def getI(mc):
    o = mc[0:6]
    s = mc[6:11]
    t = mc[11:16]
    imm = mc[21:32]
    x = i_dict[o]
    for i in range(len(i_dict[o])):
        if(i_dict[o][i] == '$rt'):
            x[i] = '$' + str(int(t,2))
        elif(i_dict[o][i] == 'imm'):
            if 'sw' in i_dict[o][0]:
                x[i] = '0x' + hex(int(imm,2)).replace('0x','').zfill(4)
            else:
                x[i] = sign(int(imm,2))
        elif(i_dict[o][i] == '$rs'):
            if i_dict[o][i-1] == 'imm':
                x[i] = '($' + str(int(s,2)) +')'
            else:
                x[i] = '$' + str(int(s,2))
        if i_dict[o][2] == 'imm':
            x[3] = '($' + str(int(s,2)) +')'
    if '(' in x[3]:       
        return x[0] + ' ' + x[1] + ', '+''.join(x[2:len(x)])
    else:  
        return x[0]+ ' '+', '.join(x[1:len(x)])
    
def getJ(mc):
    return j_dict[mc[0:6]][0] +' 0x' + hex(int(mc[6:32],2)<<2).replace('0x','').zfill(8)

def cleancode():
    start = 0
    end = 0
    for i in range(len(mifstr)):
        if 'CONTENT BEGIN' in mifstr[ i]:
            start = i + 1
        if '[ ' in mifstr[ i]:
            end = i
        mifstr[ i] = str.split(mifstr[ i])
        mifstr[ i] = mifstr[ i]
    mifstr[ 0:start-end+1] = mifstr[ start:end]
    del mifstr[ start-end+1:len(mifstr)+1]
    for i in range(len(mifstr)):
        code[ i] = mifstr[ i][ 2].replace(';' , '')
        code[ i] = bin(int('0x'+code[ i] , 16)).replace('0b' , '')

cleancode()
print(getR('00000011111110000000001111100001'))
print(getJ('1000000100000000000000001101'.zfill(32)))
print(hex(int('0x400025',16)>>2))
