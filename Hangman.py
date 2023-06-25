import random
class hang:
    def readFile(self):
        reader = open("wordList.txt", "r")
        word = reader.readline()
        self.wordList = reader.read().split("\n")
    def onePlayer(self, name):
        n =  random.randint(0, len(self.wordList)-1)
        word = self.wordList[n].strip()
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
        points = 10         
        for i in range(10):
            va = encrypt
            print("\n",name, " have ",(10-i)," chances" )
            print("your word ", encrypt)
            char = input("\nguess a letter ") 
            char = char.strip() 
            
            if char in word:
                encrypt = ""
                for g in range(len(word)):
                    
                    if(word[g]==char):
                        encrypt = encrypt+ char
                    else:
                        encrypt = encrypt+ va[g]
            else:
                points -=1

            if (word==encrypt):
                print(name," completed the game in ", i+1, " chances")
                print("the answer is ", word)
                print("points earned in this round ", points)
                return points

        print(name," lost, the answer is ", word)
        return 0 
    def multiplePlayer(self, name1, name2):

        turns = int(input("how many turns each player? "))
        count1= 0
        count2 = 0
        for i in range(turns*2):
            if(i%2==0):
               count1 += self.onePlayer(name1)
               print("total score at the moment is ", count1)
            if(i%2!=0):
               count2 += self.onePlayer(name2)
               print("total score at the moment is ", count2)

        if(count1>count2):
            print(name1," is the winner with ", count1, " points")
        if(count1<count2):
            print(name2," is the winner with ", count2, " points")
        else:
            print("it is a tie")
ob = hang()
ob.readFile()            
print("WELCOME TO MY GAME")
while(True):
    print("1 for one player \n2 for two players\n3 to end the game")
    option = int(input("choose an option "))
    if(option==1):
        p = input("player name: ")
        while(True):
            ob.onePlayer(p)
            keep = input("do you want to keep playing? y for YES and n for NO")
            if(keep =="n"):
                break
            
    elif(option==2):
        name1 = input("player 1 name ")
        name2 = input("player 2 name ")
        while(True):
            ob.multiplePlayer(name1, name2)
            keep = input("do you want to keep playing? y for YES and n for NO")
            if(keep =="n"):
                break
    elif(option==3):
        print("game ended")
        break
    else:
        print("wrong input")           






p1 = input("player 1 name: ")
p2 = input("player 2 name: ")