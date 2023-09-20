# Mastermind in Python
# 20/09/2023
import random

def getCode(colorsList, combinationLength):
    duplicatedList = colorsList * combinationLength

    random.shuffle(duplicatedList)

    code = duplicatedList[:combinationLength]

    return ''.join(code), code

def getMatches(list1, list2):
    return len( [idx for idx, item in enumerate(list2) if list1[idx] == item] )

def getWrongPlaces(codeList, attemptList):
    wrongPlaces = 0

    for idx, element in enumerate(attemptList):
        if element != codeList[idx] and element in codeList:
            wrongPlaces += 1

    return wrongPlaces


def main(COLORS, CODE_LENGTH):
    RIGHT_PLACE = "You have {num} existing marbles in the right place."
    WRONG_PLACE = "You have {num} existing marbles in the wrong place."

    CODE, codeList = getCode(COLORS, CODE_LENGTH)

    ATTEMPTS_LEFT = 10

    while ATTEMPTS_LEFT > 0:
        print("Enter the code (e.g. R O G B G): ")
        codeAttempt = input(" > ")
        attemptList = codeAttempt.split(" ")[:CODE_LENGTH]
        
        if attemptList == codeList:
            print(f"You got the code in {1 + (10 - ATTEMPTS_LEFT)} tries!")
            askPlayAgain()

        print("Wrong code.")
        print(RIGHT_PLACE.replace("{num}", str(getMatches(codeList, attemptList))))
        print(WRONG_PLACE.replace("{num}", str(getWrongPlaces(codeList, attemptList))))

        ATTEMPTS_LEFT -= 1
        if ATTEMPTS_LEFT > 1:
            print(f"{ATTEMPTS_LEFT} attempts left.")
        elif ATTEMPTS_LEFT > 0:
            print(f"Only {ATTEMPTS_LEFT} attempt left. Better make it count.")
        else:
            print("You failed ;-;")
            print("I knew I shouldn't have hired the codebreaker from Wish!")

    print(f"The code was {' '.join(codeList)}")
    askPlayAgain()

def askPlayAgain():
    print("Want to play again? [y/n]: ")
    playAgain = input(" > ")

    if playAgain.lower() == "y":
        print("Okay, let's play again!")
        main(COLORS, CODE_LENGTH)
        return
    else:
        print("Okay, goodbye!")
        exit()

def intro():
    COLORS = ["R", "O", "Y", "G", "B", "P"]
    CODE_LENGTH = 5

    print("Welcome to Mastermind.")
    print("You have to try and crack a code, consisting of colors.")
    print(f"The colors are {COLORS} and the code is {CODE_LENGTH} characters long.")
    print("Good luck.")
    return COLORS, CODE_LENGTH

if __name__ == "__main__":
    COLORS, CODE_LENGTH = intro()
    main(COLORS, CODE_LENGTH)