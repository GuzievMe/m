
import string

import random


Questions = [
    [["The capital of Estonia ?"], [["Tallin"] ,["Vilnus"], [ "RIga"] , ["Skopie"]] , ["Tallin"]  , ["The 1000 $ Question"]], 
    [["What sort of animal is Walt Disnay's Dumbo ?"], [["Deer"] ,["Rabbit"], [ "Elephant"] , ["Donkey"]] , ["Elephant"] , ["The 2000 $ Question"]],
    [[], [[7] ,[3], [ "RIga"] , ["Skopie"]] , ["Tallin"]  , ["The 1000 $ Question"]], 
    [["What sort of animal is Walt Disnay's Dumbo ?"], [["Deer"] ,["Rabbit"], [ "Elephant"] , ["Donkey"]] , ["Elephant"] , ["The 2000 $ Question"]],
    [["The capital of Estonia ?"], [["Tallin"] ,["Vilnus"], [ "RIga"] , ["Skopie"]] , ["Tallin"]  , ["The 1000 $ Question"]], 
    [["What sort of animal is Walt Disnay's Dumbo ?"], [["Deer"] ,["Rabbit"], [ "Elephant"] , ["Donkey"]] , ["Elephant"] , ["The 2000 $ Question"]],
    [["The capital of Estonia ?"], [["Tallin"] ,["Vilnus"], [ "RIga"] , ["Skopie"]] , ["Tallin"]  , ["The 1000 $ Question"]], 
    [["What sort of animal is Walt Disnay's Dumbo ?"], [["Deer"] ,["Rabbit"], [ "Elephant"] , ["Donkey"]] , ["Elephant"] , ["The 2000 $ Question"]],
    [["The capital of Estonia ?"], [["Tallin"] ,["Vilnus"], [ "RIga"] , ["Skopie"]] , ["Tallin"]  , ["The 1000 $ Question"]], 
    [["What sort of animal is Walt Disnay's Dumbo ?"], [["Deer"] ,["Rabbit"], [ "Elephant"] , ["Donkey"]] , ["Elephant"] , ["The 2000 $ Question"]],
    [["The capital of Estonia ?"], [["Tallin"] ,["Vilnus"], [ "RIga"] , ["Skopie"]] , ["Tallin"]  , ["The 1000 $ Question"]], 
    [["What sort of animal is Walt Disnay's Dumbo ?"], [["Deer"] ,["Rabbit"], [ "Elephant"] , ["Donkey"]] , ["Elephant"] , ["The 2000 $ Question"]],
    [["The capital of Estonia ?"], [["Tallin"] ,["Vilnus"], [ "RIga"] , ["Skopie"]] , ["Tallin"]  , ["The 1000 $ Question"]], 
    [["What sort of animal is Walt Disnay's Dumbo ?"], [["Deer"] ,["Rabbit"], [ "Elephant"] , ["Donkey"]] , ["Elephant"] , ["The 2000 $ Question"]],
    [["The capital of Estonia ?"], [["Tallin"] ,["Vilnus"], [ "RIga"] , ["Skopie"]] , ["Tallin"]  , ["The 1000 $ Question"]], 
  
    ]


namegamer = input("What is your name? ")

print(namegamer , " welcome to Who Wants to Be a Millionaire. Good luck!")
start_game = input("Are you ready to play? (yes or no) ")
if start_game == "yes":
    print('\nTELIMATM:\nFor each question, select the correct answer by choosing A, B, C or D. or if you want use Joker, select J')
    for i in range(len(Questions)):
        originalanswers = Questions[i][1]
        print(Questions[i][0], "\n" , (Questions[i][1]) , "\n" , "earn", Questions[i][3])
        random.shuffle(Questions[i][1])
        A = Questions[i][1][0]
        B = Questions[i][1][1]
        C = Questions[i][1][2]
        D = Questions[i][1][3]
        print("A)",Questions[i][1][0],"B)",Questions[i][1][1],"C",Questions[i][1][2],"D",Questions[i][1][3] )
        Answ= input("EnterVariant")
        if Answ == originalanswers[i][1][0]:
            "Good"
          
                                                                          #     print("That is Correct", "\n" , "You have just earned ", Questions[i][3])
    
                                                                               # COntinue = input("Answer the next question for a chance to win $7,000 (yes or no)")
                                                                                 # if COntinue == "yes":
                                                                                  #     pass
            
    
#  correct."yes"
# 

# 







else:
    print(namegamer, "Get tezeden gelersen !! :D")
    
# a = random.shuffle(Questions[0][1])
# print(a)









"""

class Player:
    def __init__(self, name=''):
        self.name = name
    def get_name(self):
        self.name = input("What is your name? ")
player = Player()
player.get_name()
                                                        #print(Questions[1])
def who_wants_to_be_a_millionaire():
    print(f"{player.name}, welcome to Who Wants to Be a Millionaire. Good luck!")
    start_game = input('Are you ready to play? (yes or no) ')
    if start_game == 'yes':
        print('\nInstructions:\nFor each question, select the correct answer by choosing A, B, C or D.')

        for i in range(len(test_questions)):


"""


random.shuffle(Questions[0][1])
print("A)",Questions[0][1][0],"B)",Questions[0][1][1],"C",Questions[0][1][2],"D",Questions[0][1][3] )

