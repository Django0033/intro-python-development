def wind_chill_calculations(t, v):
    return round((35.74 + (0.6215 * t) - (35.75 * (v ** 0.16)) + (0.4275 * t * (v ** 0.16))), 2)


def convert_to_fahrenheit(t):
    return round((t * 1.8) + 32, 1)


temperature = float(input('What is the temperature? '))
scale = input('Fahrenheit or Celcius (F/C)? ')

if scale.lower() == 'f':
    for i in range(5, 61, 5):
        print('At temperature {}F, and wind speed {} mph, the windchill is: {}F'.format(
            temperature, i, wind_chill_calculations(temperature, i)))

else:
    for i in range(5, 61, 5):
        print('At temperature {}F, and wind speed {} mph, the windchill is: {}F'.format(
            convert_to_fahrenheit(temperature), i, wind_chill_calculations(convert_to_fahrenheit(temperature), i)))
