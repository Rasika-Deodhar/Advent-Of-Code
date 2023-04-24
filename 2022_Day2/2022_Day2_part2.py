f = open("input.txt", "r")
input = f.readlines()

verdict = {
    'X' : 0, #lose
    'Y' : 3, #draw
    'Z' : 6  #won
}
player1 = {
    'A' : 1, #rock
    'B' : 2, #paper
    'C' : 3  #scissor
}

score = 0

for line in input:
    if line[2] == 'X':
        if line[0] == 'A':
            score += verdict['X'] + 3
        elif line[0] == 'B':
            score += verdict['X'] + 1
        elif line[0] == 'C':
            score += verdict['X'] + 2
    elif line[2] == 'Z':
        if line[0] == 'A':
            score += verdict['Z'] + 2
        elif line[0] == 'B':
            score += verdict['Z'] + 3
        elif line[0] == 'C':
            score += verdict['Z'] + 1
    elif line[2] == 'Y':
        score += verdict['Y'] + player1[line[0]]

print('Score = ', score)
