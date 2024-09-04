import random
import time

class FruitQuiz:
    def __init__(self):
        self.fruitdict = {"apple":"red",
                          "orange":"orange",
                          "grapes":"purple",
                          "mango":"yellow"}
        
    def quiz(self):
        print("Enter (in small letters)")
        time.sleep(1)
        while True:    
            fruit = random.choice(list(self.fruitdict.items()))
            print(" The colour of" ,fruit[0])
            time.sleep(1)
            colour = input(" Enter here: ")
            if colour == self.fruitdict[fruit[0].lower()]:
                print("Correct answer")
            else:
                print("Wrong answer")
            time.sleep(1)
            repeat = input("Do you want to play again? (Y/N): ")
            if repeat == "N":
                break

print("Hello! Welcome to the fruit quiz")
time.sleep(1)
print("We are going to ask a fruit and you are going to tell it's colour")
time.sleep(1)
fq = FruitQuiz()
fq.quiz()
print("Thank you for playing this game with us. See you! Bye Bye :)")