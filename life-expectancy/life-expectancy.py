countries = []
abbreviations = []
years = []
life_expectancies = []

with open('./life-expectancy.csv') as life_file:

    for line in life_file:
        line = line.strip()
        line_parts = line.split(',')
        country = line_parts[0]
        abbreviation = line_parts[1]
        year = line_parts[2]
        life_expectancy = line_parts[3]
        countries.append(country)
        abbreviations.append(abbreviation)
        years.append(year)
        life_expectancies.append(life_expectancy)

countries.pop(0)
abbreviations.pop(0)
years.pop(0)
life_expectancies.pop(0)
highest_life_expectancy = max(life_expectancies)
lowest_life_expectancy = min(life_expectancies)
higest_life_index = life_expectancies.index(highest_life_expectancy)
lowest_life_index = life_expectancies.index(lowest_life_expectancy)
highest_life_country = countries[higest_life_index]
lowest_life_country = countries[lowest_life_index]
highest_life_year = years[higest_life_index]
lowest_life_year = years[lowest_life_index]
countries_of_interest = []
abbreviations_of_interest = []
years_of_interest = []
life_of_interest = []


def fill_lists_of_interest():
    countries_of_interest.append(countries[i])
    abbreviations_of_interest.append(abbreviations[i])
    years_of_interest.append(years[i])
    life_of_interest.append(float(life_expectancies[i]))


year_of_interest = input('\nEnter the year of interest: ')
print('\nThe overall max life expectancy is: {} from {} in {}'.format(highest_life_expectancy, highest_life_country, highest_life_year) + '\nThe '
      'overall min life expectancy is: {} from {} in {}'.format(lowest_life_expectancy, lowest_life_country, lowest_life_year))
print('\nFor the year {}:'.format(year_of_interest))

for i in range(len(years)):
    if years[i] == year_of_interest:
        fill_lists_of_interest()

average_life_interest = sum(life_of_interest) / len(life_of_interest)
max_life_interest = max(life_of_interest)
max_country_interest = countries_of_interest[life_of_interest.index(
    max_life_interest)]
min_life_interest = min(life_of_interest)
min_country_interest = countries_of_interest[life_of_interest.index(
    min_life_interest)]

print('The average life expectancy across all countries was {:.2f}'.format(
    average_life_interest))
print('The max life expectancy was in {} with {}'.format(
    max_country_interest, max_life_interest))
print('The min life expectancy was in {} with {}'.format(
    min_country_interest, min_life_interest))

country_of_interest = input('\nEnter the country of interest: ')
countries_of_interest = []
abbreviations_of_interest = []
years_of_interest = []
life_of_interest = []

for i in range(len(countries)):
    if countries[i].lower() == country_of_interest.lower():
        fill_lists_of_interest()

average_life_interest = sum(life_of_interest) / len(life_of_interest)
max_life_interest = max(life_of_interest)
max_year_interest = years_of_interest[life_of_interest.index(
    max_life_interest)]
min_life_interest = min(life_of_interest)
min_year_interest = years_of_interest[life_of_interest.index(
    min_life_interest)]

print('\nFor {}:'.format(country_of_interest.capitalize()))
print('The average life expectancy is {:.2f}'.format(average_life_interest))
print('The max life expectancy was in {} with {}'.format(
    max_year_interest, max_life_interest))
print('The min life expectancy was in {} with {}'.format(
    min_year_interest, min_life_interest))
