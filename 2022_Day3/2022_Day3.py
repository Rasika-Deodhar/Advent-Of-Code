f = open("input.txt", "r")
input = f.readlines()


# thanks to chat-gpt
letter_to_number = {chr(i): i - 96 for i in range(97, 123)}
letter_to_number.update({chr(i): i - 38 for i in range(65, 91)})

res = 0

for line in input:
    length = len(line)
    half = int(length/2)
    compartment1 = line[0:half]
    compartment2 = line[half : length]
    matches = []
    print(line + '----' + compartment1 + '---' + compartment2)
    for i in compartment1:
        if i in compartment2:
            matches.append({'letter': i, 'score': letter_to_number[i]})
            compartment2 = compartment2.replace(i, '')
    res += sum([m['score'] for m in matches])

print('sum of matches = ', res)
