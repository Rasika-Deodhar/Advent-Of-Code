f = open("input.txt", "r")
input = f.readlines()

row_wise = {}

# reading input
# i=0
# for line in input:
#     if line[0]!=' ':
#         arr = line.split(' ')
#         print(arr, len(arr))
#         last_index = 0
#         index_val = 0
#         for i in range(len(arr)):
#             if arr[i] != '':
#                 index_val = i - last_index - 1
#                 row_wise[index_val].append(arr[i])
#     else:
#         break

stack1 = ['Q', 'S', 'W', 'C', 'Z', 'V', 'F', 'T']
stack2 = ['Q', 'R', 'B']
stack3 = ['B', 'Z', 'T', 'Q', 'P', 'M', 'S']
stack4 = ['D', 'V', 'F', 'R', 'Q', 'H']
stack5 = ['J', 'G', 'L', 'D', 'B', 'S', 'T', 'P']
stack6 = ['W', 'R', 'T', 'Z']
stack7 = ['H', 'Q', 'M', 'N', 'S', 'F', 'R', 'J']
stack8 = ['R', 'N', 'F', 'H', 'W']
stack9 = ['J', 'Z', 'T', 'Q', 'P', 'R', 'B']

stack_arrays = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

for line in input:
    if line[0] == 'm':
        move = int(line.split(' ')[1])
        _from = int(line.split(' ')[3])
        to = int(line.split(' ')[5])
        print('...', move, _from, to)
        i=0
        temp=[]
        while i < move:
            temp.append(stack_arrays[_from-1].pop())
            i+=1
        for t in temp:
            stack_arrays[to-1].append(t)
        print('-----------')

print('stack arrays=', [i[-1] for i in stack_arrays])

