from word_count_class import WordCount
import sys
from pathlib import Path

if len(sys.argv) == 1:
    print("You can also give filename as a command line argument")
    filename = input("Enter Filename: ")
else:
    filename = sys.argv[1].lower()

my_file = Path(filename)
if my_file.is_file():
    temp = WordCount(my_file)
    temp.readFile()
    temp.printTopTen()
else:
    print("Invalid File name")