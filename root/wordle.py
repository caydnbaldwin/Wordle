import random
import sys

# read in word list
def readlines(filename):
    with open(filename) as file:
        return file.readlines()

# choose random word
def get_random_word(lines):
    return random.choice(lines)


def get_result(guess, random_word):
    result = ''
    for character1, character2 in zip(guess, random_word):
        # letter matches exactly
        if character1 == character2 and character1 not in result:
            result += '!'
        # correct letter in wrong place
        elif character1 == character2 and character1 in result:
            result += '?'
        # letter matches exactly but the letter has already been revealed previously
        elif character1 != character2 and character1 in random_word:
            result += '?'
        # letter not in word
        elif character1 not in random_word:
            result += '*'
    return result


def wordle_script(random_word, guesses_allowed):
    attempt = 0
    while int(attempt) < int(guesses_allowed):
        attempt += 1
        guess = input(f'Guess # {attempt}: \n')
        # winner
        if guess == random_word:
            print('!!!!!\n'
                  'Way to go!')
            break
        # loser
        elif int(attempt) == int(guesses_allowed) and guess != random_word:
            print(get_result(guess, random_word))
            print(f'Maybe next time. The answer is {random_word}.')
            break
        else:
            print(get_result(guess, random_word))


def main(input_file, guesses_allowed):
    lines = readlines(input_file)
    random_word = get_random_word(lines)
    wordle_script(random_word, guesses_allowed)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
