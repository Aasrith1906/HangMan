
from random import randint
import sys
from collections import Counter

def init():

    print("pick a word between 1-23 characters")

    len_word  = input("enter number of characters : ")

    return len_word

def GetDictionary():

    words_dic = []

    with open('words.txt','r') as text_file:

        for word in text_file:

            words_dic.append(str(word))

    #print(len(words_dic))

    return words_dic

def FilterWordsByLength(len_word):

    words_dic = GetDictionary()

    filtered_dictionary = []

    for word in words_dic:

        word = word.strip()

        if len(list(word)) == int(len_word):

            filtered_dictionary.append(str(word))

    print("there are {} words with that length".format(len(filtered_dictionary)))

    #print(filtered_dictionary)

    return filtered_dictionary

def GuessLetter(list_char,list_words):

    #guess = randint(0,len(list_char)-1)

    if len(list_words) == 0:

        print("no words found you won")

    list_words_s = ""

    final_list=[]

    for i in list_words:

        list_words_s = list_words_s + i

    result = [item for items, c in Counter(list(list_words_s)).most_common()
                                      for item in [items] * c]

    for i in result:

        if i in list_char:

            final_list.append(i)


    final_list = list(dict.fromkeys(final_list))

    if len(final_list) != None:

    #print(final_list)

        return final_list[0] ,list_char

    else:

        print("error")

        sys.exit()

def IsGuessCorrect(guess,list_char):

    user_in = input("does the word have the letter {}:".format(guess))

    if user_in == 'y':

        return True,list_char

    elif user_in == 'n':

        list_char.remove(guess)

        return False,list_char

    else:

        print("invalid!!")
        sys.exit()

def GetLetterPostition(guess):

    number_times = input("enter number of times letter occurs: ")

    pos_list = []

    for i in range(int(number_times)):

        pos = input("enter position of {} in your word:".format(guess))

        pos_list.append(int(pos))

    return pos_list

def FilterAgain(list_words,guess,pos_list):

    new_list = []

    for word in list_words:

        list_word = list(word)

        #print(list_word)

        for pos in pos_list:

            if list_word[pos-1] != guess:

                pass

            else:

                #print(word)
                new_list.append(word)

    #print(new_list)

    return new_list

def ActOnGuessFilter(is_correct , guess , list_word):

    if is_correct == True:

        for word in list_word:

            if guess not in list(word):

                list_word.remove(word)

            else:

                pass
    else:

        for word in list_word:

            if guess in list(word):

                list_word.remove(word)

            else:

                pass

    return list_word

def CheckListLetters(list_words , list_chars,guess):

    new_list_char = []

    for char in list_chars:

        if char == guess:

            pass

        else:

            for word in list_words:

                if char in list(word):

                    if char in new_list_char:

                        pass

                    else:

                        new_list_char.append(char)

    return new_list_char

def GuessWord(list_words):

    if len(list_words) == 1:

        print("word is {}".format(list_words[0]))

        return True

    elif len(list_words) == 0:

        print("couldnt find the word , you won")

    else:

        return False
