countries = []
abreviations = []
years = []
life_expectancy_per_countries = []
year_of_interest = int(input("Enter the year of interest: "))
life_expectancy_sum = 0
count = 0
year_of_interest_life_countries = []
year_of_interest_life_expectancies = []


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
        countries.append(country)
        abreviations.append(abreviation)
        years.append(year)

        if isfloat(life_expectancy) == True:
            life_expectancy_per_countries.append(life_expectancy)

for i in range(len(life_expectancy_per_countries)):

    if years[i + 1] == str(year_of_interest):
        life_expectancy_sum = life_expectancy_sum + \
            float(life_expectancy_per_countries[i])
        count += 1
        year_of_interest_life_countries.append(countries[i + 1])
        year_of_interest_life_expectancies.append(
            life_expectancy_per_countries[i])

max_life_expectancy = max(life_expectancy_per_countries)
min_life_expectancy = min(life_expectancy_per_countries)
max_life_expectancy_country = countries[life_expectancy_per_countries.index(
    max_life_expectancy) + 1]
min_life_expectancy_country = countries[life_expectancy_per_countries.index(
    min_life_expectancy) + 1]
max_life_expectancy_year = years[life_expectancy_per_countries.index(
    max_life_expectancy) + 1]
min_life_expectancy_year = years[life_expectancy_per_countries.index(
    min_life_expectancy) + 1]
life_expectancy_average = life_expectancy_sum / count
year_of_interest_max_life_expectancy = max(year_of_interest_life_expectancies)
year_of_interest_min_life_expectancy = min(year_of_interest_life_expectancies)
year_of_interest_max_life_expectancy_country = year_of_interest_life_countries[year_of_interest_life_expectancies.index(
    year_of_interest_max_life_expectancy) + 1]
year_of_interest_min_life_expectancy_country = year_of_interest_life_countries[year_of_interest_life_expectancies.index(
    year_of_interest_min_life_expectancy) + 1]

print(max_life_expectancy, max_life_expectancy_country, max_life_expectancy_year)
print(min_life_expectancy, min_life_expectancy_country, min_life_expectancy_year)
print(year_of_interest)
print(f'{life_expectancy_average:.2f}')
print(year_of_interest_max_life_expectancy_country, year_of_interest_max_life_expectancy)
print(year_of_interest_min_life_expectancy_country, year_of_interest_min_life_expectancy)
# print(life_expectancy_per_country.index(max(life_expectancy_per_country)))
