from random import randint
MAX_INT = 2147483647

#заповнює файл випадковими числами
def fileGenerator(path: str, numbers: int):
    with open(path, "wb") as file:
        for i in range(numbers):
            file.write(randint(1, MAX_INT).to_bytes(4, "big"))


#виводить перші 50 чисел з файлу
def outputFile(path: str):
    list = []
    with open(path, "rb") as file:
        for i in range(50):
            number = int.from_bytes(file.read(4), 'big')
            list.append(number)
    print(" ".join(map(str, list)))


#допоміжний клас для зчитування з файлу
class FileReader:
    def __init__(self, path: str):
        self.path = path
        self.file = open(path, "rb")
        self.current = self.file.read(4)
        self.next = self.file.read(4)

    def __next__(self):
        temp = self.current
        self.current = self.next
        self.next = self.file.read(4)
        return temp

    def close(self):
        self.file.close()


