string=input("please enter the name:")
string1=" "
for i in range(len(string)):
    if string[i]>="a" and string[i]<="z":
        string1=string1+chr((ord(string[i])-32))
    elif string[i]>="A" and string[i]<="Z":
        string1=string1+chr((ord(string[i])+32))
    else:
        string1=string1+string[i]
print("orginal string= ",string)
print("the string after toggling case= ",string1)
