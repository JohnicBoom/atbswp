def spam():
    global eggs
    eggs = 'eggs in spam'
    spammy = 'spammy in spam'
    bacon()
    print('Spam eggs = ',eggs)
    print('spammy = ',spammy)
def bacon():
    ham = 101
    eggs = 'eggs in bacon'
    spammy = 'spammy in bacon'
    print('Bacon eggs = ',eggs)
    print('spammy = ',spammy)
eggs = 'global eggs'
spammy = 'global spammy'
spam()
print('Global eggs = ',eggs)
print('spammy = ',spammy)
