import random


def all_choices(): 
    player_choice = input("Enter your choice of destruction: rock , paper ,scisorrs: ")
    
    options = ["rock", "paper", "scisorrs"]
    
    comp_choice = random.choice(options)
    
    choices = {"Player" : player_choice , "Computer" : comp_choice}

    return choices

def win_condition(player,computer):
    print(f'You chose {player} and computer chose {computer}')
    
    if player == computer:
        return "Its a tie, Lame"
    elif player == "rock":
        if computer == "scisorrs":
            return "WOW you won against a computer. Congratulatios -_-"
        else:
            return "HOW CAN YOU LOSE AGAINST AN AI!!!! skill issue"
    
    elif player == "paper":
        if computer == "rock":
            return "HOW CAN YOU LOSE AGAINST AN AI!!!! skill issue"
        else:
            return "WOW you won against a computer. Congratulatios -_-"
    
    elif player == "scisorrs":
        if computer == "rock":
            return "HOW CAN YOU LOSE AGAINST AN AI!!!! skill issue"
        else:
            return "WOW you wosn against a computer. Congratulatios -_-"


choice = all_choices()
result_calculate = win_condition(choice["Player"], choice["Computer"])  
print(result_calculate)          
               
