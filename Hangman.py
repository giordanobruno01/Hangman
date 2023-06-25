import random
class hang:
    def readFile(self):
        reader = open("wordList.txt", "r")
        word = reader.readline()
        self.wordList = reader.read().split("\n")
    def onePlayer(self):
        n =  random.randint(0, len(self.wordList)-1)
        word = self.wordList[n]
        print("the answer is ", word)
        encrypt = ""
        if(len(word)<=6):
            n1 = random.randint(0,(len(word))//2)
            n2 = random.randint(((len(word))//2)+1,len(word)-1)
            
            for i in range(len(word)):
                if(n1==i or n2==i):
                    encrypt = encrypt+word[i]
                else:
                    encrypt = encrypt+"_"
        
        elif(len(word)>6 and len(word)<=10):
            n1 = random.randint(0,(len(word))//3)
            n2 = random.randint(((len(word))//3)+1,((len(word))//3)*2)
            n3 = random.randint((((len(word))//3)*2)+1, len(word)-1)
            
            for i in range(len(word)):
                if(n1==i or n2==i or n3==i):
                    encrypt = encrypt+word[i]
                else:
                    encrypt = encrypt+"_"
        else:
            n1 = random.randint(0,(len(word))//4)
            n2 = random.randint(((len(word))//4)+1,((len(word))//4)*2)
            n3 = random.randint((((len(word))//4)*2)+1, ((len(word))//4)*3)
            n4 = random.randint((((len(word))//4)*3)+1, len(word)-1)
            for i in range(len(word)):
                if(n1==i or n2==i or n3==i or n4==i):
                    encrypt = encrypt+word[i]
                else:
                    encrypt = encrypt+"_"
        char = ""            
        for i in range(10):
            va = encrypt
            print("\nyou have ",(10-i)," chances" )
            print("your word ", encrypt)
            char = input("\nguess a letter ")  
            
            if char in word:
                encrypt = ""
                for g in range(len(word)):
                    
                    if(word[g]==char):
                        encrypt = encrypt+ char
                    else:
                        encrypt = encrypt+ va[g]
            if (word==encrypt):
                print("you completed the game in ", i+1, " chances")
                print("the answer is ", word)
                return

        print("you lost, the answer is ", word)    
ob = hang()
ob.readFile()
ob.onePlayer()
