while True:
    with open('names.txt', 'a') as file:
        file.write(input("Write names: ")+'\n')
        choice = input('Wana write more names? (y/n)')
        if choice == 'n':
            break