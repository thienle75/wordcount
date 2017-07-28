import operator
import itertools
import os

class WordCount:

    word_count = {}
    filename = ''
    ext = ''
    total = 0
    def __init__(self,filename):
        self.ext = os.path.splitext(filename)[-1].lower()
        self.filename = filename

    #==================================================================
    # Validate file type
    #==================================================================
       
    def validateFile(self):
        if self.ext.endswith(('.txt','.csv')):
            return True
        else:
            return False

    #==================================================================
    # Clean up each word
    #==================================================================        
    def cleanUpWord(self,word):
            symbols = "!@#$%^&*(){}:\"<>?,./;'[]'"
            for i in range(0, len(symbols)):
                word = word.replace(symbols[i],"")
            if len(word) > 0 :
                return word
            else:
                return ''

    #==================================================================
    # Read input file , split into words and store in an array and store
    # in a dictionary
    #==================================================================
    def readFile(self):
        if self.validateFile():
            infile = open(self.filename,'r') # open the file to read
            content = infile.read()  # read content of the file
            infile.close() # close the file when finish reading
            if content != '' :
                words = content.lower().split()
                for each_word in words:
                    word = self.cleanUpWord(each_word)
                    if word == '':
                        continue
                    if word in self.word_count:
                        self.word_count[word] += 1
                       
                    else:
                        self.word_count[word] =1 
                    self.total +=1
            else:
                print('File is empty')
        else:
            print('Invalid file Type')
    
    #==================================================================
    # Print out top ten words
    #================================================================== 
            
    def printTopTen(self):
        if len(self.word_count) == 0:
            print('Text file is empty')
        else:
            print("Total number words "+str(self.total))
            ten_list = itertools.islice(sorted(self.word_count.items(),key = lambda t:t[1],reverse = True),0,9)
            for key,value in ten_list:
                print("word : "+str(key), "count : "+str(value))    
