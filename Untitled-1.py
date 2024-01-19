logo= """


  ██████╗ ██╗   ██╗███████╗███████╗███████╗██╗███╗   ██╗ ██████╗      ██████╗  █████╗ ███╗   ███╗███████╗
 ██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝██║████╗  ██║██╔════╝     ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
 ██║  ███╗██║   ██║█████╗  ███████╗███████╗██║██╔██╗ ██║██║  ███╗    ██║  ███╗███████║██╔████╔██║█████╗  
 ██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║██║██║╚██╗██║██║   ██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
 ╚██████╔╝╚██████╔╝███████╗███████║███████║██║██║ ╚████║╚██████╔╝    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝





"""
print(logo)
import random
print("Welcome to Number Guessing Game!")
print("I am thinking of a number 1-100!")
choose=input("choose a difficulty. Type 'easy' or 'hard': ")
number_computer=random.randint(1,101)



#difficulty choosing
def option(): 
    if choose=="easy":
        print("you have 10 attempts")
        easy()
    elif choose=="hard":
        print("you have 5 attempts")
        hard()
    else:
        print("invalid option")

def result(number_user):

        if number_user < number_computer:
            print("Too Low")
            return False
        elif  number_user > number_computer:
             print("Too High")
             return False
        elif number_user ==  number_computer:

            print("You Have Won")
            return True
        else:
            print("invalid option")
            return False

def easy():
    attempts=10
    while attempts>0:
        attempts-=1
        number_user=int(input("Make a Guess: "))
        print(f"you have {attempts} left:")
        
        if result(number_user):
            break
        else:
          print("you run out of attempts you lose")

def hard():
    attempts=5
    while attempts>0:
        attempts-=1
        number_user=int(input("Make a Guess: "))
        print(f"you have {attempts} left:")
        if result(number_user):
            break
        else:
          print("you run out of attempts you lose")


print(option())    
  