"""
This is a silly name generator game which will allow a user to randomly select
 a first and last name from two tuple lists.
"""

import sys
import random

"""Choose names randomly from 2 tuples of names that will print to the screen"""

print("\nWelcome to the Random Name Generator!")
print("Your name comes from the Psych show which Sean would pick for Gus.\n")

#  tuple for first name
first_name = (
    'Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'", "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder',
    "Bud 'Lite'", 'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield', 'Chewy', 'Chigger', 'Cinnabuns',
    'Cleet', 'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso', 'Fancypants',
    'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'",
    'Johnny', 'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid', "Mr Peabody", 'Oil-Can', 'Oinks',
    'Old Scratch', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet', 'Rock Candy', 'Schlomo',
    'Scratchensniff', 'Scut', "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam',
    'Spritzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe', "Winston 'Jazz Hands'",
    "Worms"
)

# tuple for last name
last_name = (
    'Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom', 'Breedslovetrout', 'Butterbaugh', 'Clovenhoof',
    'Clutterbuck','Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith', 'Goodpasture', 'Guster',
    'Henderson', 'Hooperbag', 'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
    'Kingfish', 'Listenbee', "M'Bembo'", 'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti', 'Outerbridge',
    'Overpeck', 'Overturf', 'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins',
    'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern', 'Stevens',
    'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins', 'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger',
    'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn', 'Woolysocks'
)

print("Ready to play?")
print("type 'q' for quit, enter to begin game")

user_input = input()
while user_input.lower() != 'q':
    first_silly_name = random.choice(first_name)  # uses random method
    last_silly_name = random.choice(last_name)

    print(f"\t{first_silly_name} {last_silly_name}\n", file=sys.stderr)  # file used for error red color text
    user_input = input("type 'q' for quit, enter to keep playing\n")

#  outside of loop
if user_input.lower() == 'q':
    print("\nThanks for playing, hope you enjoyed your silly name!")

