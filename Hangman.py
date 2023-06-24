class hang:
    def readFile(self):
        reader = open("wordList.txt", "r")
        word = reader.readline()
        self.wordList = reader.read().split("\n")
        print(self.wordList)
    def onePlayer(self):
        pass  

ob = hang()
ob.readFile()