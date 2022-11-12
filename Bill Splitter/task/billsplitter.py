import random

party_dict = {}
friend_list = []

def bill_splitter(x,y):
    return round(x / y, 2)


print("Enter the number of friends joining the party:")
num_friends = int(input())
if num_friends <= 0:
    print("No one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    for i in range(num_friends):
        friend_list.append(input())
    party_dict = dict.fromkeys(friend_list, 0)
    print("\nEnter the total bill value:")
    bill_value = int(input())
    party_dict = dict.fromkeys(friend_list, bill_splitter(bill_value, num_friends))
    print("\nDo you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    user_input = input()
    if user_input == "Yes":
        lucky = random.choice(friend_list)
        print(f"{lucky} is the lucky one!")
        party_dict = dict.fromkeys(friend_list, bill_splitter(bill_value, num_friends - 1))
        party_dict[lucky] = 0

    if user_input == "No":
        print("No one is going to be lucky")
    print("\n")
    print(party_dict)

