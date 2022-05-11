print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

from random import randint

guess = randint(1,100)
#This is the random number

num_guess=0
#This is the number of guesses

inp_guess = 101
#This is the guess by the user, initialized at 101

prev_margin=0
#This is to initialize the previous margin for the user

while inp_guess != guess:
    inp_guess = input('\nEnter your guess here:' )
    inp_guess = int(inp_guess)
    num_guess += 1
    if inp_guess < 1 or inp_guess > 100:
        print('OUT OF BOUNDS')
    else:
        if num_guess==1:
            if inp_guess == guess:
                print('Congratulations, you guessed the number in your first try!')
            
            elif abs(inp_guess - guess) <=10:
                print('Warm')
            
            else:
                print('Cold')
            
            prev_margin=abs(inp_guess-guess)
        
        else:
            if inp_guess == guess:
                print(f'Congratulations, you guessed the number in {num_guess} tries!')
        
            elif abs(inp_guess-guess) < prev_margin:
                print('Warmer')
            
            else:
                print('Colder')
        
            prev_margin=abs(inp_guess-guess)
        