import random
messages = ['It is certain',
            'It is decidedly so',
            'Yes, definitely',
            'Reply hazy. Try again',
            'Ask again later',
            'Concentrate and ask again',
            'No',
            'Outlook not so good',
            'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])