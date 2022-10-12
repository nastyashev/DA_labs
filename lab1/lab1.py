from DefaultAlgorithm import balancedMultiwayMerging
from functions import fileGenerator
from functions import outputFile
import time

file_size = int(input("Enter size of file in MB: "))
numbers = int(file_size * pow(2, 20) / 4)
ways_num = int(input("Enter number of ways: "))

fileGenerator("A.bin", numbers)
print("File was successfully generated")

start = time.time()
balancedMultiwayMerging("A.bin", "Sorted.bin", ways_num)
finish = time.time()

print("Algorithm operation time: {0:10.3f}".format(finish - start))

output = input("Show result? [y / n]: ")
if output == "y":
    outputFile("Sorted.bin")
