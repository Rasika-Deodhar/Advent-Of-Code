f = open("input.txt", "r")
input = f.readlines()

list1=[]
max_val = 0
max_val2 = 0
max_val3 = 0
all_results = []

for line in input:
    if line != '\n':
        list1.append(int(line))
        print(line)
    else:
        all_results.append(sum(list1))
        list1=[]

all_results.sort(reverse=True)
print('Max val:', all_results[0], all_results[1], all_results[2])
print('Max val sum:', all_results[0] + all_results[1] + all_results[2])
f.close()

# print (list1)


