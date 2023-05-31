import math
from RandomNumberGenerator import RandomNumberGenerator

def find_index_2d(array, current_task_index, value):
    indexes = []

    for i in range(current_task_index):
        for j in range(len(array[i])):
            if array[i][j] == value:
                indexes.append((i, j))

    if not indexes:
        return None
    else:
        return indexes

def count_values_2d(array):
    count = 0

    for row in array:
        count += len(row)

    return count


def calculate_Cmax(p, mu):
    n = len(p) 

    m = max(max(mu[i]) for i in range(n))

    C = [[0] * len(p[i]) for i in range(n)]
    C_machine = [[(0, 0)] * len(p[i]) for i in range(n)] 

    C[0][0] = p[0][0]
    C_machine[0][0] = (C[0][0], mu[0][0])
    for j in range(1, len(p[0])):
        C[0][j] = C[0][j-1] + p[0][j]
        C_machine[0][j] = (C[0][j], mu[0][j])

    for i in range(1, n):
        for j in range(len(p[i])):
            if j == 0:
                values = find_index_2d(mu, i, mu[i][j])
                if values is not None:
                    row, col = values[-1]
                    C[i][j] = C[row][col] + p[i][j] 
                else:    
                    C[i][j] = p[i][j]

                C_machine[i][j] = (C[i][j], mu[i][j])

            else:
                C[i][j] = C[i][j-1] + p[i][j]
                C_machine[i][j] = (C[i][j], mu[i][j])
            
    Cmax = max(max(row) for row in C)

    return C, C_machine, Cmax


rng = RandomNumberGenerator(2451)

m = 4
j = 5

o = []
pkj = []
muk = []
pkj_tmp = []
muk_tmp = []

for i in range(j):
    pomoc_o = rng.nextInt(1, math.floor(m * 1.2)) + 1
    o.append(pomoc_o)
    for k in range(o[i]):
        pomoc = rng.nextInt(1, 29)
        pkj_tmp.append(pomoc)
  
    pkj.append(pkj_tmp.copy())
    pkj_tmp.clear()


for i in range(j):
    for k in range(o[i]):
        pomoc = rng.nextInt(1, m)
        muk_tmp.append(pomoc)
    muk.append(muk_tmp.copy())
    muk_tmp.clear()

seed = 2451

C, C_machine, Cmax = calculate_Cmax(pkj, muk)

total_values = count_values_2d(pkj)

pi = list(range(1,18))

print("seed: ", seed)
print("size: ", len(pkj), "x", max(max(muk[i]) for i in range(len(pkj))))
print(pkj)
print(muk)
print("Permutacja naturalna")
print(pi)
print(C)
print("Cmax:", Cmax)
