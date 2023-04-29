# f = open("input.txt", "r")
# input = f.readlines()

# from itertools import islice
# with open("input.txt", 'r') as infile:
#     lines_gen = islice(infile, 3, 6)
#     for lines in lines_gen:
#         print('lines', lines)



# thanks to chat-gpt
letter_to_number = {chr(i): i - 96 for i in range(97, 123)}
letter_to_number.update({chr(i): i - 38 for i in range(65, 91)})

res = 0
matches = []

# thanks to chat-gpt
with open('input.txt', 'r') as file:
    while True:
        lines = [file.readline().strip() for _ in range(3)]
        if not any(lines):
            break  # Reached EOF
        print(lines)
        matches=[]
        for i in lines[0]:
            if i in lines[1] and i in lines[2]:
                lines[1] = lines[1].replace(i, "")
                lines[2] = lines[2].replace(i, "")
                matches.append({'match': i, 'score': letter_to_number[i]})
            print('match = ', matches)
        res += sum([m['score'] for m in matches])

print('res = ', res)


