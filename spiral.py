N = -1
matrix = [[0 for i in range(N)] for j in range(N)]
counter = 1
a, b = 0, 0
num = N - 1
pseudo_zero = 0
while counter <= N*N:

    matrix[a][b] = counter
    counter += 1

    if b < num - pseudo_zero and a == pseudo_zero: # right
        b += 1
    elif b == num - pseudo_zero and a < num - pseudo_zero: # down
        a += 1
    elif b != pseudo_zero and a == num - pseudo_zero: # left
        b -= 1
    else: # up
        a -= 1
        if a - 1 == pseudo_zero:
            pseudo_zero += 1
for line in matrix:
    print(*line)