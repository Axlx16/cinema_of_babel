import imagetools
import fpe
import numpy as np

def userImage(image, width, height):
    myarray = imagetools.imageToArray(image)
    encrypt_int = fpe.encryptFpe(myarray)
    
    chunks = [int(encrypt_int[i:i+3]) for i in range(0, len(encrypt_int), 3)]
    chunks_arr = np.array(chunks)
    
    chunks_arr.resize(width, height, 3) 
    imagetools.arrayToText(chunks_arr)
        

# userText converts text passed by the user into the image
def userText(text, width, height):
    # Conver text to array
    num_array = imagetools.textToArray(text, width, height)
    
    combined_num = [] 
    
    
    for num in np.nditer(num_array, flags=['refs_ok']):
        num_str = str(num)
        if (len(num_str) == 1): 
            combined_num.append('00' + num_str)
             
        elif (len(num_str) == 2):
            combined_num.append('0' + num_str)

        else:
            combined_num.append(num_str)
    
    num = ''.join(combined_num)
    
    decrypt_arr = fpe.decryptFpe(num, width, height)


    imagetools.arrayToImage(decrypt_arr)


image_loc = "../images/144-leaves.jpg"

width, height = imagetools.getImageDimensions(image_loc)


userImage(image_loc, width, height)

with open("moviescript.txt", 'r') as f:
   userText(f, width, height)