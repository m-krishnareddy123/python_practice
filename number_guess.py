secret_number = 7
number = int(input("Guess a number between 1 to 10: "))
if number == secret_number:
  print("Your guessed number is correct")
else:
  print("Your guessed number is wrong, The correct number is:", secret_number)
  
