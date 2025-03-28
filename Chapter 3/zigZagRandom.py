import time, sys, random

indent = 0 
indentEnd = 20

indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)
        if indentIncreasing:
            indent = indent + 1
            if indent >= indentEnd:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == indentEnd - 20 or indent == 0:
                indentIncreasing = True
                indentEnd = random.randint(10,40)
                if indent > indentEnd:
                    indentEnd = indentEnd + 10
except KeyboardInterrupt:
    sys.exit()