import random 
def ropasi():
    user_score = 0
    computer_score = 0

    while True:
        print("WELCOME TO THE GAME")
        player = input("enter your choice:\n *rock\n *paper\n *scissors: ")
        player=player.lower()

        if player not in['rock','paper','scissors']:
            print("INVALID INPUT")
            continue

        com = random.choice(['rock','paper','scissors'])

        print("your choice",player)
        print("computer's choice",com)

        if player == com:
            print('DRAW!!')
        elif (player=='rock' and com=='scissors') or \
            (player=='scissors' and com=='paper') or \
                (player=='paper' and com=='rock'):
                print('you win!')  
                user_score +=1
        else:
                print('computer win!')
                computer_score+=1

        print(f"score- You: {user_score},Computer: {computer_score}")
        again=input("do you want to play again? (yes/no): ")
        if again.lower() != 'yes':
            if user_score>computer_score:
                print("        CONGRATULATIONS YOU WON!!!")
            elif user_score<computer_score:
                print("        COMPUTER WON , BETTER LUCK NEXT TIME"   )
            else:
                print("        IT IS A DRAW")
            break
        

r=ropasi()

                
     

    