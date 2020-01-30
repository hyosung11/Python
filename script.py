import random

def run_guess(guess, answer):
    if guess > 0 < 11 :
        if guess == answer:
            print('Great guess. Correct')
            return True
    else:
        print('Between 1~10, try again.')
        return False


if __name__ == "__main__":
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10: '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue
