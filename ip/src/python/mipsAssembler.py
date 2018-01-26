# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:21:11 2018

@author: Luis
"""

# bin(decimal) to convert decimal numbers to binary of the form 0b00000

mips_dict = {
  "r": ["rs", "rt", "rd", "function"],
  "ri": ["rs", "rt", "rd", "function"],
  "i": ["rs", "rt", "rd", "function"],
  "j": ["rs", "rt", "rd", "function"],
}

r_dict = {
        "and": "101010",
        "and": "101010",
        "and": "101010",
        "and": "101010",
        "and": "101010",
        }

i_dict = {
        "andi": "101010"}

ri_dict = {
            "help": "help"}

mips_dict["r"][0] = "37"
mips_dict["r"][1] = "5"
mips_dict["r"][2] = "3"
mips_dict["r"][3] = "1"

x = (''.join(mips_dict["r"]))

#print (bin(int(x)))

test = "lui $1, 0xffff"
test = test.replace(',','') #this strips commas

new = str.split(test)
mips_dict["swag"] = new
mips_dict["swag"][2] = bin(int(mips_dict["swag"][2],16))
mips_dict["swag"][2] = mips_dict["swag"][2].replace('0b','')



dict = {
        "add": "opcode" + "r1" + "r2" + "r3" +"s" +"f"}
        
        


