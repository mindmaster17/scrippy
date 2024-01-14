from pathlib import Path
import time
import urllib.request 
from PIL import Image 

banner_1 = """
                      __●__ ●
                      _ █___█
                      __ █__ █
                      __ ███____________█████ 　　　
                      _█▒░░█_________██▓▒▒▓██ ☆
                      █▒░●░░█___ ██▓▒██▓▒▒▓█　　 ★
                      █░█▒░░██_ ██▓▒██▓▒░▒▓█
                      _██▒░░██ ██▓▒░██▓▒░▒▓█ 　　　★
                      ____█▒░██ ██▓▒░░ ████▓█
                      ___█▒░██__██▓▓▒▒░░░██ 　 ★★
                      ____█▒░██___████████████
                      ______██████████████████.•°*”˜҈.•°*”˜҈.                                  
                                          

"""
# Displays an Ascii Text Banner
print(banner_1)
path_1 = Path.cwd()
print("Running File: ", path_1)
seconds = time.time()
local_time = time.ctime(seconds)
print("Local Time:", local_time)

# Input fron the user
file_name = "img_"
string_1 = input("String: ")
text_1 = input("Text: ")
pages = int(input("No. Pages: "))

file_1 = open("/Users/gthea/OneDrive/Documents/file_1.txt", "w")

# Generating different links for download
for i in range(10):
    file_name_1 = file_name + str(i) + ".png"
    text_2 = text_1 + str(i)
    position_1 = string_1.find(text_1)
    replaced_1 = string_1.replace(text_1,text_2) 
    print(replaced_1)
    file_1.write(str(replaced_1 + "\n"))
    urllib.request.urlretrieve(replaced_1, file_name_1 ) 

# Opening the first image Downloaded
img = Image.open('img_1.jpg') 
img.show()
    
file_1.close()
