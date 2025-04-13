#!/usr/bin/env python3
# myMultiplicationQuiz.py - Write Your Own Multiplication Quiz

"""
To see how much PyInputPlus is doing for you, try re-creating the multipli-
cation quiz project on your own without importing it. This program will
prompt the user with 10 multiplication questions, ranging from 0 × 0 to
9 × 9. You’ll need to implement the following features:

* If the user enters the correct answer, the program displays “Correct!”
  for 1 second and moves on to the next question.
* The user gets three tries to enter the correct answer before the
  program moves on to the next question.
* Eight seconds after first displaying the question, the question is
  marked as incorrect even if the user enters the correct answer after
  the 8-second limit.
"""

# I started with the multiplation quiz code from the other project, and built it without pyinputplus

import random, time

numberOfQuestions = 10
correctAnswers = 0
maxTries = 3
maxTime = 8 # in seconds

for questionNumber in range(numberOfQuestions):
    # Pick two random numbers
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    product = num1 * num2
    
    # Create a prompt with our random numbers and the question number
    prompt = f'#{questionNumber + 1}: {num1} * {num2} = '
        
    # Initialize question limits
    startTime = time.time()
    tries = 0
    
    response = ''
    
    while True: #(response != product) and (startTime + 8 >= time.time()) and (tries < 3):
        # Input validation
        try:
            response = input(prompt)
            if response == "":
                print('Please enter a number.')
                continue
            response = int(response)
        except ValueError:
            print('Please enter a number.')
            continue
            
        # Check for correct answer
        if response == product:
            # Check we are within the time limit
            if startTime + maxTime <= time.time():
                print('That was correct, but you were out of time.')
                break
            else:
                correctAnswers += 1
                print('Correct!')
                time.sleep(1)
                break
        else:
            # Check we are within the time limit
            if startTime + maxTime <= time.time():
                print('That was incorrect, and you were out of time.')
                break
            else:
                tries += 1
                # Check for ability to continue
                if tries == maxTries:
                    print('Sorry, that was 3 tries.')
                    break
                else:
                    print('Incorrect, please try again.')
                
# Print the results
print(f'Score: {correctAnswers} / {numberOfQuestions}')