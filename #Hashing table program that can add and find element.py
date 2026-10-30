#Hashing table program that finds elements in a hashtable
import random

KEY = random.randint(1,10) # Saftey measure against hackers
List =[[] for i in range(10)]

def HashFinder(INPUT):
    INDEX = 0
    TOTAL = KEY
    for letter in INPUT:
       TOTAL += (TOTAL+ord(letter)**2) 

    INDEX = TOTAL % 10

    return INDEX


def InsertionHashTable(Insert):
    INDEX = 0
    TOTAL = KEY
    
    for letter in Insert:
        TOTAL += (TOTAL+ord(letter)**2) 
    
    INDEX = TOTAL % 10

    List[INDEX].append(Insert)

    return List


while True:
    Choice = input("What do you want to do: Find(f) or Insert(i) or Exit(e):  ").lower()

    if Choice == "f":
        INPUT = input("[What do you want to find]:  ")
        Finding = List[HashFinder(INPUT)]
        
        if Finding.count(INPUT) < 1:
            print("NONE")

        else:
            print(INPUT," is located at index  ",HashFinder(INPUT))

        

    elif Choice == "i":
        Insert = input("[What do you want to insert into the Hashtable]:  ")
        NewList = InsertionHashTable(Insert)
        List = NewList
        
    elif Choice == "e":
        print("___Program Closed___")
        break

       