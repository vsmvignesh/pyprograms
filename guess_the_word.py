#!/usr/bin/python
import random
import sys
from collections import Counter

found_letters=[]


def main():
    
    global found_letters
    words=['something','everything','water','picture','maximize','enough','expertise','program','solution','apprehend','malfunction','research','revolution','biscuit']
    pick_word=random.choice(words)
    word_len=len(pick_word)
    wrong_choices=0
    tries=0
    
    temp_word=pick_word
    print("Welcome to Guess the Word Game!!\n")
    print("Guess the \"" + str(word_len) + "\" letter word\n")
    print(word_len * '_ ')
    print("\n")
    while wrong_choices < word_len:
        tries+=1
        guessed_letter=raw_input("Guess a letter!!\n\n")
        print("\n")
        if guessed_letter in pick_word:
            found_letters.append(guessed_letter)
            print("Good Guess!\n")
            for letter in pick_word:
                if letter not in found_letters:
                    temp_word=temp_word.replace(letter,'_ ')
            print temp_word 
            print("\n")            
            
            if set(found_letters) == set(pick_word):
                print("Yayyyy!!! You got it in \"" + str(tries) + "\" tries \n")
                sys.exit(0)
            temp_word=pick_word
            
        else:
            print("Not the letter we are looking for!!!\n")
            print("Retry '" + str(wrong_choices+1) + "'... Remaining retries: " + str(word_len-(wrong_choices + 1)) + "\n")
            wrong_choices+=1
            
    else:
        print("\nToo many tries and no luck!!! The word is \"" + str(pick_word) + "\" \n")
        print("Try again later!!! Bubbyeeee!!\n")

if __name__ == "__main__":
    main()