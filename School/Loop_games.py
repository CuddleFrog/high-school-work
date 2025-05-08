# Loop the game feature so that it keeps asking until they say no


from games import Rock
from games import GuessNum
from RPG import rpg


class Loop:
    def run(self):
        play = input("Do you want to play\n1(rock paper scissors)\n2(guess the number)\n3(RPG)   ")

        if play == "1":
            games = Rock()
            games.run()
            
        elif play == "2":
            games = GuessNum()
            games.run()

        elif play == "3":
            RPG = rpg()
            RPG.run()
            
        else:
            print("error write 1, 2 or 3")
            exit()




        

            