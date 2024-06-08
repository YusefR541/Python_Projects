name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to "
               "go?").lower()

if answer == "left":
    answer = input("You come to a river. You can walk around it or swim across. Type walk to walk around and type swim "
                   "to swim across it.")

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")

elif answer == "right": 
    
    answer2 = input("You come to a bridge. It looks wobbly. Do you want to cross it or turn back? Type cross or back.").lower()

    if answer2 == "back":
        print("You go back and lose.")
    if answer2 == "cross":
        answer3 = input ("You cross the bridge and meet a stranger. Do you talk to them? Type yes or no.")
    
if answer3 == "yes":
    print("You talk to the stranger and they give you gold. YOU WIN!")
    
if answer3 == "no":
    print("You ignore the stranger and they push you into the river and you drown.")

else:
        print('Not a valid option. You lose.')   
