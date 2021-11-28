people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
names = []
ages = []

for person in people:
    person = person.split()
    name = person[0].strip()
    age = int(person[1].strip())
    names.append(name)
    ages.append(age)

lower_age_index = ages.index(min(ages))
younger_person = names[lower_age_index]
lower_age = ages[lower_age_index]
print(younger_person, lower_age)
