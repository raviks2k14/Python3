def city_country(city, country, population=''):
    if population:
        c_c = f"{city.title()}, {country.title()} - population {population}"
    else:
        c_c = f"{city.title()}, {country.title()}"
    return c_c
