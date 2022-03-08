# Python-Bot-3.0
#This is a bot that will take and store the users input, then evaluate the information to output it into a neat and organized table for the user to view

print("===================================BOT 3.0=====================================")
print("-------------------------------------------------------------------------------")

def welcome(): 
    name = "Hello my name is B.E.M.O" # Name of the bot
    print(name)

Q1 = input("What is your name?: ")


def conversation(): # Information on the user for data
    convo = ("Tell me about yourself",Q1)
    print() # line spacing
    print(convo)
    print() # line spacing
    Q2 = input("What is your dream job?: ")
    print() # line spacing
    Q3 = input("What is your favorite color?: ")
    print() # line spacing
    Q4 = int(input("What year were you born?: "))
    print() # line spacing
    print("hmmm... so you was born in",2022 - Q4)

    print("=====================================================================")
    print("Oh wow, I didnt you wanted to be a", Q2,"and", Q3, "is my favorite color too!?")
    print()

def guess(): # Quick guessing game for testing purposes
    num = int(input("Guess a number between 1 - 10: "))
    for i in range(1):
        if num >= 5:
            print("Youre right!!")
        else:
            if num <= 5:
                print("Wrong!!")
    print() # Line spacing
    
def bio():

    Q5 = input("Tell me more about yourself: ") # Bio/Info of the user
    print("==================================================================")
    print("Thanks for sharing that information about yourself",Q1,"!")

    print("Now that we know each other, lets take some information down to better assist you.") # This statement leads to the data entry conversation between B.E.M.O & user
    print("===================================================================")
    print()
    print("choose from the selection for me to better assist you.")
    print()

    Par = input("Paste paragraph here: ")

def wordCount(par): # Word count in paragraph 
    count = 0 
    for i in par:
        if i == (1,100):
            count += 1
        print(wordCount(par))
    return count


welcome()
conversation()
guess()
bio()
wordCount()
