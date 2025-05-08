#RPG
class RPG:
    def run(self):
        action1 = input("You find yourself in a lush forest with creatures lurking in every corner\n1(do you go right) or\n2(do you go to the left)  ")
        if action1 == "1":
            print("you walk to the right and after quite some time you hear water and whispers")
            
            action2 = input("Do you\n1(sneak towards the whispers) or\n2(do you make a run for it towards the sound of water)  ")

            if action2 == "1":
                print("You sneak towards the whispers and spot a group of elves talking around a campfire")

                action3 = input("Do you\n1(approch them) or\n2(ease drop into their conversation)  ")

                if action3 == "1":
                    print("You approch them and they instanniusly get on guard and un sheath their weapons")
                
                    action4 = input("Do you\n1(give up and surrender) or\n2(stand your ground and fight)  ")
                    

                    if action4 == "1":
                        print("You give up and surrender causing the elves to laugh hysterically")
                        
                        action5 = input("Do you\n1(start laughing with them) or\n2(walk away while they´re distracted)   ")
                        
                        if action5 == "1":
                            print("You start laughing with them causing them to stop laughing")
                            action6 = input("Do you\n1(continue to laugh) or\n2(ask them why they stopped laughing)  ")
                            




                        


                        elif action5 == "2":
                            print("You silently walk away while they´re to ocuppied laughing")
                            action6 = input("Do you\n1(keep walking away) or\n2(do a silly dance while walking away)  ")





                    


                    elif action4 == "2":
                        print("You stand your ground and make the fisrt move by kicking one of the eleves on their chest causing him to vomit out blood")

                        action5 = input("Do you\n1(punch the same elf) or\n2(kick another elf)  ")


                        if action5 == "1":
                            print("You procced to punch the same elf so hard he flies back and is knocked unconcious")
                            action6("Do you\n1(continue to pummel the same elf) or\n2(turn to fight the other eleves)  ")






                        
                        elif action5 == "2":
                            print("You instantainously turn around and kick another elf causing them to fume up foam from his mouth and gets knocked out cold")
                            action6("Do you\n1(turn to fight the other evles) or\n2(make a run for it)  ")








                        else:
                            print("error write 1 or 2")
                            exit()




                    else:
                        print("error write 1 or 2")
                        exit()

                elif action3 == "2":
                    print("You listen in to their conversation and discover that they are hunting humans")

                    action4 = input("Do you\n1(run away) or\n2(fight them)  ")
                    
                    if action4 == "1":
                        print("You sneakly run away without a sound")

                        action5 = input("You find a village do you\n1(approch it) or\n2(keep running)  ")
                        
                        if action5 == "1":
                            print("You approch the village and you are greeted by a group of rowdy dwarves wecloming you warmly")
                            action6("Do you\n1(greet them formally) or\n2(greet them aggressively)  ")

                        



                        elif action5 == "2":
                            print("You keep running and find a massive cavern")
                            action6("Do you\n1(enter the mysterious cavern) or\n2(turn aroundand head back to the village)  ")






                        else:
                            print("error write 1 or 2")
                            exit()




                    elif action4 == "2":
                        print("You conduct a sneak attack on one of the elves from behind causing them to fall unconscious")
                        action5 = input("Do you\n1(silenty knock another elf out) or\n2(make it loud and go all out)  ")

                        if action5 == "1":
                            print("You knock out another elf, by whispering sweet nothings into his ear causing him to fall asleep")
                            action6("")
                        


                        elif action5 == "2":
                            print("You go all out and fight them in an amazing cinematic fight scene")
                            action6("")
                        



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
                            action6("")




                        
                        elif action5 == "2":
                            print("You swim up trying to find a way out but instead it´s pich black and you are starting to fall unconcious")
                            action6("")
                        




                        else:
                            print("error write 1 or 2")
                            exit()


                    
                    elif action4 == "2":
                        print("While swiming back up to the surface you suddenly get struck by a massive creature")

                        action5 = input("Do you\n1(grip onto it) or\n2(punch it)  ")

                        if action5 == "1":
                            print("You grip onto to it by digging your nails into it´s skin causing it to roar out in pain")
                            action6("")
                        




                        elif action5 == "2":
                            print("You somehow manage to punch it under water and it screams out in an agonizing screetch")
                            action6("")
                        



                        else:
                            print("error write 1 or 2")
                            exit()


                    
                    else:
                        print("error write 1 or 2")
                        exit()


                elif action3 == "2":
                    print("You swim upwards and climb up onto land and see a gigantic monster swiming past")

                    action4 = input("Do you\n1(attack the monster) or\n2(let it swim past you)  ")
                    
                    if action4 == "1":
                        print("You attack the monster by throwing a head sized rock onto it causing it to roar out in agony")

                        action5 = input("Do you\n1(throw another rock) or\n2(throw a sharp stick)  ")


                        if action5 == "1":
                            print("You pick up another larger rock and fling it onto the creature causing it to laugh histeracally")
                            action6("")
                        



                        elif action5 == "2":
                            print("You pick up a sharp stick and fling it onto the creature, puncturing it´s skin and causing it to bleed and roar in agony")
                            action6("")
                        




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

            action2 = input("Do you\n1(go towards the village) or\n2(walk past)  ")
            if action2 == "1":
                print("You enter the village and you are greeted by welcoming dwarves")

                action3 = input("Do you\n(greet them respectfully) or\n2(agressivly)  ")

                if action3 == "1":
                    print("You greet them respctfully by bowing and greeting them")

                    action4 = input("They dislike that and are getting ready to fight, do you\n1(fihgt back) or\n2(surrender)  ")

                    if action4 == "1":
                        print("You fight back by headbuttting one of the dwarves causing them to fall back unconcious")

                        action5 = input("Do you\n1(brawl it out) or\n2(intimidate them by roaring out)  ")


                        if action5 == "1":
                            print("You brawl it out causing them to smile and laugh while fighting you")
                            action6("")
                        


                        elif action5 == "2":
                            print("You roar out but the only thing that comes out of your mouth is a small cute squick")
                            action6("")
                        





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

                    action4 = input("They like your attitude and offer to take you to their village cheif, do you\n1(except) or\n2(decline)  ")
                    if "1":
                        print("You except and they take you to the cheif, the cheif is a massive ancient golem")
                        action5 = input("The golem says that you must find a massive ancient looking door in order for you to escape this nightmare, before the elves do. Do you\n1(listen to the advice of the cheif) or\n2(do you bad mouth him)  ")

                        if action5 == "1":
                            print("You for some strange reason listen to and agree to follow his advice, he points towards two portals one is red and one is blue")
                            action6("")
                        



                        elif action5 == "2":
                            print("You bad mouth the giant golem by saying, f*****g b***h a** giant pile of rock why should I listen to you?")
                            action6("")
                        




                        else:
                            print("error write 1 or 2")
                            exit()





                    elif action4 == "2":
                        print("You decline their offer and they seem dissapointed but welcome you to an inn instead")
                        action5 = input("Do you\n1(ask how much it costs to stay for one night) or\n2(ask how much it costs for a cup of chai)  ")


                        if action5 == "1":
                            print("You ask how much it costs to stay a night and they start laughing uncontrollably")
                            action6("")
                        



                        elif action5 == "2":
                            print("You ask how much a cup of tea costs and they reply 5 /*;,.:/'*")
                            action6("")
                        



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

                action3 = input("Do you\n1(enter the mysterious cavern) or\n2(turn back to the village)  ")
                
                if action3 == "1":
                    print("You enter the mysterious cavern and discover a gorgeous crystal covered forest")

                    action4 = input("Do you\n1(move in deeper) or\n2(set up camp)  ")
                    if action4 == "1":
                        print("You wander deeper into the beautiful cavern and spot a massive ancient looking door")
                        action5 = input("Do you\n1(approch it) or\n2(turn around and walk away)  ")

                        if action5 == "1":
                            print("You approch the door and it greets you by saying, you must prove you are worthy to pass through")
                            
                            # write 3 actions for this one, one that says "I am worthy because you are a figment of my reality"
                            action6("")
                        



                        elif action5 == "2":
                            print("You turn around and start leaving, but suddenly the door says, wait don´t leave me!")
                            action6("")
                        


                        else:
                            print("error write 1 or 2")
                            exit()




                    
                    elif action4 == "2":
                        print("You set up a small camp fire and a make shift tent, while setting up you hear somthing coming towards you with light steps")
                        action5 = input("Do you\n1(find cover to hide behind) or\n2(wait to face it, face to face)  ")

                        if action5 == "1":
                            print("You find cover behind a massive crystal")
                            action6("")

                        


                        elif action5 == "2":
                            print("You wait and wait until finally a small cute frog jumps out from around the corner")
                            action6("")
                        




                        else:
                            print("error write 1 or 2")
                            exit()



                    else:
                        print("error write 1 or 2")
                        exit()    


                elif action3 == "2":
                    print("You turn back to the village but you get ambushed by a group of elves")

                    action4 = input("Do you\n1(ready up for a fight) or\n2(pretend not to notice them)  ")
                    if action4 == "1":
                        print("You raise your fists and upper cut one of the elves so hard causing a tooth to fly out")
                        action5 = input("Do you\n1(punch the same elf) or\n2(kick another elf)  ")

                        if action5 == "1":
                            print("You punch the elf again this time harder on his stomach, causing him to spit out blood and falls unconcious")
                            action6("")
                        


                        elif action5 == "2":
                            print("You turn around and kick an elf but you acidentally kick them on their crotch causing him to pass out cold")
                            action6("")
                        



                        else:
                            print("error write 1 or 2")
                            exit()




                    elif action4 == "2":
                        print("You pretend not to notice the eleves and they are prepelexed, they try to gain your attention but fails and give up on bothering you")
                        action5 = input("Do you\n1(keep walking away) or\n2(turn around and do a silly greeting)  ")
                        

                        if action5 == "1":
                            print("You keep walking away until you lose sight of them")
                            action6("")

                        

                        elif action5 == "2":
                            print("You turn around and flex your biceps and say, Howdy dooby dooo partners!")
                            action6("")

                        



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

