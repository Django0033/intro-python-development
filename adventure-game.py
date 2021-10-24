print()
print()
print('         #############################')
print('         #                           #')
print('         #      For the Kingdom      #')
print('         #                           #')
print('         #############################')
print()
print()
print('The orcs are terrorizing your people. ')
print('You, the King of Fiomar, have the power to save your kingdom.')
print()

while True:
    answer = input('Do you want to start your adventure? YES/NO: ').lower()
    if answer not in ('yes', 'no'):
        continue
    else:
        break

if answer == 'yes':
    print()
    answer = input('\
You are the King of Fiomar. You are awakened by a loud noise outside the gates\n\
of your castle. You look out the window and see a large number of orcish\n\
raiders on the road outside the castle.\n\n\
\
Your squire comes in with your sword and shield and helps you prepare for the\n\
battle. Men while, your guard commander comes in to brief you on the situation.\n\
Do you want to HEAR the briefing, GATHER your troops or RUSH into battle? \
').lower()

    while True:
        if answer not in ('hear', 'gather', 'rush'):
            answer = input('Please choose a valid option. HEAR/GATHER/RUSH ').lower()
            continue
        else:
            break
    
    if answer == 'hear': # 1.
        answer = input('\n\
The commander of the guard tells you that he\'s sorry he didn\'t wake you\n\
sooner but wanted to see your face as he was sending you to a deathly battle.\n\
"The orcs have surrounded the castle," he says, "we are their primary targets."\n\
Do you want to PUNISH the commander or FORGIVE him for this mistake? \
').lower()

        while True:
            if answer not in ('punish', 'forgive'):
                answer = input('Please choose a valid option. PUNISH/FORGIVE ').lower()
                continue
            else:
                break

        if answer == 'punish': # 1.1.
            answer = input('\n\
A guard manacle and enchain the commander. You hear a voice through your\n\
window: "The humans are weak. I can smell fear and weakness on them." Do you\n\
want to LOOK through the window or GO outside? \
').lower()

            while True:
                if answer not in ('look', 'go'):
                    answer = input('Please choose a valid option. LOOK/GO ').lower()
                    continue
                else:
                    break

            if answer == 'look': # 1.1.1.
                input('\n\
You look through your window and suddenly an arrow hits your chest. You feel a\n\
terrible pain and lose your balance. You fall through the window to your death\n\
and the orcs take control of your castle.\n\n\
GAME OVER\n\
(Hit ENTER to exit)\
')

            elif answer == 'go': # 1.1.2.
                input('\n\
You go outside and see the roaring battle. Your guards are fighting with all\n\
their might but the orcs are stronger. Suddenly you see a huge orc rushing\n\
towards you. It\'s the shaman of the orcs. He hits you with his club and sends\n\
you flying away. You hit the floor, something cracks inside you and you can\'t\n\
move anymore. The only thing that you can do is to see how the orcs take\n\
control of your castle.\n\
GAME OVER\n\
(Hit ENTER to exit)\
')

        elif answer == 'forgive': # 1.2.
            answer = input('\n\
You laugh, "It\'s nothing commander. I still remember my training. It was a\n\
wise man who trained me, who could have done it better?" The commander smiles\n\
and leaves the room. Do you want to WALK behind the commander or RUN outside? \
        ').lower()

            while True:
                if answer not in ('walk', 'run'):
                    answer = input('Please choose a valid option. WALK/RUN ').lower()
                    continue
                else:
                    break
            
            if answer == 'walk': # 1.2.1.
                input('\n\
You walk behind your commander taking your time. When you reach the outside,\n\
the orcs are waiting for you. All your guards are dead. You know that this is\n\
the end, the orcs take you as their prisoner and start the destruction of your\n\
castle.\n\
GAME OVER\n\
(Hit ENTER to exit)\
')

            elif answer == 'run': # 1.2.2.
                input('\n\
You run outside passing by the side of your commander. You see the\n\
battle at the doors of the castle and give the order to the archers\n\
to fire from the walls. The guards defeat the orcs at the gates and\n\
the reinforcements of the orcs run away from the arrows. You have won\n\
this battle.\n\
YOU WON!\n\
(Hit ENTER to exit)\
')

    elif answer == 'gather': # 2
        answer = input('\n\
You rush outside and assemble your troops. The entire town is there to help.\n\
Your squire stands by ready to carry anything you need. The guards are divided\n\
into groups of ten. Do you want to ENCOURAGE them or TELL them to run into the\n\
battle? \
').lower()

        while True:
            if answer not in ('encourage', 'tell'):
                answer = input('Please choose a valid option. ENCOURAGE/TELL ').lower()
                continue
            else:
                break

        if answer == 'encourage': # 2.1
            answer = input('\n\
"Ready men! Let\'s make them remember the terror they brought to Fiomar!" You\n\
march forth to meet the orcs. Do you want to MARCH in front of your men or RIDE\n\
your horse behind your troops? \
').lower()

            while True:
                if answer not in ('march', 'ride'):
                    answer = input('Please choose a valid option. MARCH/RIDE ').lower()
                    continue
                else:
                    break

            if answer == 'march': # 2.1.1
                input('\n\
You march in front of your men. Your men feel inspired by your mighty presence.\n\
You run towards tho orcs and your men start running behind you. The orcs feel\n\
fear in their dark hearts when they see your brave army. They flee away and you\n\
have protected your kingdom.\n\
YOU WON\n\
(Hit ENTER to exit)\
')

            elif answer == 'ride': # 2.1.2
                input('\n\
You ride your horse behind your man. Your men run into battle but they are\n\
confused without your presence between them. A lot of them die but the orcs\n\
start to flee away. You have won the battle but at what cost.\n\
YOU WON\n\
(Hit ENTER to exit)\
')

        elif answer == 'tell': # 2.2
            answer = input('\n\
“You need to charge the orcs, kill as many as you can, and break up their line\n\
to get through them,” you shout. The guards are hesitant to follow your\n\
orders.While you are guards still thinking, the orcs rush inside your castle.\n\
Do you want to ATTACK the orcs or go back inside the barracks? \
').lower()

            while True:
                if answer not in ('attack', 'go'):
                    answer = input('Please choose a valid option. ATTACK/GO ').lower()
                    continue
                else:
                    break
            
            if answer == 'attack': # 2.2.1
                input('\n\
You run towards the orcs and attack them with your sword. There are too many of\n\
them and when your troops get into battle, you are already crushed by the clubs\n\
of the orcs.\n\
GAME OVER\n\
(Hit ENTER to exit)\
')

            elif answer == 'go': # 2.2.2
                input('\n\
You go back inside the barracks and the orcs kill your army. You smell smoke\n\
and the flames start to roar all over the place. You know that this is the\n\
end.\n\
GAME OVER\n\
(Hit ENTER to exit)\
')

    elif answer == 'rush': # 3
        answer = input('\n\
You grab your sword and shield, and rush out of the barracks. The guards are\n\
ready for the orcs, with spears raised and shields held overhead. Do you want\n\
to ATTACK the orcs or LOOK for the orc leader? \
').lower()

        while True:
            if answer not in ('attack', 'look'):
                answer = input('Please choose a valid option. ATTACK/LOOK ').lower()
                continue
            else:
                break

        if answer == 'attack': # 3.1
            answer = input('\n\
You run towards the orcs and your army runs behind you. The battle roars and\n\
your brave army starts pushing back the orcs. They start to flee away. You have\n\
protected your kingdom.\n\
YOU WON\n\
(Hit ENTER to exit)\
').lower()

        elif answer == 'look': # 3.2
            answer = input('\n\
The battle starts and your men strike the orcs. You look for the orc leader,\n\
you find him and you kill him. The orcs get confused without a leader and they\n\
start to pull back. They are running away and your kingdom is safe for now.\n\
YOU WON\n\
(Hit ENTER to exit)\
').lower()

elif answer == 'no':
    print()
    print('Perhaps your people can handle this. Just go back to sleep.')
