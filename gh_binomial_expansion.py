from math import comb
import re

# Idea / Kata from codewars. Had good fun coming up with my solution

#Examples:
#expand("(x+1)^2")      # returns "x^2+2x+1"
#expand("(p-1)^3")      # returns "p^3-3p^2+3p-1"
#expand("(2f+4)^6")     # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
#expand("(-2a-4)^0")    # returns "1"
#expand("(-12t+43)^2")  # returns "144t^2-1032t+1849"
#expand("(r+0)^203")    # returns "r^203"
#expand("(-x-1)^2")     # returns "x^2+2x+1"

# (a+b)^n = (n-choose-0)a^n + (n-choose-1)a^n-1*b^1 + (n-choose-2)a^n-2*b^2
# ......... + (n-choose-n-1)a^1b^n-1 + (n-choose-n)b^n

# My thought steps:
#Step 1: From the input, extract A, B and N
    # Write a function that inputs the string and returns a list with a, b and n.
    # a is a list within a list with an integer at index 0 and the letter at index 1.
    # Stores integers as positive or negative numbers.

#Step 2: Create a function that calculates all the parts of the new string
    #Counter from n to zero and from 0 to n
    #Inputs the list with a, b and c, returns a list with all the parts, every list consists of a list with ['integer', 'letter', 'power']

#Step 3: Create a function that parses the list coming out of the calculater function to a string
    #inputs a list, outputs a string
    # Example
    # [[64, 'f', 6], [768, 'f', 5], [3840, 'f', 4], [10240, 'f', 3], [15360, 'f', 2], [12288, 'f', 1], [4096, '', 1]]

#Step 4: Combine all of the above in one function

def expand(expr):
    return parse_string_from_list(calculate(extract(expr)))

def parse_string_from_list(array):
    opstring = ""
    for part in array:
        tempstr = ""
        if part[0] > 0:
            tempstr += "+"
        if part[0] == 1 and part[1] != "":
            tempstr += part[1]
        elif part[0] == -1 and part[1] != "":
            tempstr += "-"+part[1]
        else:
            tempstr += str(part[0]) + part[1]
        if part[2] != 1:
            tempstr += "^"+str(part[2])
        if part[0] != 0:
            opstring += tempstr
    
    if opstring[0] == "+":
        opstring = opstring[1:]

    return opstring



def calculate(array):
    an = array[0][0]
    al = array[0][1]
    b = array[1]
    n = array[2]

    bcount = 0
    oplist = []
    while bcount <= n:
        choose = comb(n, bcount)
        current_int = choose * (an**(n-bcount))*(b**bcount)
        if n-bcount == 0:
            current_letter = ''
            current_power = 1
        else:
            current_letter = al
            current_power = n-bcount
        
        oplist.append([current_int, current_letter, current_power])
        bcount += 1
    
    return oplist



def extract(string):
    patterna = r"[-]?[\d]*[a-zA-Z]"
    patternb = r"[+-][\d]+\)"
    patternn = r"\)\^[\d]+"

    proga = re.compile(patterna)
    progb = re.compile(patternb)
    progn = re.compile(patternn)

    complete_a = proga.findall(string)[0]
    complete_b = int(progb.findall(string)[0][:-1])
    complete_n = int(progn.findall(string)[0][2:])

    pattern_ca1 = r"[-]?[\d]*"
    pattern_ca2 = r"[a-zA-Z]"

    prog_a1 = re.compile(pattern_ca1)
    prog_a2 = re.compile(pattern_ca2)

    sep_a1 = prog_a1.findall(complete_a)[0]
    sep_a2 = prog_a2.findall(complete_a)[0]

    if sep_a1 == '-':
        sep_a1 = -1
    elif sep_a1 == '':
        sep_a1 = 1
    else:
        sep_a1 = int(sep_a1)



    return [[sep_a1, sep_a2], complete_b, complete_n]
