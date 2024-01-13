from pathlib import Path
import time

banner_1 = """
                      __●__ ●
                      __ █__ █_
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
string_1 = input("String: ")
text_1 = input("Text: ")
file_1 = open("/Users/gthea/OneDrive/Documents/file_1.txt", "w")

# Generating different links
for i in range(10):
    text_2 = text_1 + str(i)
    position_1 = string_1.find(text_1)
    replaced_1 = string_1.replace(text_1,text_2) 
    print(replaced_1)
    file_1.write(str(replaced_1 + "\n"))
    
file_1.close()
