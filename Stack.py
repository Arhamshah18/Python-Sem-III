global stack
stack=[]
class s:
    def push(a):
        stack.append(a)
    def pop():
        stack.remove[len(stack)-1]
    def peek():
        return stack[len(stack)-1]
    def size():
        return len(stack)
i=5
while i>0:
    i=int(input("Enter choice\n1 to push\n2 to pop\n3 to peek\n4 to check size\n0 to exit\n"))
    if i==1:
        k=input("Enter element to add : ")
        s.push(k)
        print("PUSH operation successfull")
    elif i==2:
        s.remove()
        print("POP operation successfull")
    elif i==3:
        print(f"Top element ={s.peek()}")
    elif i==4:
        print(f"size of stack={s.size()}")
    elif i!=0:
        print("Invalid Choice")
    
