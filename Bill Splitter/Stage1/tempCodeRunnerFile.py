# write your code here
inpt = int(input("Enter the number of friends joining (including you):\n"))
if inpt != 0:
    print("\nEnter the name of every friend (including you), each on a new line:")
    friends = {input(): 0 for i in range(inpt)}
else:
    print("\nNo one is joining for the party")
try:
    print(friends)
except:
    pass