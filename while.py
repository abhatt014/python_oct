# count = 1
# while True :
#     print(f"count is : {count}")
#     count = count + 1

# print("Loop finished")

# Ask the user for a number.
import time
val = int(input("Enter a number: "))

# Use a while loop to count down from that number to 1, printing each number.
while val >= 1:
    print(val)
    time.sleep(1)
    val = val - 1
# After the loop, print "Blast off!".
print("Blast off!")   