import sys as sys
from time import sleep
def fun(t,s):
    
    a=t/len(s)
    sys.stdout.write(s)
    for i in range(len(s)):
        sleep(a)
        sys.stdout.write('\b \b')



fun(10,"ayushayushayush")


# from threading import Thread
# t=[]
# for i in range(10):
#     t.append(Thread(target=fun,args=(10,"ayush")))

# for i in t:
#     i.start()