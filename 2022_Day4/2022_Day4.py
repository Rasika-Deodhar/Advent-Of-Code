f = open("input.txt", "r")
input = f.readlines()

overlap=0

for line in input:
    first = line.split(',')[0]
    second = line.split(',')[1]

    first_0 = first.split('-')[0]
    first_1 = first.split('-')[1]    
    
    second_0 = second.split('-')[0]
    second_1 = second.split('-')[1]

    
    print(first_0, first_1, second_0, second_1)

    if int(first_0) <= int(second_0) and int(second_1) <= int(first_1):
            overlap += 1
            print('added')
    elif int(second_0)  <= int(first_0) and int(second_1) >= int(first_1):
            overlap +=1
            print('added')
    #part 2
    elif int(first_0) <= int(second_0) and (int(second_0) <= int(first_1) and int(first_1) <= int(second_1)):
            overlap += 1
            print('added')
    elif int(second_0)  <= int(first_0) and (int(second_1) >= int(first_0) and int(second_1) <= int(first_1) ):
            overlap +=1
            print('added')

print('overlap =', overlap)
