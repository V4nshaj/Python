def decorator(func):
    def wrapper():
        print('Wrapper Upside')
        func()
        print('Wrapper Downside')
    return wrapper

@decorator
def chocolate():
    print('chocolate')
    # print('wrapper')#add this
    #change the behaaviour of the function in middle of process 

@decorator
def cake():
    print('cake')


chocolate()
cake()