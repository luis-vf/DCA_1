# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:51:26 2018

@author: Luis
"""

asm = open("test0.txt","r")

a = asm.readlines()



mips_dict = {
    #standard rtype instructions
    "add": ["100000","$rd","$rs","$rt"],
    "addu": ["100001","$rd","$rs","$rt"],
    "sub": ["100010","$rd","$rs","$rt"],
    "subu": ["100011","$rd","$rs","$rt"],
    "and": ["100100","$rd","$rs","$rt"],
    "or": ["100101","$rd","$rs","$rt"],
    "xor": ["100110","$rd","$rs","$rt"],
    "nor": ["100111","$rd","$rs","$rt"],
    "slt": ["101010","$rd","$rs","$rt"],
    "sltu": ["101011","$rd","$rs","$rt"],
    "sll": ["000000","$rd","$rs","shamt"],
    "srl": ["000010","$rd","$rs","shamt"],
    "sra": ["000011","$rd","$rs","shamt"],
    "sllv": ["000100","$rd","$rs","$rt"],
    "srlv": ["000110","$rd","$rs","$rt"],
    "srav": ["000111","$rd","$rs","$rt"],
    #2 PARAMETER RTYPE
    "jalr": ["001001","$rd","$rs"],
    "mult": ["011000","$rs","$rt"],
    "multu": ["011001","$rs","$rt"],
    #1 parameter rtype
    "mfhi": ["010000","$rd"],    
    "mflo": ["010010","$rs"],
    "mthi": ["010001","$rd"], 
    "mtlo": ["010011","$rs"],
    "jr" : ["001000","$rs"],

    #jtype
    "j": ["000010","addr"],
    "jal": ["000011","addr"],
    
    #itype
    "beq":["000100","$rs","$rt","imm"],
    "bne":["000101","$rs","$rt","imm"],
    "blez":["000110","$rs","00000","imm"],
    "bgtz":["000111","$rs","00000","imm"],
    
     #ri type
    "bltz":["00000","$rs","imm"],
    "bgez":["00001","$rs","imm"],
    "bltzal":["10000","$rs","imm"],
    "bgezal":["10001","$rs","imm"],
    
    #itype
    "addi":["001000","$rt","$rs","imm"],
    "andi":["001100","$rt","$rs","imm"],
    "addiu":["001001","$rt","$rs","imm"],
    "slti":["001010","$rt","$rs","imm"],
    "sltiu":["001011","$rt","$rs","imm"],
    "ori":["001101","$rt","$rs","imm"],
    "xori":["001110","$rt","$rs","imm"],

    "lw":["100011","$rt","imm","$rs"],
    "lwl":["100010","$rt","imm","$rs"],
    "lwr":["100110","$rt","imm","$rs"],
    "lh":["100001","$rt","imm","$rs"],
    "lui":["001111","$rt","imm"],
    "lbu":["100100","$rt","imm","$rs"],
    "lhu":["100101","$rt","imm","$rs"],
    "lb":["100000","$rt","imm","$rs"],
    "sb":["101000","$rt","imm","$rs"],
    "sh":["101001","$rt","imm","$rs"],
    "sw":["101011","$rt","imm","$rs"],
}

ri_list = ["bltz","bgez","bltzal","bgezal"]

r_list = ["add","addu","sub","subu","and","or","xor","nor","slt","sltu","sll","srl","sra","sllv","srlv",
    "srav","jalr","mult","multu","mfhi","mflo","mthi","mtlo","jr"]

j_list = ["j","jal"]

i_list = ["beq","bne","blez""bgtz","addi" ,"andi" , "addiu" , "slti" ,"sltiu" ,"ori" ,"xori" ,
"lw" ,"lwl" ,"lwr" ,"lh" ,"lui","lbu" ,"lhu" ,"lb" ,"sb" ,"sh" ,"sw"]


asm_dict = {}

r_type =['000000','sssss','ttttt','ddddd','mmmmm','ffffff']
ri_type = ['000001', 'sssss', 'RRRRR', 'CCCCCCCCCCCCCCCC']
i_type = ['EEEEEE', 'sssss', 'ttttt', 'CCCCCCCCCCCCCCCC']
j_type = ['EEEEEE','AAAAAAAAAAAAAAAAAAAAAAAAAA']

#reg = '$7'
#below converts reg in format $# to 5 character string
#reg = reg.replace('$','')
#reg = bin(int(reg)).replace('0b','').zfill(5)


def regnum_tob(reg):
    """turns register number in the form $# to 5 bit binary"""
    reg = reg.replace('$','')
    reg = bin(int(reg)).replace('0b','').zfill(5)
    return reg
    
def addr_tob(addr):
    if('-' in addr):
        b = bin(int(addr) & 0b1111111111111111).replace('0b','')
    else:
        b = bin((int(addr, 16))).replace('0b','').zfill(16)
    return b

def jaddr_tob(addr):
    b = bin((int(addr, 16))).replace('0b','').zfill(26)
    return b
    

    
def makeasm_dict():
    """creates a dictionary from assembly text files"""
    for x in range(len(a)):
        asm_dict[x] = str.split(a[x].replace('\n','').replace(',','').replace('(',' ').replace(')',' '))
        
def check_isa(line):
    """returns a boolean to see if the assembly instruction is in the list of instructions"""
    return asm_dict[line][0] in mips_dict.keys()
    
    
def rtype_out(line):
    """outputs rtype instruction in format"""
    output = r_type
    #r_type =['000000','sssss','ttttt','ddddd','shamt,''ffffff']
    output[1] = '00000' #s
    output[2] = '00000' #t
    output[3] = '00000' #d
    output[4] = '00000' #shift amount
    output[5] = '000000' #f
    output[5] = mips_dict[asm_dict[line][0]][0] #puts in function code
    for i in range(len(mips_dict[asm_dict[line][0]])-1):
        if mips_dict[asm_dict[line][0]][i+1] == '$rs':
            output[1] = regnum_tob(asm_dict[line][i+1])
        elif mips_dict[asm_dict[line][0]][i+1] == '$rt':
            output[2] = regnum_tob(asm_dict[line][i+1])
        elif mips_dict[asm_dict[line][0]][i+1] == '$rd':
            output[3] = regnum_tob(asm_dict[line][i+1])
        elif mips_dict[asm_dict[line][0]][i+1] == 'shamt':
            output[4] = regnum_tob(asm_dict[line][i+1])
    return output
    
def itype_out(line):
    """outputs itype instruction in format"""
    output = i_type
    #i_type = ['EEEEEE', 'sssss', 'ttttt', 'CCCCCCCCCCCCCCCC']
    output[1] = '00000' #s
    output[2] = '00000' #t
    output[3] = '0000000000000000' #imm
    output[0] = mips_dict[asm_dict[line][0]][0]#puts in opcode
    for i in range(len(mips_dict[asm_dict[line][0]])-1):
        if mips_dict[asm_dict[line][0]][i+1] == '$rs':
            #output
            output[1] = regnum_tob(asm_dict[line][i+1])
        elif mips_dict[asm_dict[line][0]][i+1] == '$rt':
            output[2] = regnum_tob(asm_dict[line][i+1])
        elif mips_dict[asm_dict[line][0]][i+1] == 'imm':
            output[3] = addr_tob(asm_dict[line][i+1])
    return output

def ritype_out(line):
    """outputs ritype instruction in format"""
    output = ri_type
    #ri_type = ['000001', 'sssss', 'RRRRR', 'CCCCCCCCCCCCCCCC']]
    output[0] = '000001' #opcode
    output[1] = '00000' #s
    output[3] = '0000000000000000' #imm
    output[2] = mips_dict[asm_dict[line][0]][0] #puts in opcode
    for i in range(len(mips_dict[asm_dict[line][0]])-1):
        if mips_dict[asm_dict[line][0]][i+1] == '$rs':
            #output
            output[1] = regnum_tob(asm_dict[line][i+1])
        elif mips_dict[asm_dict[line][0]][i+1] == 'imm':
            output[3] = addr_tob(asm_dict[line][i+1])
    return output
 
def jtype_out(line):
    """outputs ritype instruction in format"""
    output = j_type
    #j_type = ['EEEEEE','AAAAAAAAAAAAAAAAAAAAAAAAAA']
    output[0] = mips_dict[asm_dict[line][0]][0]
    output[1] = jaddr_tob(asm_dict[line][1])
    return output
    
    
def checktype(line):
    if asm_dict[line][0] in ri_list :
        return ritype_out(line)
    elif asm_dict[line][0] in i_list :
        return itype_out(line)
    elif asm_dict[line][0] in r_list:
        return rtype_out(line)
    elif asm_dict[line][0] in j_list:
        return jtype_out(line)
    
#checks to see if mips function is a key in dictionary
#b = (asm_dict[0][0] in mips_dict.keys())
makeasm_dict()
#print(check_isa(1))
#print(regnum_tob('$21'))
#print(addr_tob('0xffff'))

output_dict = {}
for i in range(len(asm_dict)-1):
    output_dict[i] = ''.join(checktype(i))

f = open('test0.mif','w')
"""print('')
print('WIDTH = 32;')
print('DEPTH = 256;')
print('')
print('ADDRESS_RADIX=HEX;')
print('DATA_RADIX=BIN;')
print('')
print('CONTENT BEGIN')
for i in range(len(output_dict)):
    print('   '+hex(int('0x00400000',16) + i) +'   :   '+ output_dict[i] + ';')
print('   [' + hex(int('0x00400000',16) + len(output_dict))+'..'+ hex(int('0x00400000',16) + 255) +']'+ '   :   '+ '00000000000000000000000000000000;')  

print('END;')
"""
f.write(''+ '\n')
f.write('WIDTH=32;'+ '\n')
f.write('DEPTH=256;'+ '\n')
f.write(''+ '\n')
f.write('ADDRESS_RADIX=HEX;'+ '\n')
#f.write('DATA_RADIX=BIN;'+ '\n')
f.write('DATA_RADIX=HEX;'+ '\n')
f.write(''+ '\n')
f.write('CONTENT BEGIN'+ '\n')
for i in range(len(output_dict)):
    #f.write('   '+ '0x'+ hex(int('0x00400000',16) + i).replace('0x','').zfill(8).upper() +'   :   '+ output_dict[i] + ';'+ '\n') #binary output
    f.write('   '+ '0x'+ hex(int('0x00400000',16) + i).replace('0x','').zfill(8).upper() +'   :   '+ 
            hex(int('0b'+ output_dict[i],2)).replace('0x','').upper().zfill(8) + ';'+ '\n') #to get hex output
    
f.write('   [' + '0x' + hex(int('0x00400000',16) + len(output_dict)).replace('0x','').zfill(8).upper()+'..'
             + hex(int('0x00400000',16) + 255) +']'+ '   :   '+ '00000000000000000000000000000000;'+ '\n')  

f.write('END;'+ '\n')

f.close()
    
#print(asm_dict[10])
#print(len(''.join(rtype_out(10))))
#print(mips_dict[asm_dict[line][0]][3])
#R type 000000 sssss ttttt ddddd SSSSS ffffff

#RI type 000001 sssss RRRRR CCCCCCCCCCCCCCCC

#I type EEEEEE sssss ttttt CCCCCCCCCCCCCCCC

#j type EEEEEE AAAAAAAAAAAAAAAAAAAAAAAAAA
