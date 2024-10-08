import random
#print instructions
print("The rules of the game ROCK PAPER SCISSORS are:\n"
      +"Rock vs Paper -> Paper wins \n"
      +"Rock vs Scissors -> Rock wins \n"
      +"Paper vs Scissors -> Scissors wins\n")
while True:
    print("Enter your choice \n 1-Rock \n 2-Paper \n 3-Scissors \n")
    #take input from user
    choice=int(input("Enter your choice:"))
    #loop until user enter a valid input
    while choice >3 or choice <1:
        choice=int(input("Enter a valid choice please:"))
        #intialize value of choice_name variable to its corresponding choice value
        if choice==1:
            choice_name='Rock'
        elif choice==2:
            choice_name='Paper'
        else:
            choice_name='Scissors'
        #print user choice
        print("User choice is :",choice_name)
        print("Now it's Computer's Turn......")
        #The computer chooses randomly any number among 1,2,3
        computer_choice=random.randint(1,2,3)
        #Initialize value of thecoputer_choice_name variable corresponding to the choice value
        if computer_choice==1:
            computer_choice_name='Rock'
        elif computer_choice==2:
            computer_choice_name='Paper'
        else:
            computer_choice_name='Scissors'
        print("Computer choice is: ", computer_choice_name)
        print(choice_name,'vs',computer_choice_name)
        #to determine the winner
        if choice==computer_choice:
            result='DRAW'
        elif (choice==1 and computer_choice==2) or (computer_choice==1 and choice==2):
            result='Paper'
        elif (choice == 1 and computer_choice == 3) or (computer_choice == 1 and choice == 3):
            result = 'Rock'
        elif (choice == 2 and computer_choice == 3) or (computer_choice == 2 and choice == 3):
            result = 'Scissors'
        
        #print result
        if result=='DRAW':
            print("<---It's a tie!--->")
        elif result==choice_name:
            print("<---User wins--->")
        else:
            print("<---Computer wins--->")
        #ask if the user wants to play again
        print("Do you want to play again? (Y/N))")
        ans=input().lower()
        if ans=='n':
            break
print("Thanks for playing")
