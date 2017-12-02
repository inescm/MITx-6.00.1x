high = 100
low = 0
ans = int((high+low)/2)

print("Please think of a number between 0 and 100!")

print("Is your secret number "+str(ans)+"?")
print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",end='')
user_=input()
while user_!='c':
    if user_ =='h':
        high = ans

    elif user_ =='l':
        low = ans
    else :
        print("Sorry, I did not understand your input.")
        print("Is your secret number "+str(ans)+"?")
        print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",end='')

    ans = int((high+low)/2)
    print("Is your secret number "+str(ans)+"?")
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",end='')
    user_=input()
print("Game over. Your secret number was: "+str(ans))
