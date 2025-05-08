from games import Rock
from games import GuessNum
from RPG import rpg
from Loop_games import Loop

# Name
name = input("What is your name?  ")
bot_name = "Brian"
if name == "Brian":
    print("Woow we have the exact same name.")
elif name == "":
    print("error please enter a name next time.")
    exit()

else:
    print(f"Hello {name}, my name is {bot_name}.")


# Age and age diffrence
age = input("How old are you?  ")
bot_age = 17
age_diffrence = int(age) - bot_age

if int(age) < bot_age:
    print(f"You are younger than me, you are {age} years old while I am {bot_age} years old.")

elif int(age) > 18:
    print(f"Wow if you are {age} years old and I am {bot_age} years old, then we are {age_diffrence} years apart.")

elif int(age) == bot_age:
    print(f"Wooow we are the exact same age, {bot_age} years old")

elif int(age) == 18:
    print(f"If you are {age} and I am {bot_age} then we are {age_diffrence} year apart")
else:
    print("error please enter an age in numbers next time")
    exit()


# Avrage grade F - A

grade = input("What is your average grade (A, B, C, D, E, F)  ")

if grade == "A":
    print("Wooow That is amazing")
elif grade == "a":
    print("Wooow That is amazing")

elif grade == "B":
    print("That is really good")

elif grade == "b":
    print("That is really good")

elif grade == "C":
    print("Keep up the good work")
elif  grade == "c":
    print("Keep up the good work")

elif grade == "D":
    print("That is pretty good")

elif grade == "d":
    print("That is pretty good")
elif grade == "E":
    print("At least it is a passing grade")
elif grade == "e":
    print("At least it is a passing grade")

elif grade == "F":
    print("Damn that sucks, I sincerly wish the best for you")
elif grade == "f":
    print("Damn that sucks, I sincerly wish the best for you")

else:
    print("error write a letter That is within ()")
    exit()

# Are you still a student
is_student = input("Are you still a student, (yes, no)  ")
if is_student == "yes":
    print("Wow I wish you good luck in your studies")
elif is_student == "Yes":
    print("Wow I wish you good luck in your studies")
elif is_student == "no":
    print("I see then I sincerely wish you good luck in life ahead")
elif is_student == "no":
    print("I see then I sincerely wish you good luck in life ahead")
else:
    print("error write one of the awnsers in () next time")
    exit()

# 









# Are you bored
bored = input("Are you bored right now if\n(yes) then let`s play a game\nif\n(no) then let´s play another time?  ")
if bored == "yes":
    print("Ok lets have some fun")
elif bored == "no":
    print("Oh that´s to bad maybe we can play next time")
    exit()
elif bored =="Yes":
    print("Ok let´s play")

elif bored == "No":
    print("Oh that´s to bad let´s play some other time")
    exit()
else:
    print("Awnser yes or no next time")
    exit()


# Do you want to play a game
game = input("Do you want to play\n1 (rock paper scissors)\n2 (guess the number)\n3 (RPG)   ")

if game == "2":
    games = GuessNum()
    games.run()


elif game == "1":
    games = Rock()
    games.run()

elif game == "3":
    RPG = rpg()
    RPG.run()

else:
    print("error write 1, 2 or 3")
    exit()




# I want to loop the "do you want to play again funcion" from another file called Loop_games.py 

play = input("Do you still want to play (yes) or (no)?   ")

if play == "yes":
    print("Yay let´s play!")
    Loop_games = Loop()
    Loop_games.run()

elif play == "no":
    print(f"Ok see you next time\n{name}")
    exit()
elif play == "Yes":
    print("Yay let´s play!")
    Loop_games = Loop()
    Loop_games.run()
elif play == "No":
    print(f"Ok see you next time\n{name}")
    exit()

else:
    print("error write yes or no")
    exit()

play = input("Do you still want to play (yes) or (no)?   ")

if play == "yes":
    print("Yay let´s play!")
    Loop_games = Loop()
    Loop_games.run()

elif play == "no":
    print(f"Ok see you next time\n{name}")
    exit()
elif play == "Yes":
    print("Yay let´s play!")
    Loop_games = Loop()
    Loop_games.run()
elif play == "No":
    print(f"Ok see you next time\n{name}")
    exit()

else:
    print("error write yes or no")
    exit()

play = input("Do you still want to play (yes) or (no)?   ")

if play == "yes":
    print("Yay let´s play!")
    Loop_games = Loop()
    Loop_games.run()

elif play == "no":
    print(f"Ok see you next time\n{name}")
    exit()
elif play == "Yes":
    print("Yay let´s play!")
    Loop_games = Loop()
    Loop_games.run()
elif play == "No":
    print(f"Ok see you next time\n{name}")
    exit()

else:
    print("error write yes or no")
    exit()


play = input("Do you still want to play (yes) or (no)?   ")

if play == "yes":
    print("Yay let´s play!")
    Loop_games = Loop()
    Loop_games.run()

elif play == "no":
    print(f"Ok see you next time\n{name}")
    exit()
elif play == "Yes":
    print("Yay let´s play!")
    Loop_games = Loop()
    Loop_games.run()
elif play == "No":
    print(f"Ok see you next time\n{name}")
    exit()

else:
    print("error write yes or no")
    exit()




print("Thank you for trying this code")
exit()

