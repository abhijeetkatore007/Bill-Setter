"""https://hyperskill.org/projects/175/stages/903/implement#solutions



"""

import random 

inpt = int(input("Enter the number of friends joining (including you):\n"))
if inpt <= 0:
    print("\nNo one is joining for the party")
    
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    friends = {input(): 0 for i in range(inpt)}
    bill = float(input("\nEnter the total bill value:\n"))
    new_frnds = dict.fromkeys(friends, round(bill/inpt, 2))
    if 'no' == input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n').lower():
        print('\nNo one is going to be lucky')    
    else:
        l = {"a":"A", "b":"B", "c":"C"}
        # kkey = list(friends.keys())
        # print(f'\n{random.choice(kkey)} is the lucky one!')
        print(f'\n{random.choice(list(friends.keys()))} is the lucky one!')

    

    # Moderator

    import random

count = int(input("Enter the number of friends joining (including you):\n"))
if count <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line: ")
    friends = {input(''): 0 for i in range(count)}
    total_bill = int(input("Enter the total bill value:\n"))
    lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky_feature == "Yes":
        print(f"{random.choice(list(friends.keys()))} is the lucky one!")
    else:
        print("No one is going to be lucky")
    # friends = {i: round(total_bill / len(friends.keys()), 2) for i in friends}
    # print(friends)
