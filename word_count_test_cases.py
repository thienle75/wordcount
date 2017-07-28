from word_count_class import WordCount
import sys
from pathlib import Path
def runTest(filename):
    temp = WordCount(filename)
    temp.readFile()
    temp.printTopTen()

print("Test case 1: File not text file ")
my_file = Path('InputTestFiles/Testcase1.png')
if my_file.is_file():
    runTest(my_file)
else:
    print("Invalid File name")

print("===================================================")

print("Test case 2: Empty text File ")
my_file = Path('InputTestFiles/Testcase2.txt')
if my_file.is_file():
    runTest(my_file)
else:
    print("Invalid File name")

print("===================================================")

print("Test case 3: Normal text File ")
my_file = Path('InputTestFiles/Testcase3.txt')
if my_file.is_file():
    runTest(my_file)
else:
    print("Invalid File name")

print("===================================================") 

print("Test case 4: text File with contain &*() character ")
my_file = Path('InputTestFiles/Testcase4.txt')
if my_file.is_file():
    runTest(my_file)
else:
    print("Invalid File name")

print("===================================================")