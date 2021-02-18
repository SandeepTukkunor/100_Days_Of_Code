import random 

def play():
    user = input(" 'r' for rock, 'p' for paper , 's' for scissor")
    computer = random.choice(["r", "p","s"])


    if user == computer:
        print("tie")

    if is_win(user, computer):
        return "you won "
    
    return "you lost "

#r> s, s>p, p>r


def is_win(player, oppenent):

    if (player == 'r' and oppenent == "s") or (player == 's' and oppenent == 'p' ) or (player == 'p' and oppenent == 'r'):
        return "you won"

print(play())





