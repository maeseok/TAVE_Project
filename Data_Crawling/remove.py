import os 
path="./"
List=[]
data=[]
with open("./여자배우.txt","r",encoding="UTF8") as f:
    while True:
        line = f.readlines()
        for i in line:
            List.append(i.strip())
        break

for i in List:
    start=300
    for j in range(500):
        data=i+"/google_0"+str(start)+".jpg"
        try:
            print(path+data)
            os.remove(path+data)
        except:
            pass
        start+=1