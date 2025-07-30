motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
motorcycles[0] = 'ducati' 
motorcycles.append('Opel') #adds at the end of the list.

motorcycles.insert(1,'Joe')
del motorcycles[0]
last_owned = motorcycles.pop()
print(motorcycles)
#print(popped_motorcycle)


print(f"The last motorcycle I owned was a {last_owned.title()}.")
print(f'the last motorcycle i owned a {last_owned.title()}.')

motorcycles.remove('yamaha') #remove item by value
print(motorcycles)