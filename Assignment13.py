
import threading
import time

# Task 1: Print numbers
def task1():
    for i in range(1, 6):
        print("Thread 1: Number =", i)
        time.sleep(1)

# Task 2: Print squares
def task2():
    for i in range(1, 6):
        print("Thread 2: Square =", i * i)
        time.sleep(1)

# Task 3: Print cubes
def task3():
    for i in range(1, 6):
        print("Thread 3: Cube =", i * i * i)
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for threads to complete
t1.join()
t2.join()
t3.join()

print("\nAll threads completed successfully!")
