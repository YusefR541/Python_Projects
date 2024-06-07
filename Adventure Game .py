name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. "
               "\nWhich way would you like to go?")

if answer.lower() ==  "left":
    answer = input("You come to a river. You can walk around it or swim across. "
                   "\nType walk to walk around and type swim to swim across it.")

    if answer.lower() == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer.lower() == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")

elif answer.lower() == "right":
    
    answer2 = input("You come to a bridge. It looks wobbly. Do you want to cross it or turn back? "
                    "\nType cross or back.")

    if answer2.lower() == "back":
        print("You go back and lose.")
    elif answer2.lower() == "cross":
        answer3 = input("You cross the bridge and meet a stranger. Do you talk to them? Type yes or no.")
    
        if answer3 == "yes":
            print("You talk to the stranger and they give you gold. YOU WIN!")
        elif answer3 == "no":
            print("You ignore the stranger and they push you into the river and you drown.")

else:
    print('Not a valid option. You lose.')



    