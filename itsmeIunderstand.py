import random


###NOVBETI MERHELEYE KECHMEK ISTEYIB ISTEMEDIYINI SORMALIYAM  ### istemirse, break


############################################################
def baraj(earn):
    if earn <1000:
        print("Siz udush qazanmadiniz...")
        
    if earn > 1000 and earn < 32000:
        print("Udushunuz $ 1000 oldu..." )
        
    if earn > 32000 and earn < 1000000:
        print("Udushunuz $ 32000 oldu..." )
    if earn == 1000000:
        print("Millionersiniz !!!!! ")
##############################################################











Questions = [
    ["The capital of Estonia ?", ["Tallin" ,"Vilnus",  "RIga" , "Skopie"] , "Tallin"  , 100], 
    ["What sort of animal is Walt Disnay's Dumbo ?", ["Deer" ,"Rabbit",  "Elephant" , "Donkey"] , "Elephant" , 200],
    ["How many works have N.Ganjavi's Khamsa ? ", [7 ,2,  5 , 10] , 5  , 300], 
    ["In what year did the Berlin Wall collapse?" , [1991 , 1992,  1989 , 1990] , 1991 , 500],
    ["What country surrounds the Vatican?" , ["Italy" ,"Canada",  "Russia" , "Spain"] , "Italy"  , 1000], 
    ["What is the name of the tallest mountain in the world?", ["Everest" ,"Merchison",  "SamaniPiki" , "Klimancaro"] , "Everest" , 2000],
    ["In what country would you find Stonehenge?", ["United Kingdom" ,"Denmark",  "Antigua and Barbuda" , "Tunis"] , "United Kingdom"  , 4000], 
    ["Which toys have been marketed with the phrase “robots in disguise?", ["Bratz Dolls" ,"Sylvanian Families",  "Hatchimals" , "Transformers"] ,"Transformers" , 8000],
    ["What does the word loquacious mean?", ["Angry" ,"Chatty",  "Beautiful" , "Shy"] , "Chatty"  , 16000], 
    ["Which of these religious observances lasts for the shortest period of time during the calendar year?", ["Ramadan" ,"Diwali",  "Lent" , "Hanukkah"] , "Diwali" , 32000],
    ["Construction of which of these famous landmarks was completed first?", ["Empire State Building" ,"Royal Albert Hall",  "Eiffel Tower" , "Big Ben Clock Tower"] , "Big Ben Clock Tower"  ,64000], 
    ["At the closest point, which island group is only 50 miles south-east of the coast of Florida?", ["Bahamas" ,"US Virgin Islands",  "Turks and Caicos Islands" , "Bermuda"] , "Bahamas" , 125000],
    ["Which battles took place between the Royal Houses of York and Lancaster?", ["Thirty Years War" ,"Hundred Years War",  "War of the Roses" , "English Civil War"] , "War of the Roses"  , 250000], 
    ["Queen Anne was the daughter of which English Monarch?", ["James II" ,"Henry VIII",  "Victoria" , "William I"] , "James II" , 500000],
    ["Which Shakespeare play features the line 'Neither a borrower nor a lender be'?", ["Hamlet" ,"Macbeth",  "Othello" , "The Merchant of Venice"] , "Hamlet"  , 1000000]
    ]


Jokers = [ "50/50", "CallFriend", "Auditory"]


print(len(Jokers))


print('''Ladies and Gentlemen !
      
    Welcome to a new round of 
      
    Who
    Wants
    To be
    a Millionaire ?!
    
    Our first Condidate tonight is ...    
    ''')

while True:
    
    
        
            
    
      
    namegamer = input("What is your name ? ")
    print(namegamer , " welcome to Who Wants to Be a Millionaire. Good luck!")
    start_game = input("Are you ready to play? (yes or no) ")
    if start_game.lower() == "yes":
        print(f"Everyone, A BIG ROUND OF APPLOUSE FOR OUR CONDIDATE {namegamer} \n")
        print('''Ok. Lets get started.For each question, select the correct answer by choosing A, B, C or D. First a reminder you have 3 Jokers:
    A) 50/50 Joker
    B) The Telephone Joker
    C)The Audience Joker
              
OK, LET'S GO !
            ''') 
        
    for num in Questions:
        
        
        
        def answer_A():
            if trueAnswer == answers[0]:
                print("Super. Correct answer!!")
                
        
        
        
        
        answers = num[1]   
        random.shuffle(answers)
        trueAnswer = num[2]
        amount = num[3]
        print(f"{Questions.index(num) +1} . {num[0]}")
        print(num[3])       
         
        print(f"  A) {answers[0]} \n  B) {answers[1]} \n  C) {answers[2]}  \n  D) {answers[3]}")
        
        answer = input("Sechiminiz ? ")
        if answer.upper() == "A":
            if answers[0] == trueAnswer:
                print("Super. Correct answer !!")
                if amount ==1000000:
                    baraj(amount)
                    break
                step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                if step ==1:                    
                    continue
                else:
                    print(f"{amount} Qazandiniz")
                    break
            else:
                print("Sorry. InCorrect")
                baraj(amount)   
                break             
        elif answer.upper() == "B":
            if answers[1] == trueAnswer:
                print("Super. Correct answer !!")
                if amount ==1000000:
                    baraj(amount)
                    break
                step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                if step ==1:                    
                    continue
                else:
                    print(f"{amount} Qazandiniz")
                    break
                
            else:
                print("Sorry. InCorrect")
                baraj(amount)
                break
        elif answer.upper() == "C":
            if answers[2] == trueAnswer:
                print("Super. Correct answer !!")
                if amount ==1000000:
                    baraj(amount)
                step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                if step ==1:                    
                    continue
                else:
                    print(f"{amount} Qazandiniz")
                    break
                
            else:
                print("Sorry. InCorrect")
                baraj(amount)
                break
        elif answer.upper() == "D":
            if answers[3] == trueAnswer:
                print("Super. Correct answer !!")
                if amount ==1000000:
                    baraj(amount)
                step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                if step ==1:                    
                    continue
                else:
                    print(f"{amount} Qazandiniz")
                    break
                
            else:
                print("Sorry. InCorrect")       
                baraj(amount)      
                break
        elif answer.upper() == "J":            
            print(Jokers)
            chooseJoker = input("Jokerlerdennbirini seche bilersiniz: ")
            
################################################################################
#####################################################################################
######################################################################################           
            
            if chooseJoker == "1":
                Jokers.remove("50/50")
                copyansw = num[1]
                copyansw.remove(trueAnswer)
                Kalanlar =[]
                Kalanlar = random.choices(copyansw, k = 1)
                Kalanlar.append(trueAnswer)
                
                print(f"A) {Kalanlar[0]}\t B) {Kalanlar[1]}")
                newanswer = input("Qalan varianlardan dogru bildiyinizi sechin:  ") 
                
                if newanswer.upper() == "A":
                    if Kalanlar[0] == trueAnswer:
                        print("Super. Correct answer !!")
                        if amount ==1000000:
                            baraj(amount)
                            break
                        step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                        if step ==1:                    
                            continue
                        else:
                            print(f"{amount} Qazandiniz")
                            break
                    else:
                        print("Sorry. InCorrect")
                        baraj(amount)   
                        break             
                elif newanswer.upper() == "B":
                    if Kalanlar[1] == trueAnswer:
                        print("Super. Correct answer !!")
                        if amount ==1000000:
                            baraj(amount)
                            break
                        step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                        if step ==1:                    
                            continue
                        else:
                            print(f"{amount} Qazandiniz")
                            break
                
                    else:
                        print("Sorry. InCorrect")
                        baraj(amount)
                        break
                
                elif newanswer.upper() == "J":            
                    print(Jokers)
                    chooseJoker = input("Jokerlerdennbirini seche bilersiniz: ")
                    if chooseJoker == "2":
                        Jokers.remove("CallFriend")
                        print(f"friend's choose is {trueAnswer}")
                        answer = input("Do you approve this? and choose your variant : ")
                        if answer.upper() == "A":
                            if answers[0] == trueAnswer:
                                print("Super. Correct answer !!")
                                if amount ==1000000:
                                    baraj(amount)
                                step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                                if step ==1:                    
                                    continue
                                else:
                                    print(f"{amount} Qazandiniz")
                                    break
                            else:
                                print("Sorry. InCorrect")
                                baraj(amount)
                                break
                        elif answer.upper() == "B":
                            if answers[1] == trueAnswer:
                                print("Super. Correct answer !!")
                                if amount ==1000000:
                                    baraj(amount)
                                step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                                if step ==1:                    
                                    continue
                                else:
                                    print(f"{amount} Qazandiniz")
                                    break
                            else:
                                print("Sorry. InCorrect")
                                baraj(amount)
                                break
                        elif answer.upper() == "C":
                            if answers[2] == trueAnswer:
                                print("Super. Correct answer !!")
                                if amount ==1000000:
                                    baraj(amount)
                                step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                                if step ==1:                    
                                    continue
                                else:
                                    print(f"{amount} Qazandiniz")
                                    break
                            else:
                                print("Sorry. InCorrect")
                                baraj(amount)
                                break
                        elif answer.upper() == "D":
                            if answers[3] == trueAnswer:
                                print("Super. Correct answer !!")
                                if amount ==1000000:
                                    baraj(amount)
                                step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                                if step ==1:                    
                                    continue
                                else:
                                    print(f"{amount} Qazandiniz")
                                    break
                            else:
                                print("Sorry. InCorrec  t")       
                                baraj(amount)
                                break       
                        elif answer.upper() == "J":
                            print(f" {Jokers}  jokerlerini de kullana bilersiz. ")
                            chooseJoker = input("Use Joker: ")
                        
                        if chooseJoker == "3":
                            Jokers.remove("Auditory")
                             
                            if answers[0] == trueAnswer:
                                print(" A) --> 78%, B --> 5% , C-->9% , D -->8% ")
                            elif answers[1] == trueAnswer:
                                print(" A) --> 5%, B --> 78% , C-->9% , D -->8% ")
                            elif answers[2] == trueAnswer:
                                print(" A) --> 5%, B --> 9% , C-->78% , D -->8% ")
                            elif answers[3] == trueAnswer:
                                print(" A) --> 5%, B --> 8% , C-->9% , D -->78% ")
                                
                            answer = input("Again ! ENter your selection : ")
                            if answer.upper() == "A": 
                                if answers[0] == trueAnswer:
                                    print("Super. Correct answer !!")
                                    if amount ==1000000:
                                        baraj(amount)
                                        break
                                    step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                                    if step ==1:                    
                                        continue
                                    else:
                                        print(f"{amount} Qazandiniz")
                                        break
                                else:
                                    print("Sorry. InCorrect")
                                    baraj(amount)   
                                    break             
                            elif answer.upper() == "B":
                                if answers[1] == trueAnswer:
                                    print("Super. Correct answer !!")
                                    if amount ==1000000:
                                        baraj(amount)
                                        break
                                    step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                                    if step ==1:                    
                                        continue
                                    else:
                                        print(f"{amount} Qazandiniz")
                                        break
                                else:
                                    print("Sorry. InCorrect")
                                    baraj(amount)
                                    break
                            elif answer.upper() == "C":
                                if answers[2] == trueAnswer:
                                    print("Super. Correct answer !!")
                                    if amount ==1000000:
                                        baraj(amount)
                                    step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                                    if step ==1:                    
                                        continue
                                    else:
                                        print(f"{amount} Qazandiniz")
                                        break
                                else:
                                    print("Sorry. InCorrect")
                                    baraj(amount)
                                    break
                            elif answer.upper() == "D":
                                if answers[3] == trueAnswer:
                                    print("Super. Correct answer !!")
                                    if amount ==1000000:
                                        baraj(amount)
                                    step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                                    if step ==1:                    
                                        continue
                                    else:
                                        print(f"{amount} Qazandiniz")
                                        break
                                else:
                                    print("Sorry. InCorrect")       
                                    baraj(amount)      
                                    break
                            elif answer.upper() == "J":
                                print(Jokers)
                                chooseJoker = input("Jokerlerdennbirini seche bilersiniz: ")
                            
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                        
            elif chooseJoker == "3":
                Jokers.remove("Auditory")
                
                if answers[0] == trueAnswer:
                    print(" A) --> 78%, B --> 5% , C-->9% , D -->8% ")
                elif answers[1] == trueAnswer:
                    print(" A) --> 5%, B --> 78% , C-->9% , D -->8% ")
                elif answers[2] == trueAnswer:
                    print(" A) --> 5%, B --> 9% , C-->78% , D -->8% ")
                elif answers[3] == trueAnswer:
                    print(" A) --> 5%, B --> 8% , C-->9% , D -->78% ")
                answer = input("Again ! ENter your selection : ")
                if answer.upper() == "A": 
                    if answers[0] == trueAnswer:
                        print("Super. Correct answer !!")
                        if amount ==1000000:
                            baraj(amount)
                            break
                        step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                        if step ==1:                    
                            continue
                        else:
                            print(f"{amount} Qazandiniz")
                            break
                    else:
                        print("Sorry. InCorrect")
                        baraj(amount)   
                        break             
                elif answer.upper() == "B":
                    if answers[1] == trueAnswer:
                        print("Super. Correct answer !!")
                        if amount ==1000000:
                            baraj(amount)
                            break
                        step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                        if step ==1:                    
                            continue
                        else:
                            print(f"{amount} Qazandiniz")
                            break
                    else:
                        print("Sorry. InCorrect")
                        baraj(amount)
                        break
                elif answer.upper() == "C":
                    if answers[2] == trueAnswer:
                        print("Super. Correct answer !!")
                        if amount ==1000000:
                            baraj(amount)
                        step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                        if step ==1:                    
                            continue
                        else:
                            print(f"{amount} Qazandiniz")
                            break
                    else:
                        print("Sorry. InCorrect")
                        baraj(amount)
                        break
                elif answer.upper() == "D":
                    if answers[3] == trueAnswer:
                        print("Super. Correct answer !!")
                        if amount ==1000000:
                            baraj(amount)
                        step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                        if step ==1:                    
                            continue
                        else:
                            print(f"{amount} Qazandiniz")
                            break
                    else:
                        print("Sorry. InCorrect")       
                        baraj(amount)      
                        break
                elif answer.upper() == "J":            
                    print(Jokers)
                    chooseJoker = input("Jokerlerdennbirini seche bilersiniz: ")
                    
                    if chooseJoker == "2":
                        Jokers.remove("CallFriend")
                        print(f"friend's choose is {trueAnswer}")
                        answer = input("Do you approve this? and choose your variant : ")
                        if answer.upper() == "A":
                            if answers[0] == trueAnswer:
                                print("Super. Correct answer !!")
                                if amount ==1000000:
                                    baraj(amount)
                                step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                                if step ==1:                    
                                    continue
                                else:
                                    print(f"{amount} Qazandiniz")
                                    break
                            else:
                                print("Sorry. InCorrect")
                                baraj(amount)
                                break
                        elif answer.upper() == "B":
                            if answers[1] == trueAnswer:
                                print("Super. Correct answer !!")
                                if amount ==1000000:
                                    baraj(amount)
                                step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                                if step ==1:                    
                                    continue
                                else:
                                    print(f"{amount} Qazandiniz")
                                    break
                            else:
                                print("Sorry. InCorrect")
                                baraj(amount)
                                break
                        elif answer.upper() == "C":
                            if answers[2] == trueAnswer:
                                print("Super. Correct answer !!")
                                if amount ==1000000:
                                    baraj(amount)
                                step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                                if step ==1:                    
                                    continue
                                else:
                                    print(f"{amount} Qazandiniz")
                                    break
                            else:
                                print("Sorry. InCorrect")
                                baraj(amount)
                                break
                        elif answer.upper() == "D":
                            if answers[3] == trueAnswer:
                                print("Super. Correct answer !!")
                                if amount ==1000000:
                                    baraj(amount)
                                step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                                if step ==1:                    
                                    continue
                                else:
                                    print(f"{amount} Qazandiniz")
                                    break
                            else:
                                print("Sorry. InCorrec  t")       
                                baraj(amount)
                                break       
                        elif answer.upper() == "J":
                            print(f" {Jokers}  jokerlerini de kullana bilersiz. ")
                    
                    
                        if chooseJoker == "1":
                            Jokers.remove("50/50")
                            copyansw = num[1]
                            copyansw.remove(trueAnswer)
                            Kalanlar =[]
                            Kalanlar = random.choices(copyansw, k = 1)
                            Kalanlar.append(trueAnswer)
                
                            print(f"A) {Kalanlar[0]}\t B) {Kalanlar[1]}")
                            newanswer = input("Qalan varianlardan dogru bildiyinizi sechin:  ") 
                        
                            if newanswer.upper() == "A":
                                if answers[0] == trueAnswer:
                                    print("Super. Correct answer !!")
                                    if amount ==1000000:
                                        baraj(amount)
                                        break
                                    step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                                    if step ==1:                    
                                        continue
                                    else:
                                        print(f"{amount} Qazandiniz")
                                        break
                                else:
                                    print("Sorry. InCorrect")
                                    baraj(amount)   
                                    break             
                            elif newanswer.upper() == "B":
                                if answers[1] == trueAnswer:
                                    print("Super. Correct answer !!")
                                    if amount ==1000000:
                                        baraj(amount)
                                        break
                                    step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                                    if step ==1:                    
                                        continue
                                    else:
                                        print(f"{amount} Qazandiniz")
                                        break
                
                                else:
                                    print("Sorry. InCorrect")
                                    baraj(amount)
                                    break
                        
                            elif answer.upper() == "J":            
                                print(Jokers)
                                chooseJoker = input("Jokerlerdennbirini seche bilersiniz: ")
                    
                    
                    ##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                    
                    
                    
                    
        
            ###########################################
            elif chooseJoker == "2":
                Jokers.remove("CallFriend")
                print(f"friend's choose is {trueAnswer}")
                answer = input("Do you approve this? and choose your variant : ")
                if answer.upper() == "A":
                    if answers[0] == trueAnswer:
                        print("Super. Correct answer !!")
                        if amount ==1000000:
                            baraj(amount)
                        step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                        if step ==1:                    
                            continue
                        else:
                            print(f"{amount} Qazandiniz")
                            break
                    else:
                        print("Sorry. InCorrect")
                        baraj(amount)
                        break
                elif answer.upper() == "B":
                    if answers[1] == trueAnswer:
                        print("Super. Correct answer !!")
                        if amount ==1000000:
                            baraj(amount)
                        step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                        if step ==1:                    
                            continue
                        else:
                            print(f"{amount} Qazandiniz")
                            break
                    else:
                        print("Sorry. InCorrect")
                        baraj(amount)
                        break
                elif answer.upper() == "C":
                    if answers[2] == trueAnswer:
                        print("Super. Correct answer !!")
                        if amount ==1000000:
                            baraj(amount)
                        step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                        if step ==1:                    
                            continue
                        else:
                            print(f"{amount} Qazandiniz")
                            break
                    else:
                        print("Sorry. InCorrect")
                        baraj(amount)
                        break
                elif answer.upper() == "D":
                    if answers[3] == trueAnswer:
                        print("Super. Correct answer !!")
                        if amount ==1000000:
                            baraj(amount)
                        step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                        if step ==1:                    
                            continue
                        else:
                            print(f"{amount} Qazandiniz")
                            break
                    else:
                        print("Sorry. InCorrec  t")       
                        baraj(amount)
                        break       
                elif answer.upper() == "J":
                    print(f" {Jokers}  jokerlerini de kullana bilersiz. ")
                    chooseJoker = input("Use Joker: ")
                    if chooseJoker == "1": 
                        
                        Jokers.remove("50/50")
                        copyansw = num[1]
                        copyansw.remove(trueAnswer)
                        Kalanlar =[]
                        Kalanlar = random.choices(copyansw, k = 1)
                        Kalanlar.append(trueAnswer)
                
                        print(f"A) {Kalanlar[0]}\t B) {Kalanlar[1]}")
                        mewanswer = input("Qalan varianlardan dogru bildiyinizi sechin:  ") 
                        
                        if newanswer.upper() == "A":
                            if answers[0] == trueAnswer:
                                print("Super. Correct answer !!")
                                if amount ==1000000:
                                    baraj(amount)
                                    break
                                step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                                if step ==1:                    
                                    continue
                                else:
                                    print(f"{amount} Qazandiniz")
                                    break
                            else:
                                print("Sorry. InCorrect")
                                baraj(amount)   
                                break             
                        elif newanswer.upper() == "B":
                            if answers[1] == trueAnswer:
                                print("Super. Correct answer !!")
                                if amount ==1000000:
                                    baraj(amount)
                                    break
                                step = int(input("novbeti suala kechmek isteyirsiniz?  1.YES   2.NO"))
                                if step ==1:                    
                                   continue
                                else:
                                    print(f"{amount} Qazandiniz")
                                    break
                
                            else:
                                print("Sorry. InCorrect")
                                baraj(amount)
                                break
                        
                        elif answer.upper() == "J":            
                            print(Jokers)
                            chooseJoker = input("Jokerlerdennbirini seche bilersiniz: ")
                      
                    
                    
                        
        else:
            print("sorulari Pass keche bilmersiniz !! Cavablardan birisini sechin !!")
            
            
            
            
            
            
            

            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    Oyun = input("Davam ya Tamam?  ")
    if Oyun == "Tamam":
       break
    





























