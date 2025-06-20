import random
import time

OPARTORS = ['+', '-', '*']
min_oprand = 4
max_oprand = 13
total_problems = 10

def generate_expression(min_oprand, max_oprand):
    num1 = random.randint(min_oprand, max_oprand)
    num2 = random.randint(min_oprand, max_oprand)
    operator = random.choice(OPARTORS)

    expression = str(num1) + ' ' + operator + ' ' + str(num2)
    answer = eval(expression)
    return expression, answer

expr,ans = generate_expression(min_oprand, max_oprand)


wrong = 0
print("\nWelcome to the Math Quiz!")
print("You will be given 10 problems to solve.\n")

print("|| Let's start! ||\n")
print("--------------------------------")

start_time = time.time()

for i in range(total_problems):
    expr, ans = generate_expression(min_oprand, max_oprand)
    while True:
        guess = input(f"Problem #{i+1}: {expr} = ")
        if guess == str(ans):
            break
        else:
            wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("--------------------------------")
print("Quiz Completed!")
print("Nice Work!, You Finshe in ", total_time, "Seconds\n")

accuracy = ((total_problems - wrong) / total_problems) * 100
print("You got ", (total_problems - wrong), " Problems Correctly! at First Attempt")
print("You got ", round(accuracy, 2), "% Accuracy")
