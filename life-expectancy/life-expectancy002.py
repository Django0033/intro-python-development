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
# average_life_interest = []
# type_of_interest = input('''What type of interest would you like to see?
# 1. Year
# 2. Country
# Please enter a number: ''')


def append_by_interest(interest, interest_choice):
    for i in range(len(interest)):
        if interest[i] == str(interest_choice):
            countries_of_interest.append(countries[i])
            abbreviations_of_interest.append(abbreviations[i])
            years_of_interest.append(years[i])
            life_of_interest.append(float(life_expectancies[i]))
        
    average_life_interest = sum(life_of_interest) / len(life_of_interest)
    max_life_interest = max(life_of_interest)
    max_country_interest = countries_of_interest[life_of_interest.index(max_life_interest)]
    min_life_interest = min(life_of_interest)
    min_country_interest = countries_of_interest[life_of_interest.index(min_life_interest)]
            
    return average_life_interest, max_life_interest, max_country_interest, min_life_interest, min_country_interest


year_of_interest = input('\nEnter the year of interest: ')
function_return = [i for i in append_by_interest(years, year_of_interest)]
print('\nThe overall max life expectancy is: {} from {} in {}'.format(highest_life_expectancy,highest_life_country,highest_life_year))
print('The overall min life expectancy is: {} from {} in {}'.format(lowest_life_expectancy,lowest_life_country,lowest_life_year))
print('\nFor the year {}'.format(year_of_interest))
print('The average life expectancy across all countries was {:.2f}'.format(function_return[0]))
print('The max life expectancy was in {} with {}'.format(function_return[2], function_return[1]))
print('The min life expectancy was in {} with {}'.format(function_return[4], function_return[3]))

country_of_interest = input('\nEnter the country of interest: ').capitalize()
function_return = [i for i in append_by_interest(countries, countries_of_interest)]
print('\nFor the year {}'.format(year_of_interest))
print('The average life expectancy across all countries was {:.2f}'.format(function_return[0]))
print('The max life expectancy was in {} with {}'.format(function_return[2], function_return[1]))
print('The min life expectancy was in {} with {}'.format(function_return[4], function_return[3]))
