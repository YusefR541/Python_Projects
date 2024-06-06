print ("Quiz game")

counter = 0

print ("2 + 2?")

print ("A. 3")
print ("B. 4")
print ("C. 6")
print ("D. 8")

x = raw_input("Answer: ")
if x == "b" or x == "B":
    x = "correct"

print ("3 + 2?")

print ("A. 3")
print ("B. 6")
print ("C. 9")
print ("D. 5")

x = raw_input("Answer: ")
if x == "d" or x == "D":
    x = "correct"

print ("5 + 4?")

print ("A. 4")
print ("B. 5")
print ("C. 6")
print ("D. 9")

x = raw_input("Answer: ")
if x == "d" or x == "D":
    x = "correct"

while x == "correct":
    counter = counter + 1
    if counter >= 1:
        print ("Your score is good")
        x = raw_input("Press enter to quit")        
    else:
        print ("Your score is not good")