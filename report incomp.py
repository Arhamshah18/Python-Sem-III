class data:    
    def subjects(i):
        sub=[]
        for j in range (0,i): 
            s=input(f"Enter Subject {j+1} : ")
            sub.append(s)
            j+=1
        return sub 
    def mk(i,sb):
        k=0;marks=[]
        for k in range (0,i):
            m=float(input(f"Enter marks for {sb[k]} : "))
            marks.append(m)
            k+=1
        return marks 
    def access(i,su,mark):
        l=0;av=0.0;sm=0
        for l in range (0,i):
            val=(27-len(str(su[l])))
            sp=" "*val
            print(f"\n{su[l]}{sp}{mark[l]}")
            l+=1
            for p in range (0,i):
                sm+=mark[p]
                p+=1
            av=sm/len(p)
            print(f"Average                    {av}")
u=int(input("Enter Number of Subjects : "))
s=data.subjects(u)
m=data.mk(u,s) 
def formats(a):
    def wrap(func):
        def inner():
            print(a*32)
            print(" "*5,"REPORT") 
            print(a*32) 
                
            func()

            print(a*32) 
            print(" "*5," END ") 
            print(a*32) 
        return inner
    return wrap 
v=input("Enter character for result border : ")
@formats(a=v)
def out():
    print("\nRESULT : ")
    print("SUBJECT                    MARKS\n\n")
    data.access(u,s,m)
    print("\n\n") 
out()
