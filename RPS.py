import random

your_win = 0
comp_win = 0
total_tie = 0

options = ["rock","papper","sessior"]

while(True) :
    user_input = input('Wnter Rock, Papper, Sessior or Q to quit : ').lower()

    if user_input == "q" :
        break

    if user_input not in options :
        print('Invalid input')
        continue

    random_number = random.randint(0,2)
    # 0 - rock 1 - papper 2 - sessior

    comp_pick = options[random_number]
    print('computer picked ', comp_pick + '.')

    if user_input == "rock" and comp_pick == 'sessior':
        print('Congrate, You Win!\n')
        your_win += 1

    elif user_input == "papper" and comp_pick == 'rock':
        print('Congrate, You Win!\n')
        your_win += 1

    elif user_input == "sessior" and comp_pick == 'papper':
        print('Congrate, You Win!\n')
        your_win += 1

    elif user_input == comp_pick :
        print('Taied\n')
        total_tie += 1

    else :
        print('You Lost Computer Win :( \n')
        comp_win += 1

print('\n')
print('Your Total Win is : ', your_win )
print('computer Total win is : ', comp_win )
print('Total Number Of ties is : ', total_tie)
print('\nThanks For Playing , Comback Soon!')