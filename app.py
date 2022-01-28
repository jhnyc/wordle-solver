from english_words import english_words_set
import random

# Filter out ineligible words, i.e. words containing ' & names
def eligible_words(english_words_set):
    words = [word for word in english_words_set if len(word) == 5 and not "'" in word]
    words = [word for word in words if word[0].isupper() == False]
    return words


# Return the result of a submission in terms of the correct, semicorrect & incorrect words
def submit(guess, answer, semicorrect=None, incorrect=None):
    """Check the guess against the answer"""
    correct = {}
    incorrect = [] if incorrect is None else incorrect
    semicorrect = {} if semicorrect is None else semicorrect
    counter = {char: 0 for char in guess}
    for i in range(5):
        if guess[i] == answer[i]:
            correct[i] = guess[i]
            counter[guess[i]] += 1
        elif guess[i] in answer and counter[guess[i]] < answer.count(guess[i]):
            semicorrect[i] = guess[i]
            counter[guess[i]] += 1
        else:
            incorrect.append(guess[i])
    return correct, semicorrect, list(set(incorrect))


# Filter words given the results of a guess
def find_words(words, correct, semicorrect, incorrect):
    incorrect = [char for char in incorrect if char not in list(correct.values()) + list(semicorrect.values())]
    # filter out all words containing incorrect characters
    words = [word for word in words if any(char in word for char in incorrect) == False]
    # filter words compatible with the correct characters
    words = [word for word in words if all(correct[i] == word[i] for i in correct)]
    # filter words containing the semicorrect characters
    words = [word for word in words if all(semicorrect[i] in word for i in semicorrect)]
    # fitler out words with characters in the positions of the semicorrect characters
    words = [word for word in words if all(semicorrect[i] != word[i] for i in semicorrect)]
    return words


# Main function for solving the word
def crack_wordle():
    words = eligible_words(english_words_set)
    correct, semicorrect, incorrect = {}, {}, []
    attempt = 1
    while len(correct) != 5 and attempt < 7:
        words = find_words(words, correct, semicorrect, incorrect)
        if attempt < 6:
            guess = f"\nAttempt {attempt}: {random.choice(words)}"
            print(guess)
            attempt += 1
        elif attempt == 6:
            guess = f"\nLast Attempt (Good Luck!): {random.choice(words)}"
            print(guess)
            break
        correct_temp = input("Correct letters (e.g. _a_py):")
        correct = {i: correct_temp[i] for i in range(len(correct_temp)) if correct_temp[i] != "_"}
        semicorrect_temp = input("Semicorrect letters (e.g. _a_py):")
        semicorrect = {i: semicorrect_temp[i] for i in range(len(semicorrect_temp)) if semicorrect_temp[i] != "_"}
        incorrect_temp = [char for char in input("Incorrect letters:") if char not in list(correct.values()) + list(semicorrect.values())]
        incorrect = list(set(incorrect + [char for char in incorrect_temp]))


if __name__ == "__main__":
    crack_wordle()
