import threading

def function_1():
    raise Exception("manually raised Exception")
    print("function 1 executed")

def function_2():
    thread = threading.Thread(target=function_1)
    thread.start()
    thread.join()
    
    print("function 2 executed")
