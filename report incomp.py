class data:
    global sub
    global marks 
    global i
    def subjects():
        i=int(input("Enter number of subjects : "));sub=[];marks=[]
        for j in range (0,1): 
            s=input(f"Enter Subject {j+1}")
            sub.append(s) 
            j+=1
    def marks():
        k=0
        for k in range (0,i):
            m=float(input(f"Enter marks for {sub[i+1]}"))
            marks.append(m)
            k+=1
    def access():
        l=0
        for l in range (0,i):
            d=(f"{sub[l]}                    {marks[l]}")
            return d
            l+=1 
class format:
    def formats(func):
        def wrap(a):
            print(a*16)
            print(" "*5,"REPORT") 
            print(a*16) 
            
            func()
            print(a*16) 
            print(" "*5," END ") 
            print(a*16) 
