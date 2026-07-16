class Library:    
    global books
    global iss
    global detail
    books=["harry potter","disney","Avengers"]
    def add(b):
        books.append(b) 
        print(f"{b} Returned!! ")
    def issue(a):
        if a in books:
            books.remove(a)
            iss.append(a)
            return True
        else:
            print("No such books exists")
            return False 
    def ret(k):
        iss.remove(k)
        books.append(k) 
    def details(n,c,id,nb):
        d={"Name" : n,
           "book" : nb,
           "Class" : c,
           "ID no." :id}
        detail.append(d)
i=4
while(i>0):       
    i=int(input(f"Welcome to Library.\nFollowing Books Available:\n{books}\nPress 1 for returning book and 2 for book issue\npress 0 to exit.\n"))
    if i==1:
        r=input("Enter name of book to return : ")
        Library.add(r)
    elif i==2:
        iis=input("Enter name of book to issue : ") 
        if Library.issue(iis):
            name=input("Enter name : ")
            clas=input("Enter class : ")
            idd=input("Enter ID Number : ")
            Library.details(name,clas,idd,iis) 
            print("Book issued and Following details recorded :");print("\n",detail) 
    elif i!=0:
        print("Invalid choice") 
class Library:    
    global books
    global iss
    global detail
    books=["harry potter","disney","Avengers"]
    def add(b):
        books.append(b) 
        print(f"{b} Returned!! ")
    def issue(a):
        if a in books:
            books.remove(a)
            iss.append(a)
            return True
        else:
            print("No such books exists")
            return False 
    def ret(k):
        iss.remove(k)
        books.append(k) 
    def details(n,c,id,nb):
        d={"Name" : n,
           "book" : nb,
           "Class" : c,
           "ID no." :id}
        detail.append(d)
i=4
while(i>0):       
    i=int(input(f"Welcome to Library.\nFollowing Books Available:\n{books}\nPress 1 for returning book and 2 for book issue\npress 0 to exit.\n"))
    if i==1:
        r=input("Enter name of book to return : ")
        Library.add(r)
    elif i==2:
        iis=input("Enter name of book to issue : ") 
        if Library.issue(iis):
            name=input("Enter name : ")
            clas=input("Enter class : ")
            idd=input("Enter ID Number : ")
            Library.details(name,clas,idd,iis) 
            print("Book issued and Following details recorded :");print("\n",detail) 
    elif i!=0:
        print("Invalid choice") 
