def decorator(func):
    def wrapper(*args, **kwargs):
        print('Wrapper Upside')
        func(*args, **kwargs)
        print('Wrapper Downside')
    return wrapper

@decorator
def chocolate():
    print('chocolate')
    # print('wrapper')#add this
    #change the behaaviour of the function in middle of process 

@decorator
def cake(name):
    print('cake ' +name)


chocolate()
cake('apple')