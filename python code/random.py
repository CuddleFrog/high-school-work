from rpg import RPG

error = "error write yes or no"



name = input("Hello user what is your name?   ")
if name == "":
    print("error write a name")
    exit()

else:
    print(f"Welcome {name}\nTo this brand new project.")

action1 = input("Do you enjoy games?\nyes\nno")
if action1 == "yes":
    print("Hooray let´s play an RPG!")
    rpg = RPG()
    rpg.run()

elif action1 == "no":
    print("Ooh that´s to bad.")
    exit()

else:
    print(error)

