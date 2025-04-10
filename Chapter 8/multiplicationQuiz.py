import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # Pick two random numbers
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    product = num1 * num2
    # Create a prompt with our random numbers and the question number
    prompt = f'#{questionNumber}: {num1} * {num2} = '
    try:
        # Right answers are handled by allowRegexes
        # Wrong answers are handeled by blockRegexes, with a custom message
        pyip.inputStr(prompt, allowRegexes=[f'^{product}$'], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block
       print('Correct!')
       correctAnswers += 1
    # Brief pause to let the user see the result
    time.sleep(2)
print(f'Score: {correctAnswers} / {numberOfQuestions}')

