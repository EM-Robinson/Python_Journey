#Imports the random module

import random

print('Welcome to the team selector! \n')

#Begins while loop for team selector

while True:

    players = ['Gabriel Jesus','Gabriel Martinelli','Bukayo Saka','Oleksandr Zinchenko','Declan Rice','Kai Havertz',
           'Martin Odegaard','Aaron Ramsdale','Gabriel','William Saliba','Thomas Partey','Ben White',
           'Emile Smith Rowe','Leandro Trossard','Reiss Nelson','Jorginho','Tomiyasu','Mikel Arteta',
           'Thierry Henry','Cesc Fabregas','Van Persie','Eddie Nketiah']

#Shuffles list of players using shuffle() method

    random.shuffle(players)

#Indexing first 11 players in randomized list

    arsenal_red = players[0:11]

#Selects team captain at random from list of indexed players using the choice() method

    team_captain_red = random.choice(arsenal_red)

    print('Arsenal Red\'s team captain is ' + team_captain_red ,'!\n')

    print('Arsenal Red lineup: ' '\n')

#Iterates through player in list and displays their name

    for player in arsenal_red:
        print(player , '\n')

#Repeats process for Arsenal White

    arsenal_white = players[11:22]

    team_captain_white = random.choice(arsenal_white)

    print('Arsenal White\'s team captain is ' + team_captain_white ,'!\n')

    print('Arsenal White lineup: ' '\n')

    for player in arsenal_white:
        print(player , '\n')

    #Confirms if selected teams can be kept. If yes then the loop ends. If no then the loop re-randomizes teams

    confirmation = input('Are you happy with the teams selected?? Please respond y or n ?')
    if confirmation == 'y':
        break
