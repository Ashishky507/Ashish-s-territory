print("------:Welcome to the Love Calcualtor:-----")

name1=input("what is your name : ")
name2=input("what's your gf name: ")
count=0
temp=0
name=name1+name2



                                               
for i in range(len(name)):                     #we can do this program using count() function, which can count num of letters in string    
    if name[i]=="T":
        count+=1
    elif name[i]=="R":
        count+=1
    elif name[i]=="U":
        count+=1
    elif name[i]=="E":
        count+=1
    else:
        count+=0

for i in range(len(name)):
    if name[i]=="L":
        temp+=1
    elif name[i]=="O":
        temp+=1
    elif name[i]=="V":
        temp+=1
    elif name[i]=="E":
        temp+=1
    else:
        temp+=0






print(f"your love percentage is {count}"+f"{temp}%")





    
    