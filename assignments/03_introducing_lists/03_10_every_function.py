favorite_foods = ['Lasagna', 'Pizza', 'Empanadas', 'Barbeque Chicken']
print(favorite_foods[0])

message = (f'My favorite food of all time is {favorite_foods [1]}')
print(message)

favorite_foods.append('Chicken Wings')
print(favorite_foods)

popped_favorite_foods = favorite_foods.pop()
print(favorite_foods)
print(popped_favorite_foods)

favorite_foods = ['Lasagna', 'Pizza', 'Empanadas', 'Barbeque Chicken']
favorite_foods.sort()
print(favorite_foods)

favorite_foods.reverse()
print(favorite_foods)

len(favorite_foods)