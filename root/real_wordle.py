import random
import sys


def readlines(filename):
    with open(filename) as file:
        return file.readlines()


def get_random_word(lines):
    return random.choice(lines)


def double_letter(character1, random_word):
    number = 0
    for character in random_word:
        if character == character1:
            number += 1
    return number > 1


def get_result(guess, random_word):
    result = ''
    for character1, character2 in zip(guess, random_word):
        if character1 == character2 and character1 not in result:
            result += '!'
        elif character1 == character2 and character1 in result:
            result += '?'
        elif character1 != character2 and character1 in random_word and character1 not in result:
            result += '?'
        elif character1 != character2 and character1 in random_word and character1 in result and double_letter(character1, random_word):
            result += '?'
        elif character1 != character2 and character1 in random_word and character1 in result and not double_letter(character1, random_word):
            result += '*'
        elif character1 not in random_word:
            result += '*'
    return result


def wordle_script(random_word, guesses_allowed):
    attempt = 0
    while int(attempt) < int(guesses_allowed):
        attempt += 1
        guess = input(f'Guess # {attempt}: \n')
        if guess == random_word:
            print('!!!!!\n'
                  'Way to go!')
            break
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
