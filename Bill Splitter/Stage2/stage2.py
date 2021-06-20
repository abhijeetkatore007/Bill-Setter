"""https://hyperskill.org/projects/175/stages/902/implement



"""
# write your code here
inpt = int(input("Enter the number of friends joining (including you):\n"))
if inpt <= 0:
    print("\nNo one is joining for the party")
    
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    friends = {input(): 0 for i in range(inpt)}
    bill = float(input("Enter the total bill value:\n"))
    new_frnds = dict.fromkeys(friends, round(bill/inpt, 2))
    print(new_frnds)
    

    # ////

count = int(input("Enter the number of friends joining (including you):\n"))
if count <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line: ")
    friends = {input(''): 0 for i in range(count)}
    total_bill = int(input("Enter the total bill value:\n"))
    friends = {i: round(total_bill / len(friends.keys()), 2) for i in friends}
    print(friends)


