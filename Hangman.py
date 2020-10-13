import random


def hang(word, guesses):
    if guesses == 0:
        print("__________")
        print("|         |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("----------")
    elif guesses == 1:
        print("Wrong guess, try again!")
        print("__________")
        print("|         |")
        print("|         O")
        print("|")
        print("|")
        print("|")
        print("__________")
    elif guesses == 2:
        print("Wrong guess, try again!")
        print("__________")
        print("|         |")
        print("|         O")
        print("|         |")
        print("|         |")
        print("|")
        print("__________")
    elif guesses == 3:
        print("Wrong guess, try again!")
        print("__________")
        print("|         |")
        print("|         O")
        print("|        \|")
        print("|         |")
        print("|")
        print("__________")
    elif guesses == 4:
        print("Wrong guess, try again!")
        print("__________")
        print("|         |")
        print("|         O")
        print("|        \|/")
        print("|         |")
        print("|")
        print("__________")
    elif guesses == 5:
        print("Wrong guess, try again!")
        print("__________")
        print("|         |")
        print("|         O")
        print("|        \|/")
        print("|         |")
        print("|        /")
        print("__________")
    elif guesses == 6:
        print("__________")
        print("|         |")
        print("|         O")
        print("|        \|/")
        print("|         |")
        print("|        / \ ")
        print("__________")
        print()
        print("You lose!")
        print("The correct word is: " + word)
        print("Type y to play again or n to quit: ")
        choice = str(input())
        if choice == "y":
            main()


def wordScraper(file):
    wordList = []
    my_file = open(file, "r")
    line = my_file.readline().strip()
    while line != "":
        wordList.append(line)
        line = my_file.readline().strip()
    my_file.close()
    return wordList


def main():
    words = wordScraper("wordbank.txt")
    word = random.choice(words)
    guess = 0
    output = ""
    for i in word:
        output += "_"

    hang(word, guess)
    print(output)
    while guess <= 7:
        chaInput = str(input("Enter a letter: "))
        while len(chaInput) != 1:
            print("Please only enter one letter at a time!")
            chaInput = str(input("Enter a letter: "))

        if chaInput in word:
            for j in range(len(word)):
                if word[j] == chaInput:
                    output = output[0:j] + chaInput + output[j+1:]
            print(output)
            print("Good guess! Next one!")
            if output == word:
                print()
                print("You got it!")
                break
        else:
            guess += 1
            hang(word, guess)
            print(output)


main()
