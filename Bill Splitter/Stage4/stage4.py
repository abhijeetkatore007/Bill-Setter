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
        print(f"{new_frnds}")
    else:
        l = {"a":"A", "b":"B", "c":"C"}
        lucky_person = random.choice(list(friends.keys()))
        print(f'\n{lucky_person} is the lucky one!')
        lucky = dict.fromkeys(friends,round(bill / (inpt - 1), 2))
        lucky[f"{lucky_person}"] = 0
        print(f"\n{lucky}")

