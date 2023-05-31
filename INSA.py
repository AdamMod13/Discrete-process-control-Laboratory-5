from RandomNumberGenerator import RandomNumberGenerator
import math

class Task:
    def __init__(self):
        self.p = []  # czas wykonywania
        self.u = []  # rodzaj maszyny
        self.number = 0  # numer operacji


def Cmax(schedule):
    m = 0
    for i in range(len(schedule)):
        data = schedule[i]
        maxMachine = max(data.u)
        m = max(m, maxMachine)

    mEndTime = [0] * m

    for i in range(len(schedule)):
        data = schedule[i]
        for j in range(len(data.p)):
            machine = data.u[j] - 1
            processingTime = data.p[j]

            if j == 0:
                if machine == 0:
                    mEndTime[machine] += processingTime
                else:
                    mEndTime[machine] = max(mEndTime[machine], mEndTime[machine - 1]) + processingTime
            else:
                mEndTime[machine] = max(mEndTime[machine], mEndTime[machine - 1]) + processingTime

    maxEndTime = max(mEndTime)

    return maxEndTime


def INSA(elem, m, iterations, task):
    bestSchedule = []
    bestCmax = float('inf')

    for i in range(iterations):
        currentCmax = Cmax(task)

        # Lokalne przeszukiwanie sąsiedztwa
        improved = True
        while improved:
            improved = False
            for j in range(elem):
                for k in range(1, len(task[j].p)):
                    task[j].p[k - 1], task[j].p[k] = task[j].p[k], task[j].p[k - 1]
                    newCmax = Cmax(task)
                    if newCmax < currentCmax:
                        currentCmax = newCmax
                        improved = True
                    else:
                        task[j].p[k - 1], task[j].p[k] = task[j].p[k], task[j].p[k - 1]

        # Aktualizacja najlepszego harmonogramu
        if currentCmax < bestCmax:
            bestCmax = currentCmax
            bestSchedule = task.copy()

    return bestSchedule


if __name__ == '__main__':
    rng = RandomNumberGenerator(2451)
    task = []
    tmp = Task()
    o = []
    elem = 5
    m = 4
    iterations = 1000

    for i in range(elem):
        pomoc_o = rng.nextInt(1, math.floor(m * 1.2)) + 1
        o.append(pomoc_o)
        for j in range(o[i]):
            pomoc = rng.nextInt(1, 29)
            tmp.p.append(pomoc)

        for j in range(o[i]):
            pomoc = rng.nextInt(1, m)
            tmp.u.append(pomoc)
        tmp.number = i + 1
        task.append(tmp)
        tmp = Task()

    # Wyświetlenie wygenerowanego harmonogramu
    for i in range(elem):
        print(task[i].number, ".")
        print("p: [", end="")
        for j in range(len(task[i].p)):
            if j == len(task[i].p) - 1:
                print(task[i].p[j], end="")
            else:
                print(task[i].p[j], ", ", end="")
        print("]")

        print("u: [", end="")
        for j in range(len(task[i].u)):
            if j == len(task[i].u) - 1:
                print(task[i].u[j], end="")
            else:
                print(task[i].u[j], ", ", end="")
        print("]")

    bestSchedule = INSA(elem, m, iterations, task)

    mEndTime = [0] * m

    for i in range(len(bestSchedule)):
        for j in range(len(bestSchedule[i].p)):
            machine = bestSchedule[i].u[j] - 1
            processingTime = bestSchedule[i].p[j]

            if j == 0:
                if machine == 0:
                    mEndTime[machine] += processingTime
                else:
                    mEndTime[machine] = max(mEndTime[machine], mEndTime[machine - 1]) + processingTime
            else:
                mEndTime[machine] = max(mEndTime[machine], mEndTime[machine - 1]) + processingTime

    print("Czasy zakończenia zadań na maszynach:")
    for m in range(1, m + 1):
        print("Maszyna", m, ":", mEndTime[m - 1])

    bestCmax = Cmax(bestSchedule)
    print("Wartość Cmax:", bestCmax)
