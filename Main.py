import Game
import sys


if __name__ == '__main__':

    len_word = Game.init()

    first_filter_words = Game.FilterWordsByLength(len_word)

    char = 'abcdefghijklmnopqrstuvwxyz'

    guess,list_char = Game.GuessLetter(list(char),first_filter_words)

    new_words_list = []

    no_turns = 0

    while no_turns < 9:

        is_correct , list_char_new = Game.IsGuessCorrect(guess,list_char)



        print("no guess : {} , is correct: {}".format(no_turns , is_correct))

        if no_turns == 0:

            new_words_list = Game.ActOnGuessFilter(is_correct,guess,first_filter_words)

        else:

            if len(new_words_list) != None:

                new_words_list = Game.ActOnGuessFilter(is_correct,guess,new_words_list)

            else:

                
                print("error")
                sys.exit()

        if is_correct == True:

            pos = Game.GetLetterPostition(guess)

            #print(guess)

            new_words_list = Game.FilterAgain(new_words_list,guess,pos)

        else:

            no_turns = no_turns + 1

        print("filtered words : {}".format(len(new_words_list)))

        list_char_new = Game.CheckListLetters(new_words_list,list_char_new,guess)

        #print(list_char_new)

        game_status = Game.GuessWord(new_words_list)

        if game_status == True:

            sys.exit()

        guess , list_char = Game.GuessLetter(list_char_new,new_words_list)

    if game_status == False:

        print("you won")
