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
    n = len(p)  # liczba zadań

    # Obliczenie maksymalnej liczby maszyn dla zadania
    m = max(max(mu[i]) for i in range(n))

    # Inicjalizacja tablicy czasy zakończenia
    C = [[0] * len(p[i]) for i in range(n)]
    C_machine = [[(0, 0)] * len(p[i]) for i in range(n)]  # Tablica pomocnicza z elementami (C, numer maszyny)

    # Obliczanie czasów zakończenia dla pierwszego zadania
    C[0][0] = p[0][0]
    C_machine[0][0] = (C[0][0], mu[0][0])
    for j in range(1, len(p[0])):
        C[0][j] = C[0][j-1] + p[0][j]
        C_machine[0][j] = (C[0][j], mu[0][j])

    # Obliczanie czasów zakończenia dla pozostałych zadań
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
            


    # Obliczanie wartości Cmax
    Cmax = max(max(row) for row in C)

    return C, C_machine, Cmax


rng = RandomNumberGenerator(2451)

m = 4
j = 5

# o = []
# pkj = []
# muk = []
# pkj_tmp = []
# muk_tmp = []

# for i in range(j):
#     pomoc_o = rng.nextInt(1, math.floor(m * 1.2))
#     o.append(pomoc_o)
#     for k in range(o[i]):
#         pomoc = rng.nextInt(1, 29)
#         pkj_tmp.append(pomoc)
  
#     pkj.append(pkj_tmp.copy())
#     pkj_tmp.clear()


# for i in range(j):
#     for k in range(o[i]):
#         pomoc = rng.nextInt(1, m)
#         muk_tmp.append(pomoc)
#     muk.append(muk_tmp.copy())
#     muk_tmp.clear()


# print(pkj)
# print(muk)

# Przykładowe dane
p = [[12, 29], [24, 20], [27, 28, 28], [3, 21, 22, 1, 9], [26, 22, 25, 8, 9]]
mu = [[3, 2], [4, 3], [2, 4, 3], [3, 1, 1, 2, 2], [1, 3, 3, 4, 1]]

seed = 2451

C, C_machine, Cmax = calculate_Cmax(p, mu)

total_values = count_values_2d(p)

pi = list(range(1,18))

print("seed: ", seed)
print("size: ", len(p), "x", max(max(mu[i]) for i in range(len(p))))
print(p)
print(mu)
print("Permutacja naturalna")
print(pi)
print(C)
print("Cmax:", Cmax)

# print("C_machine", C_machine)