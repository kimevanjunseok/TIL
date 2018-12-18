import os
os.chdir(r"C:\Users\student\Desktop\TIL\dummy") #윈도우면 r붙임
for filename in os.listdir("."): # .은 현재위치
    os.rename(filename, filename.replace("SAMSUNG", "SSAFY"))