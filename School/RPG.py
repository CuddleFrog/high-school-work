#RPG
# work on action 7 and complete it 
class rpg:
    def run(self):
        action1 = input("You find yourself in a lush forest with creatures lurking in every corner\n1(do you go right)\nor\n2(do you go to the left)  ")
        if action1 == "1":
            print("you walk to the right and after quite some time you hear water and whispers")
            
            action2 = input("Do you\n1(sneak towards the whispers)\nor\n2(do you make a run for it towards the sound of water)  ")

            if action2 == "1":
                print("You sneak towards the whispers and spot a group of elves talking around a campfire")

                action3 = input("Do you\n1(approch them)\nor\n2(ease drop into their conversation)  ")

                if action3 == "1":
                    print("You approch them and they instanniusly get on guard and un sheath their weapons")
                
                    action4 = input("Do you\n1(give up and surrender)\nor\n2(stand your ground and fight)  ")
                    

                    if action4 == "1":
                        print("You give up and surrender causing the elves to laugh hysterically")
                        
                        action5 = input("Do you\n1(start laughing with them)\nor\n2(walk away while they´re distracted)   ")
                        
                        if action5 == "1":
                            print("You start laughing with them causing them to stop laughing")
                            action6 = input("Do you\n1(continue to laugh)\nor\n2(ask them why they stopped laughing)  ")
                            
                            if action6 == "1":
                                print("You continue to laugh, in turn the elves give up on trying to capture you, because they feel creeped out")
                                action7 = input("Do you\n1(contiue to laugh)\nor\n2(stop laughing and ask why they stopped laughing)")

                                if action7 == "1":
                                    print("You continue to laugh causing them to reatreat by slowly walking away inch by inch")
                                    action8 = input()

                                
                                elif action7 == "2":
                                    print("You stop laughing and ask them why they stopped laughing, in respose they say that you are a creep for laughing in this situation")
                                    action8 = input()








                                else:
                                    print("error write 1 or 2")
                                    exit()
                                    




                            elif action6 == "2":
                                print("You ask them why they stopped laughing, they respond by saying that it´s creepy to laugh with them when you surrendered to them")
                                action7 = input("Do you\n1(insult them)\nor\n2(ask them if they give up on trying to capture you)")

                                if action7 == "1":
                                    print("You insult them by saying that they are a joke thats why you are laughing")
                                    action8 = input()








                                
                                elif action7 == "2":
                                    print("You ask them if they give up on trying to capture you and they nod their heads in unison while looking creeped out")
                                    action8 = input()









                                else:
                                    print("error write 1 or 2")
                                    exit()




                            
                            else:
                                print("error write 1 or 2")
                                exit()

                        


                        elif action5 == "2":
                            print("You silently walk away while they´re to ocuppied laughing")
                            action6 = input("Do you\n1(keep walking away)\nor\n2(do a silly dance while walking away)  ")

                            if action6 == "1":
                                print("You keep tip toeing away and slip away into a mysterious dark cavern")
                                action7 = input("Do you\n1(continue your way in)\nor\n2(go back towards the elves)")


                                if action7 == "1":
                                    print("You continue your tip toeing further into the cave, while hearing something strange following you")
                                    action8 = input()







                                elif action7 == "2":
                                    print("You squirm back to the eleves beacuse you were to scared of the dark cavern and rather deal with kidnappers instead of some random mysterious cavern")
                                    action8 = input()





                                else:
                                    print("error write 1 or 2")
                                    exit()    


                            

                            elif action6 == "2":
                                print("You do a silly chicken dance while wobbling around, causing the elves to burst into tears laughing and then collapsing out of exaustion")
                                action7 = input("Do you\n1(walk away)\nor\n2(tie them up)")

                                if action7 == "1":
                                    print("After causing the elves to collapse out of exaustion, you walk away with cool sun glasses like there´s a cool explotion behind you")
                                    print("BOOOM!")
                                    print("The end")
                                    print("Thank you for playing :)")
                                    exit()


                                elif action7 == "2":
                                    print("You somehow tie them up with your make shift rope make out of grass, sticks and leaves")
                                    print("One the elves sleep talks and says that your weird like that and then instantly falls asleep again")
                                    action8 = input()






                            
                            else:
                                print("error write 1 or 2")
                                exit()




                    


                    elif action4 == "2":
                        print("You stand your ground and make the fisrt move by kicking one of the eleves on their chest causing him to vomit out blood")

                        action5 = input("Do you\n1(punch the same elf)\nor\n2(kick another elf)  ")


                        if action5 == "1":
                            print("You procced to punch the same elf so hard he flies back and is knocked unconcious")
                            action6("Do you\n1(continue to pummel the same elf)\nor\n2(turn to fight the other eleves)  ")

                            if action6 == "1":
                                print("You continue to oblidirate the elf into a rainbow cotten candy pulp, but somehow he´s still alive and breathing.......(thankfully)")
                                action7 = input("Do you\n1(eliminate him)\nor\n2(spare his life)")
                                if action7 == "1":
                                    print("You are just about to eliminate him but right before you get the finnishing blow.......you wake up from your dream")
                                    print("thank you for playing")
                                    print("You are either sadistic or have a mest up sens of humor or you are complitely normal and somehow got to this ending either way thank you so much for playing :) ")
                                    exit()

                                

                                elif action7 == "2":
                                    print("You the strong and responsible person that you are spares his pitiful life")
                                    print("Thank you for playing and being a good person according to society")
                                    print("Bye bye :) ")
                                    exit()

                                
                                else:
                                    print("error write 1 or 2")
                                    exit()
                                



                            

                            elif action6 == "2":
                                print("You turn around your face covered in passion and rage, causing the other elf to get stunned locked while you destroy him in a one sided fight")
                                action7 = input("Do you\n1(continue to destroy him)\nor\n2(knock him out)")


                                if action7 == "1":
                                    print("You continue to destroy him in a one sided fight causing him to be pummeled to a pulp")
                                    action8 = input()



                                
                                elif action7 == "2":
                                    print("You spare him the pain and cleanly knock him out in one chop")
                                    action8 = input()








                                else:
                                    print("error write 1 or 2")
                                    exit()

                            

                            else:
                                print("error write 1 or 2")
                                exit()
                        
                            




                        
                        elif action5 == "2":
                            print("You instantainously turn around and kick another elf causing him to fume up foam from his mouth and gets knocked out cold")
                            action6("Do you\n1(turn to fight the other evles)\nor\n2(make a run for it)  ")

                            if action6 == "1":
                                print("You turn around to fight the other eleves, in a dramatic and cinematic fight")
                                action7 = input("Do you\n1(use you special technic)\nor\n2(use you ultimate ability)")
                                
                                




                            
                            elif action6 == "2":
                                print("You make a run for it into deeper into the forest, until you stumble into a lake")
                                action7 = input("Do you\n1(swim out)\nor\n2(dive down)")






                            

                            else:
                                print("error write 1 or 2")
                                exit()                            





                        else:
                            print("error write 1 or 2")
                            exit()




                    else:
                        print("error write 1 or 2")
                        exit()

                elif action3 == "2":
                    print("You listen in to their conversation and discover that they are hunting humans")

                    action4 = input("Do you\n1(run away)\nor\n2(fight them)  ")
                    
                    if action4 == "1":
                        print("You sneakly run away without a sound")

                        action5 = input("You find a village do you\n1(approch it) or\n2(keep running)  ")
                        
                        if action5 == "1":
                            print("You approch the village and you are greeted by a group of rowdy dwarves wecloming you warmly")
                            action6 = input("Do you\n1(greet them formally)\nor\n2(greet them aggressively)  ")

                            if action6 == "1":
                                print("You greet them formally, causing them to burst into laugther, telling you that you shouldn't be so formal around these parts")
                                action7 = input("")





                            

                            elif action6 == "2":
                                print("You greet them aggressively, causing them to greet you even more warmly.")
                                action7 = input("")
                            
                            else:
                                print("error write 1 or 2")
                                exit()
                        



                        elif action5 == "2":
                            print("You keep running and find a massive cavern")
                            action6 = input("Do you\n1(enter the mysterious cavern)\nor\n2(turn aroundand head back to the village)  ")

                            if action6 == "1":
                                print("You enter the mysterious cavern and discover that it's filled with a gorgeous crystal forest")
                                action7 = input("")
                            

                            elif action6 == "2":
                                print("You decide to turn around and go back to the village, but on the way you are ambushed by a group of elves")
                                action7 = input("")
                            

                            else:
                                print("error write 1 or 2")
                                exit()







                        else:
                            print("error write 1 or 2")
                            exit()




                    elif action4 == "2":
                        print("You conduct a sneak attack on one of the elves from behind causing them to fall unconscious")
                        action5 = input("Do you\n1(silenty knock another elf out)\nor\n2(make it loud and go all out)  ")

                        if action5 == "1":
                            print("You knock out another elf, by whispering sweet nothings into his ear causing him to fall asleep")
                            action6 = input("Do you\n1(silently knock out yet another elf)\nor\n2(make it go boom!)")
                            




                        elif action5 == "2":
                            print("You go all out and fight them in an amazing cinematic fight scene")
                            action6 = input("Some still reamain standing after the furocious battle. Do you\n1(continue the battle)\nor\n2(suggest a surrender from the elves)")

                        



                        else:
                            print("error write 1 or 2")
                            exit()



                    else:
                        print("error write 1 or 2")
                        exit()

                else:
                    print("error write 1 or 2")
                    exit()


            
            elif action2 == "2":
                print("You make a run for it an dash towards the water, but you accidentally fall into a lake")

                action3 = input("Do you\n1(dive down deeper) or\n2(swim up)  ")

                if action3 == "1":
                    print("You dive down deeper and discover an underground cavern")
                
                    action4 = input("Do you\n1(dive even deeper) or\n2(swim up to the surface)  ")

                    if action4 == "1":
                        print("You dive deeper and find an air pocket to rest in before finding a massive ancient looking door")

                        action5 = input("Do you\n1(approch it) or\n2(try finding your way out)  ")

                        if action5 == "1":
                            print("You approch the door and it greets you by saying you shall pass if you are worthy")
                            action6 = input("Do you show your worth by\n1(do a silly dance)\nor\n2(ignore the door)")





                        
                        elif action5 == "2":
                            print("You swim up trying to find a way out but instead it´s pich black and you are starting to fall unconcious")
                            action6 = input("Do you\n1(hold your breath)\nor\n2(breath in and out slowly)")

                        




                        else:
                            print("error write 1 or 2")
                            exit()


                    
                    elif action4 == "2":
                        print("While swiming back up to the surface you suddenly get struck by a massive creature")

                        action5 = input("Do you\n1(grip onto it)\nor\n2(punch it)  ")

                        if action5 == "1":
                            print("You grip onto to it by digging your nails into it´s skin causing it to roar out in pain")
                            action6= input("Do you\n1(continue to hold onto the creature)\nor\n2(let go)")
                        




                        elif action5 == "2":
                            print("You somehow manage to punch it under water and it screams out in an agonizing screetch")
                            action6 = input("Do you\n1(continue to engage in battle)\nor\n2(take a big bite off the creature)\nor\n3(try to have a conversation with the creature)")


                        



                        else:
                            print("error write 1 or 2")
                            exit()


                    
                    else:
                        print("error write 1 or 2")
                        exit()


                elif action3 == "2":
                    print("You swim upwards and climb up onto land and see a gigantic monster swiming past")

                    action4 = input("Do you\n1(attack the monster)\nor\n2(let it swim past you)  ")
                    
                    if action4 == "1":
                        print("You attack the monster by throwing a head sized rock onto it causing it to roar out in agony")

                        action5 = input("Do you\n1(throw another rock)\nor\n2(throw a sharp stick)  ")


                        if action5 == "1":
                            print("You pick up another larger rock and fling it onto the creature causing it to laugh histeracally")
                            action6 = input("Do you\n1(ask why it's laughing)\nor\n2(continue to throw objects at it)")
                        



                        elif action5 == "2":
                            print("You pick up a sharp stick and fling it onto the creature, puncturing it´s skin and causing it to bleed and roar in agony")
                            action6 = input("Do you\n1(start laughing at the creature)\nor\n2(continue to bombared the creature with random things you find from the forest)")

                        




                        else:
                            print("error write 1 or 2")
                            exit()
                    



                    elif action4 == "2":
                        print("You wait until it passes by quietly")

                        action5 = input("It swims past while whistling (Rick Astley (Never Gonna Give You Up))")
                        print("You got Rick rolled HARD, causing you to surrender to the forces of evil and into deep slumber....The end.")
                        print("Thank you for playing :)")
                        exit()
                    


                    else:
                        print("error write 1 or 2")
                        exit()

                else:
                    print("error write 1 or 2")
                    exit()



            else:
                print("error, input 1 or 2")
                exit()



        elif action1 == "2":
            print("You walk to the left and after a few minutes you find a village")

            action2 = input("Do you\n1(go towards the village)\nor\n2(walk past)  ")
            if action2 == "1":
                print("You enter the village and you are greeted by welcoming dwarves")

                action3 = input("Do you\n(greet them respectfully)\nor\n2(agressivly)  ")

                if action3 == "1":
                    print("You greet them respctfully by bowing and greeting them")

                    action4 = input("They dislike that and are getting ready to fight, do you\n1(fihgt back)\nor\n2(surrender)  ")

                    if action4 == "1":
                        print("You fight back by headbuttting one of the dwarves causing them to fall back unconcious")

                        action5 = input("Do you\n1(brawl it out)\nor\n2(intimidate them by roaring out)  ")


                        if action5 == "1":
                            print("You brawl it out causing them to smile and laugh while fighting you")
                            action6 = input("Do you\n1(continue)\nor\n2(stop and ask why)")

                        


                        elif action5 == "2":
                            print("You roar out but the only thing that comes out of your mouth is a small cute squick, they all start to laugh at you histerically")
                            action6 = input("Do you\n1(try again)\nor\n2(just fight them head on)")

                        





                        else:
                            print("error write 1 or 2")
                            exit()



                    
                    elif action4 == "2":
                        print("You surrender causing them to look disapointed and knocks you out cold.......")
                        print("You fell into a deep slumber never to wake up again, the end......")
                        print("Thank you for playing :)")
                        exit()


                elif action3 == "2":
                    print("You punch one of the dwarves and then greet them")

                    action4 = input("They like your attitude and offer to take you to their village cheif, do you\n1(except)\nor\n2(decline)  ")
                    if "1":
                        print("You except and they take you to the cheif, the cheif is a massive ancient golem")
                        action5 = input("The golem says that you must find a massive ancient looking door in order for you to escape this nightmare, before the elves do. Do you\n1(listen to the advice of the cheif)\nor\n2(do you bad mouth him)  ")

                        if action5 == "1":
                            print("You for some strange reason listen to and agree to follow his advice, he points towards two portals one is red and one is blue")
                            action6 = input("Do you\n1(enter the red protal)\nor\n2(enter the blue portal)")


                        



                        elif action5 == "2":
                            print("You bad mouth the giant golem by saying, f*****g b***h a** giant pile of rock why should I listen to you?, the golem is flabbergasted")
                            action6 = input("Do you\n1(continue to inslut the golem)\nor\n2(apologize)")


                        




                        else:
                            print("error write 1 or 2")
                            exit()





                    elif action4 == "2":
                        print("You decline their offer and they seem dissapointed but welcome you to an inn instead")
                        action5 = input("Do you\n1(ask how much it costs to stay for one night)\nor\n2(ask how much it costs for a cup of chai)  ")


                        if action5 == "1":
                            print("You ask how much it costs to stay a night and they start laughing uncontrollably")
                            action6 = input("Do you\n1(ask why they are laughing)\nor\n2(start a bar fight)")

                        



                        elif action5 == "2":
                            print("You ask how much a cup of tea costs and they reply 5 /*;,.:/'*")
                            action6 = input("Do you\n1(ask what  /*;,.:/'* is)\nor\n2(give them what you think is 5 /*;,.:/'*)")


                        



                        else:
                            print("error write 1 or 2")
                            exit()


                       
                    else:
                        print("error write 1 or 2")
                        exit()


                else:
                    print("error write 1 or 2")
                    exit()




            elif action2 == "2":
                print("You walk past the village and find a massive cavern")

                action3 = input("Do you\n1(enter the mysterious cavern)\nor\n2(turn back to the village)  ")
                
                if action3 == "1":
                    print("You enter the mysterious cavern and discover a gorgeous crystal covered forest")

                    action4 = input("Do you\n1(move in deeper)\nor\n2(set up camp)  ")
                    if action4 == "1":
                        print("You wander deeper into the beautiful cavern and spot a massive ancient looking door")
                        action5 = input("Do you\n1(approch it)\nor\n2(turn around and walk away)  ")

                        if action5 == "1":
                            print("You approch the door and it greets you by saying, you must prove you are worthy to pass through")
                            
                            # write 3 actions for this one, one that says "I am worthy because you are a figment of my reality"
                            action6 = input("Do you\n1(prove it by doing a silly dance)\nor\n2(prove it by puling out excalibur)\nor\n3(say, I am worthy because you are a figment of my reality)")


                        



                        elif action5 == "2":
                            print("You turn around and start leaving, but suddenly the door says, wait don´t leave me!")
                            action6 = input("Do you\n1(turn around)\nor\n2(keep walking and ignoreing the door)")







                        


                        else:
                            print("error write 1 or 2")
                            exit()




                    
                    elif action4 == "2":
                        print("You set up a small camp fire and a make shift tent, while setting up you hear somthing coming towards you with light steps")
                        action5 = input("Do you\n1(find cover to hide behind)\nor\n2(wait to face it, face to face)  ")

                        if action5 == "1":
                            print("You find cover behind a massive crystal")
                            action6 = input("Do you\n1(peek around the corner)\nor\n2(keep hiding)")



                        


                        elif action5 == "2":
                            print("You wait and wait until finally a small cute frog jumps out from around the corner")
                            action6 = input("Do you\n1(greet it)\nor\n2(get ready for battle)")






                        else:
                            print("error write 1 or 2")
                            exit()



                    else:
                        print("error write 1 or 2")
                        exit()    


                elif action3 == "2":
                    print("You turn back to the village but you get ambushed by a group of elves")

                    action4 = input("Do you\n1(ready up for a fight)\nor\n2(pretend not to notice them)  ")
                    if action4 == "1":
                        print("You raise your fists and upper cut one of the elves so hard causing a tooth to fly out")
                        action5 = input("Do you\n1(punch the same elf)\nor\n2(kick another elf)  ")

                        if action5 == "1":
                            print("You punch the elf again this time harder on his stomach, causing him to spit out blood and falls unconcious")
                            action6 = input("Do you\n1(continue to beat up the same knocked out elf)\nor\n2(turn to fight the next elf)")
                            
                        


                        elif action5 == "2":
                            print("You turn around and kick an elf but you acidentally kick them on their crotch causing him to pass out cold")
                            action6 = input("Do you\n1(apologize)\nor\n2(turn to fight the next elf)")

                        



                        else:
                            print("error write 1 or 2")
                            exit()




                    elif action4 == "2":
                        print("You pretend not to notice the eleves and they are prepelexed, they try to gain your attention but fails and give up on bothering you")
                        action5 = input("Do you\n1(keep walking away)\nor\n2(turn around and do a silly greeting)  ")
                        

                        if action5 == "1":
                            print("You keep walking away until you lose sight of them")
                            action6 = input("Do you\n1(keep walking away)\nor\n2(double back)")


                        

                        elif action5 == "2":
                            print("You turn around and flex your biceps and say, Howdy dooby dooo partners!")
                            print("The elves become even more appalled whenn you do you hilarious and dumbe greeting and begin to laugh uncontrollably.")
                            action6 = input("Do you\n1(continue your greeting)\nor\n2(do a idiotic dance)")
                        



                        else:
                            print("error write 1 or 2")
                            exit()



                    else:
                        print("error write 1 or 2")
                        exit()
            


                else:
                    print("error write 1 or 2")
                    exit()

            else:
                print("error, input 1 or 2")

        else:
            print("error, input 1 or 2")
            exit()

