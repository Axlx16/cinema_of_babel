# Process for image #
# Image => Array => Padded Number =>  Apply encrypt FPE to number => Convert number to text

# Process for text #
# Text => Number => Format Number => Apply decrpty FPE to number =>  Array => Image #

import numpy as np
import imagetools
import math
from ubiq_security_fpe import ff1

def encryptFpe(num_arr):
    # Padding each number in numpy array to ensure consitent size 
    combined_num = [] 
    for num in np.nditer(num_arr, flags=['refs_ok']):
        num_str = str(num)
        if (len(num_str) == 1): 
            combined_num.append('00' + num_str)
             
        elif (len(num_str) == 2):
            combined_num.append('0' + num_str)

        else:
            combined_num.append(num_str)
    
    # Converting Padded Array to integer
    combined_num = ''.join(combined_num)

    ctx = ff1.Context(bytes([0]*16), bytes([0]*7), 0, 7, 10)
    ct = ctx.Encrypt(combined_num, bytes([0]*7))
    return ct

def decryptFpe(num, width, height):

    ctx = ff1.Context(bytes([0]*16), bytes([0]*7), 0, 7, 10)
    ct = ctx.Decrypt(num, bytes([0]*7)) 
    
    chunks = [int(ct[i:i+3]) for i in range(0, len(ct), 3)]
    chunks_arr = np.array(chunks)
    chunks_arr.resize(width, height, 3)
    return chunks_arr 


