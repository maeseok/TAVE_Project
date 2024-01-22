import os
f = open("./여자배우.txt", 'r',encoding="utf-8")
lines = f.readlines()
data=[]
List=[]
for i in lines:
    data.append(i.strip())
print(len(data))
for i in data:
    if not i=="":
        if os.path.isdir(f"./{i}"):
            List.append(i)
List.sort()
print(len(List))

'''for i in range(len(List)):
    if os.path.isdir(f"./{i}"):
        os.rename(f"./{i}",f"./{List[i]}_수정본")'''
