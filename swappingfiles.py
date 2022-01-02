def swappingfiles():
    file1 = input('Enter file name here : ')
    file2 = input('Enter file name here : ')

    with open(file1, 'r') as A:
        dataA = A.read()
    
    with open(file2, 'r') as B:
        dataB = B.read()
    
    with open(file1, 'w') as A:
        A.write(dataB)
    
    with open(file2, 'w') as B:
        B.write(dataA)

swappingfiles()