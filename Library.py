#Assignment 1
class Library:    
    global books
    global iss
    global detail
    books=["harry potter","disney","Avengers"];iss=''
    def add(b):
        books.append(b) 
        print(f"{b} added to Library")
        print("New booklist : \n{books}") 
    def issue(a):
        if a in books:
            books.remove(a)
            iss.append(a)
            return True
        else:
            print("No such books exists")
            return False 
    def ret(k):
        if k in iss:
            iss.remove(k)
            books.append(k) 
            print(f"{k} book Returned!! ")
        else:
            print("No such book issued")
    def details(n,c,id,nb):
        d={"Name" : n,
           "book" : nb,
           "Class" : c,
           "ID no." :id}
        detail.append(d)
        return d
i=4
while(i>0):       
    i=int(input(f"Welcome to Library.\nFollowing Books Available:\n{books}\nEnter 1 for returning book \nEnter 2 for book issue\nEnter 3 to add book in Library\nEnter 0 to exit.\n"))
    if i==1:
        r=input("Enter name of book to return : ")
        Library.ret(r)
    elif i==2:
        ps=input("Enter name of book to issue : ") 
        if Library.issue(ps):
            name=input("Enter name : ")
            clas=input("Enter class : ")
            idd=input("Enter ID Number : ") 
            print("Book issued and Following details recorded :")
            print("\n",Library.details(name,clas,idd,ps)) 
    elif i==3:
        ko=input("Enter the name of book to add : ") 
        Library.add(ko)
    elif i!=0:
        print("Invalid choice") 
