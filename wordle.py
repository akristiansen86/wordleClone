import json
import random
import math

TRIES = 3

def match_word(word_of_day):
    for letter in word_of_day:
        print(letter)

def check_user_input(user_input, word_list):
    if user_input in word_list:
        return True
    else:
        return False

def welcome():
    print("Welcome to my Wordle-Clone.")
    print("Guess a 5 letter english word.")
    print("Rules: R means letter not in word,")
    print("Y means letter is in word but not in correct place and")
    print("G means correct letter in correct place.")
        

def main():
    f = open('word_list.json')
    word_list = json.load(f)
    f.close()
    num_of_words = len(word_list)
    word_of_day = word_list[math.floor(num_of_words*random.random())]
    tries = TRIES

    # for i in data:
    #     print(i)
    while True:
        welcome()
        print("You have " + str(tries) + " tries left.")
        user_input = input("Enter a 5 letter word: ")
        if len(user_input) is not 5:
            print("Please write a 5 letter word.")
        elif user_input not in word_list:
            print("Word is not in the wordlist, please try once more.")
        
        if user_input is str(word_of_day):
            print("WIN!")
        else:
            tries = tries-1

        print(word_of_day)
        match_word(word_of_day)
        
        if tries is 0:
            print("Game over. The word was: " + word_of_day + ".")
            while True:
                try_again = input("Do you want to try again? Y/N: ")
                if try_again is "Y":
                    break
                elif try_again is "N":
                    break
                else:
                    print("Please answer with Y or N.")
            if try_again is "Y":
                tries = TRIES
                main()
                break
                
            elif try_again is "N":
                print("See you another time!")
                break
            




if __name__ == "__main__":
    main()