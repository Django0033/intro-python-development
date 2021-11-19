life_expectancy_per_country = []


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


with open('./life-expectancy.csv') as life_expectancy_file:
    for line in life_expectancy_file:
        line = line.strip()
        line_parts = line.split(',')
        country = line_parts[0]
        abreviation = line_parts[1]
        year = line_parts[2]
        life_expectancy = line_parts[3]
        if isfloat(life_expectancy) == True:
            life_expectancy_per_country.append(life_expectancy)

print(min(life_expectancy_per_country))
print(max(life_expectancy_per_country))
# print(life_expectancy_per_country.index(max(life_expectancy_per_country)))
