# Exercise 1
students = ['Anna', 'Brian', 'Caroline']
print(f"The second student's name is {students[1]}.")
print(f"The last student's name is {students[-1]}.")




# Exercise 2
foods = ('apple', 'banana', 'carrot')
for food in foods:
    print(f"{food.capitalize()} is a good food.")




# Exercise 3
for food in foods[-2:]:
    print(food)




# Exercise 4
home_town = {
    "city": "Gadsden", 
    "state": "AL",
    "population": "~33,000" 
}
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}.")




# Exercise 5
home_town = {
    "city": "Arcadia",
    "state": "California",
    "population": 58000
    }
for key, value in home_town.items():
    print(f"'{key} = {value}'")




# Exercise 6
cohort = []
for idx, student in enumerate(students):
    cohort.append({'student': student, 'fav_food': foods[idx]})
for item in cohort:
    print(item)




# Exercise 7
awesome_students = [f"{student} is awesome!" for student in students]
    print(awesome_students)




# Exercise 8
foods = ('apple', 'banana', 'carrot', 'coffee')
a_foods = [food for food in foods if 'a' in food]
for food in a_foods:
    print(food)