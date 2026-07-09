#Using word.split() for variable input 
#required & keyword argument 
def req(b,a):
    print(f"name={a}\nRoll no.={b}")
#default argument 
def de(clas=2):
    print(f"class=SY{clas}") 
#variable args
def va(*s):
    print(f"Subjects={s}")
#################
n=input("Enter name : ")
r=int(input("Enter Roll no. : ")) 
wl=input("Enter subjects and seperate by commas : ")
sub=wl.split(",")  
clas=int(input("Enter classs :"))
req(a=n,b=r)
de(clas)
va(sub) 
