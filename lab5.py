# # Create a list of your favorite songs.
# songs = ['song1', 'song2', 'song3', 'song4', 'song5']
# #print(len(songs))

# # Use a for loop to print each song title along with its number in the list
# for i in range(len(songs)):
#     print(f"{i+1}. {songs[i]}")








# Choose a secret number (e.g., secret_number = 7).
# Use a while loop to repeatedly ask the user to guess the number until they get it right.
# Give hints like "Too high" or "Too low".
# When they guess correctly, print "Congratulations!" and exit the loop.

secret_number = 7
user_input = int(input("Guess a number: "))
while user_input != secret_number:
    if user_input > secret_number:
        print("Too high")
    else:
        print("Too low")
    user_input = int(input("Guess a number: ")) 

print("Congratulations , you guessed the number")    
