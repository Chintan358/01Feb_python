# f = open("myfile.txt",'w')
# f.write("Hello python")
# f.truncate(4)
# f.close()

# f = open("myfile.txt",'r')
# text = f.read()
# print(text)

# f = open("myfile.txt",'a')
# f.write("Hello python")
# f.close()

# with open("myfile.txt") as f:
#     f.seek(5)
#     print(f.tell())
#     text=f.read()
#     print(text)

with open("myfile.txt") as f :
    while True:       
        text = f.readline()
        if not text:
            break   
        a = text.split(",")[0]
        b = text.split(",")[1]
        c = text.split(",")[2]
        print(f"{a} - {b} - {c}")

import os

# os.makedirs("NEWFOLDER")
# os.rmdir("NEWFOLDER")





   



    
   

