heroes= {"flash":
                   {"speed": "fastest", 
                    "intelligence": "lowest", 
                    "strength": "lowest"}, 
         "batman":
                   {"speed": "slowest", 
                    "intelligence": "highest", 
                    "strength": "money"}, 
         "superman":
                   {"speed": "fast", 
                    "intelligence": "average", 
                     "strength": "strongest"}}
char_name = input("Which character do you want to know about? (flash, Batman, Superman)\n")
char_stat = input("What statistic do you want to know about? (strength, speed, intelligence)\n")

print (f"{char_name}'s {char_stat} is: {heroes[char_name][char_stat]}")


    


