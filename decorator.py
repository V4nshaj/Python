def chocolate():
    print('chocolate')
    # print('wrapper')#add this
    #change the behaaviour of the function in middle of process 

def decorator(func):
    def wrapper():
        print('Wrapper Upside')
        func()
        print('Wrapper Downside')
    return wrapper

chocolate = decorator(chocolate)#updates the function behaviour and stores in func choco
chocolate()