f = open("input.txt", "r")
input = f.readlines()

player = {
    'X' : 1, #rock
    'Y' : 2, #paper
    'Z' : 3  #scissor
}
player1 = {
    'A' : 1, #rock
    'B' : 2, #paper
    'C' : 3  #scissor
}

score = 0

for line in input:
    if player1[line[0]] == player[line[2]]:
        score = score +  player[line[2]] + 3
    elif line[0] == 'A' and line[2] == 'Y':
        score = score +  player['Y'] + 6
    elif line[0] == 'A' and line[2] == 'Z':
        score = score +  player['Z'] + 0
    elif line[0] == 'B' and line[2] == 'X':
        score = score +  player['X'] + 0
    elif line[0] == 'B' and line[2] == 'Z':
        score = score +  player['Z'] + 6
    elif line[0] == 'C' and line[2] == 'X':
        score = score +  player['X'] + 6
    elif line[0] == 'C' and line[2] == 'Y':
        score = score +  player['Y'] + 0


print('Score = ', score)
    