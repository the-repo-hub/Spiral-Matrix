y = int(input('height: '))
x = int(input('width: '))
matrix = [[0 for i in range(x)] for j in range(y)]
counter = 1
a, b = 0, 0
iteration = 0
num_x, num_y = x - 1, y - 1
while counter <= x*y:

    matrix[a][b] = counter
    counter += 1

    if a == iteration and b < num_x - iteration:
        b += 1
    elif b == num_x - iteration and a < num_y - iteration:
        a += 1
    elif a == num_y - iteration and b != iteration:
        b -= 1
    else:
        a -= 1
        if a - 1 == iteration:
            iteration += 1
for line in matrix:
    print(*line)
