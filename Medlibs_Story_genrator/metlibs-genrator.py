with open('story.txt', 'r') as file:
    story = file.read()

# print(story)

words = set()   # set have only unique value while can have repetation
start_of_word = -1

target_start = '<'
target_end = '>'

for i, char in enumerate(story): # enumerate gives index and element at it hence we are using 2 var i and char
    if char == target_start:
        start_of_word = i 

    if char == target_end and start_of_word != -1:
        words.add(story[start_of_word: i+1]) # i+1 because we want to include the end char as well
        start_of_word = -1

# print(words)

# answers = {'<name>': 'John',}

answers = {}

for word in words :
    answer = input('Enter a word for ' + word + ': ')
    answers[word] = answer

# print(answers)

for word in words:
    story = story.replace(word, answers[word])

print(story)

with open('genrated_story.txt', 'a') as file:
    file.write('\n' + story)
