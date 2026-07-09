#variable arguments using loop
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
sub=[]
i=int(input("Enter number of Subjects : "))
for j in range (0,i):
    s=input(f"Enter Subject number {j+1}")
    sub.append(s)
clas=int(input("Enter classs :"))
req(a=n,b=r)
de(clas)
va(sub) 
