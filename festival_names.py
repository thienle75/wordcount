from functools import partial, reduce
from itertools import chain
from typing import Iterator
import sys
from pathlib import Path
from word_count_class import WordCount

if len(sys.argv) == 1:
    print("You can also give filename as a command line argument")
    filename = input("Enter Filename: ")
else:
    filename = sys.argv[1]

my_file = Path(filename)
if my_file.is_file():
    temp = WordCount(my_file)
    temp.readCommonDelimeterFile()
    temp.printLongString()
else:
    print("Invalid File name")