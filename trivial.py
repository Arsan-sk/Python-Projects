#basi psudo code forproject

#list of questions
#answers foreach question
#randomly picking n numbers of question
#ask them to user
#check correct or wrong
#track the score
# show the score

import random

questions = {
    "What is a correct file extension for Python files?": ".py",
    "What does CPU stand for?": "processor",
    "Which language is primarily used for web development?": "javascript",
    "What is the full form of HTML?": "hypertext",
    "Which language is used for styling web pages?": "css",
    "What does SQL stand for?": "structured",
    "What keyword is used to define a function in Python?": "def",
    "Which company developed the Windows operating system?": "microsoft",
    "What does RAM stand for?": "memory",
    "What protocol is used to transfer web pages?": "http",
    "What symbol is used to comment a line in Python?": "#",
    "Which data structure uses FIFO?": "queue",
    "What does IDE stand for?": "environment",
    "What does OOP stand for?": "programming",
    "What keyword is used to create a class in Python?": "class",
    "What does API stand for?": "interface",
    "Which data structure uses LIFO?": "stack",
    "What is the extension of Java compiled files?": ".class",
    "What does DNS stand for?": "system",
    "Which command is used to install Python packages?": "pip",
    "What keyword is used to inherit a class in Python?": "super",
    "Which HTML tag is used to create a hyperlink?": "<a>",
    "What does CSS stand for?": "cascading",
    "Which method is used to add an element in a list in Python?": "append",
    "What operator is used for exponentiation in Python?": "**",
    "What is the binary equivalent of decimal 10?": "1010",
    "What data type is used to store True or False in Python?": "bool",
    "Which protocol is used for secure web browsing?": "https",
    "Which OS is based on the Linux kernel?": "android",
    "Which keyword is used to handle exceptions in Python?": "try",
    "What kind of loop continues until a condition is false?": "while",
    "What does GUI stand for?": "interface",
    "What does LAN stand for?": "network",
    "Which keyword is used to exit a loop in Python?": "break",
    "What is the time complexity of binary search?": "logarithmic",
    "What port does HTTP use by default?": "80",
    "What port does HTTPS use by default?": "443",
    "What kind of language is Python?": "interpreted",
    "Which operator checks equality in Python?": "==",
    "What keyword creates a constant in many languages?": "const",
    "What is the default file extension for C++ files?": ".cpp",
    "What character starts a tag in HTML?": "<",
    "What does URL stand for?": "locator",
    "What does Git help with?": "versioning",
    "What is a common hashing algorithm?": "sha256",
    "Which memory is faster than RAM?": "cache",
    "What does the 'return' keyword do in a function?": "exit",
    "What keyword is used to declare variables in Java?": "int",
    "What is used to uniquely identify a record in a database?": "primary",
    "Which database language is used for queries?": "sql",
    "Which Python keyword defines anonymous functions?": "lambda"
}



# to get answer we say questions["key"]  --> gives "Value"

def python_trivial_game():
    questions_list = list(questions.keys()) # list funcn makes a list of all keys in questions bcz of .keys() while .values() gives values
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list,total_questions)  # randomly select 5 questionsselecte randomly k questions from given list & return a LIST
    # print(selected_questions) checkpoint

    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your Answer: ").lower().strip() # .lower make answer lower case while .strip() remove any space in answers by useer

        if user_answer == questions[question] :
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {questions[question]}\n")

    print(f"\nYour final score is: {score}/{total_questions}")




python_trivial_game()