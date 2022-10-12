from DefaultAlgorithm import balancedMultiwayMerging
from functions import fileGenerator
import time

file_size = int(input("Enter size of file in MB: "))
numbers = int(file_size * pow(2, 20) / 4)
ways_num = int(input("Enter number of ways: "))

fileGenerator("A.bin", numbers)
print("File was successfully generated")

start_time = time.time()

balancedMultiwayMerging("A.bin", "Sorted.bin", ways_num)

print(f"\nAlgorithm operation time: {(time.time() - start_time)}s.")
