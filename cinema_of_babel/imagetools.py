from PIL import Image
import numpy as np
import mapping
import time

 # Sets infinite size array
np.set_printoptions(threshold=np.inf)


def charToNum(char):
    if char in mapping.mapping_dict:
        return mapping.mapping_dict[char]
    else:
        return 999 

def numToChar(num):
    if num in mapping.inv_mapping_dict:
       return mapping.inv_mapping_dict[num]
    else:
        print(num)
        return "™" # Unmapped character space 


def textToArray(text, width, height):
    full_array_size = 3 * width * height   
    
    # Reading textfile and truancing/adding extra characters
    with open("moviescript.txt", 'r') as f:
        text = f.read() 
        text_length = len(text)
        
        # Case for additional characters in textfile 
        if (text_length > full_array_size):
            text = text[:-(text_length - full_array_size)] 
        
        # Case for too few characters in textfile
        elif (text_length < full_array_size):
            for i in range(full_array_size - text_length):
                text += "!"
        else:
            pass
    
    # Converts text from textfile into numpy array 
    image_list = list(text)
    image_array = np.array(image_list)
    
    # Resizing Array to image dimensions
    image_array = np.reshape(image_array, (height, width, 3))
    
    # Applying charToNum() to array
    image_array = np.stack(np.vectorize(charToNum)(image_array), axis=0)
    
    # Converting array and saving image
    return image_array 

def arrayToText(imgarr):   
    # Converting each number and joining them together to create string
    imgarr = np.ravel(imgarr)
    moviescript = ""
    for num in imgarr:
        moviescript += str(numToChar(num))
        
    # Writing string to textfile
    with open("moviescript.txt", 'w') as f:
        f.write(moviescript)

def imageToArray(image):
    img = Image.open(image)
    img = img.convert("RGB")
    imgarr = np.array(img)
    return imgarr 


def arrayToImage(array): 
    array = array.astype(np.uint8)
    im_new = Image.fromarray(array)
    im_new = im_new.save("../images/output.jpg") # The final image produced from the textfile


def getImageDimensions(image):
    img = Image.open(image)
    width = img.width
    height = img.height

    return width, height

