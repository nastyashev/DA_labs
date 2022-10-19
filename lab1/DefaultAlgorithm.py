import os
import shutil
from functions import *


# основний алгоритм злиття
def balancedMultiwayMerging(pathNotSorted: str, pathSorded: str, waysNum: str):
    pathB = []
    pathC = []

    for i in range(waysNum):
        pathB.append(f"B{i + 1}.bin")
        pathC.append(f"C{i + 1}.bin")

    for path in pathC:
        with open(path, "wb") as file:
            pass

    splitA(pathNotSorted, pathB, waysNum)
    flag = True
    while not isSorted(pathNotSorted, pathB[0], pathC[0]):
        if flag:
            sortMerge(pathB, pathC, waysNum)
        else:
            sortMerge(pathC, pathB, waysNum)
        flag = not flag

    if os.path.getsize(pathNotSorted) == os.path.getsize(pathB[0]):
        shutil.copy(pathB[0], pathSorded)
    else:
        shutil.copy(pathC[0], pathSorded)

    for path in pathB:
        if os.path.exists(path):
            os.remove(path)
    for path in pathC:
        if os.path.exists(path):
            os.remove(path)


# розділення початкового файлу
def splitA(pathNotSorted: str, pathB: list, waysNum: str):
    fileA = FileReader(pathNotSorted)
    filesB = []
    for path in pathB:
        filesB.append(open(path, "wb"))

    bIndex = 0
    while fileA.current:
        filesB[bIndex].write(fileA.current)
        if fileA.current > fileA.next:
            bIndex = (bIndex + 1) % waysNum
        next(fileA)

    fileA.close()
    for file in filesB:
        file.close()


# злиття n файлів у інші n файлів
def sortMerge(pathsInputs: list, pathsOutputs: list, waysNum: int):
    readers = []
    writers = []

    index = 0
    prev_num = None

    for path in pathsInputs:
        readers.append(FileReader(path))

    for path in pathsOutputs:
        writers.append(open(path, "wb"))

    while (not isEOFReached(readers)):
        minNum = MAX_INT
        minIndex = -1

        for i in range(waysNum):
            if readers[i].current:
                number = int.from_bytes(readers[i].current, 'big')
                if prev_num == None or number >= prev_num:
                    if number <= minNum:
                        minNum = number
                        minIndex = i

        if minIndex == -1:
            prev_num = None
            index = (index + 1) % waysNum
        else:
            writers[index].write(minNum.to_bytes(4, 'big'))
            prev_num = minNum
            next(readers[minIndex])

    for file in readers:
        file.close()
    for file in writers:
        file.close()


# первіряє чи прочитані всі файли
def isEOFReached(readers):
    for file in readers:
        if file.current:
            return False
    return True


# перевіряє чи сортування завершилося
def isSorted(pathA: str, pathB: str, pathC: str) -> bool:
    return os.path.getsize(pathA) == os.path.getsize(pathB) or os.path.getsize(pathA) == os.path.getsize(pathC)
