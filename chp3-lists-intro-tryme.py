#CHP3

#3-4(Guest list)
#build a list
guests = ['grandfather', 'grandmother', 'wife', 'son']

#print out invitations
print(guests[0].title() + " you are invited to dinner, please bring drinks.")
print(guests[1].title() + " you are invited to dinner, please bring bread.")

#insert random person
guests.insert(2, 'Bob')
print(guests[2].title() + " come over. ")

#3-5(Changing Guest List)
print(guests.pop(2) + " can't make it to the party")

#3-6(More Guests)
#adding more guests, append adds to the end
guests.insert(0, "george")
guests.insert(3, "james")
guests.append("frank")

#printing specific guest
print(guests[0].title())

#generalized statement
print("I found a bigger table three more can come!")

#3-7 Shrinking Guest List(Space for only 2)
print("Sorry, we only have space for 2")
print("Sorry, I cannot invite you, no space", guests.pop().title())
print(guests)
print("Sorry, I cannot invite you, no space", guests.pop().title())
print(guests)
print("Sorry, I cannot invite you, no space", guests.pop().title())
print(guests)
print("Sorry, I cannot invite you, no space", guests.pop().title())
print(guests)
print("Sorry, I cannot invite you, no space", guests.pop().title())

#Inviting the only two left not popped out of the list
print(guests[0].title() + ", you are still invited to dinner")
print(guests[1].title() + ", you are still invited to dinner")

#Removing the remaning names from element 0 to 1
del guests[0:2]

#proof list is empty
print(guests)

