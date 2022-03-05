import random
secret_number = str(random.randint(10, 99))
print("Guess the number. It contains 2 digits.")
print(secret_number)
chance = 7
 
while chance > 0:
   player_guess = input("Enter your guess: ")
   
   if player_guess == secret_number:
       print("Yay, you guessed it!")
       print("YOU WIN.")
       break
   else:
       bulls = 0
       cows = 0
      
       if player_guess[0] == secret_number[0]:
           bulls += 1
       if player_guess[1] == secret_number[1]:
           bulls += 1
       if player_guess[0] == secret_number[1]:
           cows += 1
       if player_guess[1] == secret_number[0]:
           cows += 1
 
       print("Bulls: ",bulls)
       print("Cows: ",cows)
 
       chance -= 1
 
       if chance < 1:
           print("You lost the game.")
           break