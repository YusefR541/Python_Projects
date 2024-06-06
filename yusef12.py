#at the end you go back through and see the ones you got wrong and it tells you the correct answer
import random

inccorrect = ["Good try but its wrong.", "Not quite the answer, you gave it a good shot though."]
correct = ["That is correct.", "Correct."]

def MQ1():
    print("What does 2 + 2 =")
    input("Enter the answer:")
    if input == float(4):
        print(random.choice(correct))
    else:
        print(random.choice(inccorrect))

def MQ2():
    print("Lets make these questions harder.")
    print("What does 4³ =")
    input("Enter the answer:")
    if input == "64":
        print(random.choice(correct))
    else:
        print(random.choice(inccorrect))

def MQ3():
    print("Lets see how far you can get!")
    print("What does 6*10⁴ = ")
    input("Enter the answer:")
    if input == "60000":
        print(random.choice(correct))
    else:
        print(random.choice(inccorrect))

#scoreboards keeps count of how many Qs you have gotten right or wrong
#need to check the answers
#need to count right and wrong answers and show above the next answer

#to avoid just printing out everything at once need to check if each question has been answered
def main():
    MQ1()
    MQ2()
    MQ3()
main()