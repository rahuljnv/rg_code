n = 8

# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

print("Hey welcome to the Smart Guess!")
#print("This is Binary Game:")
print("Choose your Number:\t")
no_guess = 9
rmc = 9
while(True):
    rmc -= 1
    if(rmc == 0):
        print("Sorry!! Better Try Next Time, you'r no of guess is no more remain")
        break
    else:
        inp = int(input())
        if(inp == n):
            print("You are Winner, Enjoy the Glory\nGuesses are left:",rmc)
            break
        elif(inp < n):
               print("You'r no. is Smaller,\nGuesses are left:",rmc)
               print("try, Next Number:\t")
        else:
            print("You'r no. is Bigger,\nGuesses are left:", rmc)
            print("try, Next Number:\t")


