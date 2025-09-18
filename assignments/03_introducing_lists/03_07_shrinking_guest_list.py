people = ['Charles Martinet', 'Masanori Sato', 'Yoko Shimomura']

message = ['I would like to invite you to dinner', 'Would you like to join me for dinner', 'Thank you for joining me for dinner']

print (message [0], people [0])
print (message [1], people [1])
print (message [2], people [2])

del people[0]

print (people)

message = ['there is room for more!']
print (message)

insert = ['Koji Kondo','Reggie']
append = ['Miyamoto']

messages = ['Enjoy your dinner', 'Glad you could join us', 'Greetings']

print (messages [0], insert [0])
print (messages [1], insert [1])
print (messages [2], append [0])

message = ['It seems we ran out of room for more guests']
print (message)

popped_insert = insert.pop()
print (insert)
print (popped_insert)

new_message = ['Apologies, we have no more room']
print (new_message)

popped_insert = insert.pop()
print (insert)
print (popped_insert)

message = ['Unfortunately we have no more room for more guests']
print (message)

popped_people = people.pop()
print (people)
print (popped_people)

message = ['The last two of you can stay over for dinner']
print (message)

del people[0]
