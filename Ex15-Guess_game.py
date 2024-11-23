import random

#função do jogo
def guess_game():
    print('Welcome to the guessing game!')

    #Escolher dificuldade
    print('Choose a difficulty level:')
    print('1 - Easy (1-10)')
    print('2 - Medium (1-50)')
    print('3 - Hard (1-100)')
    difficulty = int(input('Choose one option: '))

    try:
        if difficulty == 1:
            min_num = 1
            max_num = 10
        elif difficulty == 2:
            min_num = 1
            max_num = 50
        elif difficulty == 3:
            min_num = 1
            max_num = 100

    except ValueError:   
            print('Invalid option. Please try again.')

    secret_num = random.randint(min_num, max_num)
    attempts = 0

    while True:
        guess = int(input(f'Guess a number between {min_num} and {max_num}: '))
        attempts += 1

        if guess == secret_num:
            print(f'Congratulations! You guessed the number in {attempts} attempts.')
            break
        elif guess < secret_num:
            print('Too low. Try again.')
        else:
            print('Too high. Try again.')

guess_game()