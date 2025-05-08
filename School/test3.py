fights = ["punch", "kick"]

hp = 100
action = input(f"{fights} awnser 1 or 2     ")
if action == "1":
    print("you punch the monster")
    hp -= 10

elif action == "2":
    print("you kick the monster")
    hp -= 10
 

while hp < 30:
    print("monster dying")
    hp = 30
    
        
