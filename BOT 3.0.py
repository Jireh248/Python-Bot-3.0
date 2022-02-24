print("---------------------------------------------------------------------------------")

def welcome():
    name = "Hello my name is Jireh"
    print(name)
    
def conversation():
    convo = "Tell me about yourself "
    user = input("Where are you from: ")
    user2 = input("What is your dream job? ")
    print("Oh wow, I didnt youre from", user,"and", user2, "is interesting")

def guess():
    for i in range(1,10):
        num = int(input("Guess a number between 1 - 10: "))
        print(num)
        if i == (1,5):
            print("Youre right!!")
        else:
            print("Wrong!!")

welcome()
conversation()
guess()
