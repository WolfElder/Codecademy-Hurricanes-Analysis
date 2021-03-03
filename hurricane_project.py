import pprint

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# write your update damages function here:
def damages_update(damages):
    """ Updates damages to remove letters and replace with 0 """
    updated_damages = []
    conversion = {"M": 1000000,
                  "B": 1000000000}
    for damage in damages:
        if damage == 'Damages not recorded':
            updated_damages.append(damage)
        elif damage[-1] in conversion:
            updated_damages.append(float(damage[:-1]) * conversion[damage[-1]])
    return updated_damages


print()

damages = damages_update(damages)


# print(damages)


# write your construct hurricane dictionary function here:
def dict_canes(name, month, year, m_s_w, affected_area, damages, deaths):
    """Makes a dictionary for all information on Hurricanes"""
    canes = {}
    for i in range(len(name)):
        new_name = name[i]
        canes[new_name] = {"Name": name[i],
                           "Month": month[i],
                           "Year": year[i],
                           "Max Sustained Wind": m_s_w[i],
                           "Damage": damages[i],
                           "Areas Affected": affected_area[i],
                           "Death": deaths[i]}
    return canes


hurricanes = dict_canes(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
# pprint.pprint(hurricanes)
print()


# write your construct hurricane by year dictionary function here:
def dict_by_year(hurricanes):
    """Takes data from Hurricanes, and displays information by year."""
    cane_by_year = {}
    for cane in hurricanes:
        current_cane = []
        current_year = hurricanes[cane]["Year"]
        current_cane.append(hurricanes[cane])
        if current_year in cane_by_year:
            cane_by_year[current_year] += current_cane
        else:
            cane_by_year[current_year] = current_cane
    return cane_by_year


hurricanes_by_year = dict_by_year(hurricanes)
# pprint.pprint(hurricanes_by_year)
print()


# write your count affected areas function here:
def count_affected_area(areas_affected):
    """This makes a dictionary of the areas with a count of how many times it was hit by a storm."""
    areas = []
    count_areas = {}
    for area in areas_affected:
        for item in area:
            if item.title().startswith("The"):
                item = item.replace("The ", "")
            areas.append(item.title())
    for name in areas:
        count_areas[name] = areas.count(name)
    return count_areas


counted_affected_areas = count_affected_area(areas_affected)
# print(counted_affected_areas)
print()


# write your find most affected area function here:

def find_most_affected_area(location):
    """This finds the area that gets hit the most often"""
    current_high = 0
    current_location = 0
    for area in location:
        if location[area] > current_high:
            current_high = location[area]
            current_location = area

    return current_location, current_high


most_affected = find_most_affected_area(counted_affected_areas)
# print(most_affected)
print()


# write your greatest number of deaths function here:
def most_deaths_caused(hurricane):
    """Find the area where the most deaths occur"""
    current_high = 0
    current_cane = 0
    for record in hurricane:
        if hurricane[record]["Death"] > current_high:
            current_high = hurricane[record]["Death"]
            current_cane = hurricane[record]["Name"]
    return current_cane, current_high


most_deaths = most_deaths_caused(hurricanes)
# print(most_deaths)
print()


# write your categorize by mortality function here:


def mortality_scale(hurricanes):
    """Takes deaths from Hurricanes and assigns them to a rating then outputs Rating : Hurricane_Names"""
    mortality_scale_values = {0: 0,
                              1: 100,
                              2: 500,
                              3: 1000,
                              4: 10000}
    hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for cane in hurricanes:
        num_deaths = hurricanes[cane]["Death"]
        if num_deaths == mortality_scale_values[0]:
            hurricanes_by_mortality[0].append(hurricanes[cane])
        elif mortality_scale_values[0] < num_deaths <= mortality_scale_values[1]:
            hurricanes_by_mortality[1].append(hurricanes[cane])
        elif mortality_scale_values[1] < num_deaths <= mortality_scale_values[2]:
            hurricanes_by_mortality[2].append(hurricanes[cane])
        elif mortality_scale_values[2] < num_deaths <= mortality_scale_values[3]:
            hurricanes_by_mortality[3].append(hurricanes[cane])
        elif mortality_scale_values[3] < num_deaths <= mortality_scale_values[4]:
            hurricanes_by_mortality[4].append(hurricanes[cane])
        else:
            hurricanes_by_mortality[5].append(hurricanes[cane])
    return hurricanes_by_mortality


mortality_ratings = mortality_scale(hurricanes)
# pprint.pprint(mortality_ratings)
print()


# write your greatest damage function here:
def greatest_damage(hurricanes):
    """Finds the hurricane that caused the most damage"""
    current_high = 0
    current_cane = []
    for record in hurricanes:
        damage = hurricanes[record]["Damage"]
        if damage != "Damages not recorded" and damage > current_high:
            current_high = damage
            current_cane = hurricanes[record]["Name"]
    return current_cane, "$" + str(current_high)


hurricane_greatest_damage = greatest_damage(hurricanes)
# print(hurricane_greatest_damage)
print()


# write your categorize by damage function here:

def rate_by_damage(hurricanes):
    """"Takes the damage values and ranks hurricanes by destruction"""
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}
    hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for cane in hurricanes:
        damage = hurricanes[cane]["Damage"]
        if damage == "Damages not recorded":
            hurricanes_by_damage[0].append(hurricanes[cane])
        elif damage == damage_scale[0]:
            hurricanes_by_damage[0].append(hurricanes[cane])
        elif damage_scale[0] < damage <= damage_scale[1]:
            hurricanes_by_damage[1].append(hurricanes[cane])
        elif damage_scale[1] < damage <= damage_scale[2]:
            hurricanes_by_damage[2].append(hurricanes[cane])
        elif damage_scale[2] < damage <= damage_scale[3]:
            hurricanes_by_damage[3].append(hurricanes[cane])
        elif damage_scale[3] < damage <= damage_scale[4]:
            hurricanes_by_damage[4].append(hurricanes[cane])
        else:
            hurricanes_by_damage[5].append(hurricanes[cane])
    return hurricanes_by_damage


hurricanes_by_damage = rate_by_damage(hurricanes)
# pprint.pprint(hurricanes_by_damage)
print()
