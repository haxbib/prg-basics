
import random


computer = random.randint(1, 6)


you = int(input('Guess the dice number (1-6): '))
won = computer == you

print(f'You won: {won}')