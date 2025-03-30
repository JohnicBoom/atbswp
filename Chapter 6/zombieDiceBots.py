#!/usr/bin/env python3
# zombieDiceBots.py -

"""Programming games are a game genre where instead of playing a game
directly, players write bot programs to play the game autonomously.
I’ve created a Zombie Dice simulator, which allows programmers to
practice their skills while making game-playing AIs. Zombie Dice bots
can be simple or incredibly complex, and are great for a class
exercise or an individual programming challenge.

Zombie Dice is a quick, fun dice game from Steve Jackson Games. The
players are zombies trying to eat as many human brains as possible
without getting shot three times. There is a cup of 13 dice with
brains, footsteps, and shotgun icons on their faces. The dice icons
are colored, and each color has a different likelihood of each event
occurring. Every die has two sides with footsteps, but dice with
green icons have more sides with brains, red-icon dice have more
shotguns, and yellow-icon dice have an even split of
brains and shotguns. Do the following on each player’s turn:

    1. Place all 13 dice in the cup. The player randomly draws three
    dice from the cup and then rolls them. Players always roll exactly
    three dice.
    
    2. They set aside and count up any brains (humans whose brains
    were eaten) and shotguns (humans who fought back). Accumulating
    three shotguns automatically ends a player’s turn with zero points
    (regardless of how many brains they had). If they have between
    zero and two shotguns, they may continue rolling if they want.
    They may also choose to end their turn and collect one point
    per brain.
    
    3. If the player decides to keep rolling, they must reroll all
    dice with footsteps. Remember that the player must always roll
    three dice; they must draw more dice out of the cup if they have
    fewer than three footsteps to roll. A player may keep rolling dice
    until either they get three shotguns — losing everything — or all
    13 dice have been rolled. A player may not reroll only one or two
    dice, and may not stop mid-reroll.
    
    4. When someone reaches 13 brains, the rest of the players finish
    out the round. The person with the most brains wins. If there’s a
    tie, the tied players play one last tiebreaker round.

Zombie Dice has a push-your-luck game mechanic: the more you reroll
the dice, the more brains you can get, but the more likely you’ll
eventually accrue three shotguns and lose everything. Once a player
reaches 13 points, the rest of the players get one more turn
(to potentially catch up) and the game ends. The player with the most
points wins.

See the PDF for more... lots more!"""


import zombiedice

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break



zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    MyZombie(name='JohnicZombie')
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)

"""
Shotgun = S, Brains = B, Footsteps = F

3 red dice - S more likely		3S 2F 1B	0.5 0.333 0.167
4 yellow dice - B & S even		2S 2F 2B	0.333
6 green dice - B more likely	1S 2F 3B	0.167 0.333 0.5

I want my zombie to basically work like the "stop at 2 shotguns"
zombie. However, mine will choose to act based on the dice available.

Since we know the spread of dice in the cup, we can know the chances
of rolling a S.

To make a roll decision, I need to

"""