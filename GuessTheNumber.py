import random

# r=random.randrange(1,11) # random no bte 1 to 10 avoid 11 for 0 to 11 we can write (11)
# r = random.randint(1, 10) # it will include 10 as well
# print(r)

print("|| Let's Play! ||\n")

max_num = int(input('enter the last number of range between you want to guess from 0 : '))
print("")

if max_num <= 0 :
    print("Plese enter a number grater than 0 next time :) " )
    quit()


random_number = random.randint(0,max_num)

# guess = int(input('Guess The Number betwee 0 to '+ str( max_num) + ' : '))
# attempt = 1

# while(True):
#     if guess != random_number :
#         guess = int(input('Wrong Guess! Try Again :( '))
#         attempt+=1

#     else  :
#         print("\nCongragulations Correct guess ",guess )
#         print("Total Attempt : ",attempt)
#         break

attempt = 0
while(True):
    if attempt  == 0 :
        guess = int(input('Guess The Number betwee 0 to '+ str( max_num) + ' :( ') )
    else :
        guess = int(input('Wrong Guess Try Agian!  :( ') )
    attempt += 1

    if guess != random_number :
        if guess < random_number :
            print('Enter A Larger Number ')
            continue
        else :
            print('Enter a Smaller Number ')
            continue
    else :
        print("\nCongragulations You Got Correct Guess i.e : ",guess )
        print("Total Attempt : ",attempt)
        break


    
