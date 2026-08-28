import random
choice=['rock','paper','scissor']

name=input("Enter your name:").upper()

ply_score=0
comp_score=0 

while True:
    print('===ROCK PAPER SCISSOR GAME===')
    print('CHOISE YOUR OPTION:')
    print('1.ROCK')
    print('2.PAPER')
    print('3.SCISSOR')
    print('4.EXIT')

    ply=int(input("ENTER A OPTION: "))
    if ply==4:
        print('---THANKS FOR PLAYING---')
        print(f'SCORE OF {name} IS: {ply_score:}')
        print(f'SCORE OF COMPUTER IS: {comp_score}')
        break
    elif ply==1:
        player='rock'
    elif ply==2:
        player='paper'
    else:
        player='scissor'

    print(f'{name} CHOICE: {player}')
    
    computer=random.choice(choice)
    print('COMPUTER CHOICE:',computer)
    if player==computer:
        print("TIE")

    elif player=='rock' and computer=='scissor' or player=='paper' and computer=='rock' or player=='scissor' and computer=='paper' :
        print(f'{player} BEATS {computer}')
        print(f'{name} WINS')
        ply_score=ply_score+1

    else:
        print(f'{computer} BEATS {player}')
        print(f'COMPUTER WINS')
        comp_score=comp_score+1
    print('\n')

    

