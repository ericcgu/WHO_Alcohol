import numpy as np
import pprint
pp = pprint.PrettyPrinter(width=150) 

#import
world_alcohol = np.genfromtxt("data/world_alcohol.csv", dtype = "U75", delimiter=",", skip_header = 1)

#filter
def total_per_country_by_year(year, country):
    filter_by = (world_alcohol[:,0] == year) & (world_alcohol[:,2] == country)
    alcohol_filtered = world_alcohol[filter_by, :]
    alcohol_filtered[alcohol_filtered[:,4] == '',4] = '0'
    alcohol_consumed = alcohol_filtered[:,4].astype(float)
    return alcohol_consumed.sum()

countries = set(world_alcohol[:,2])
totals = dict.fromkeys(countries, 0)
for country in countries:
    totals[country] = total_per_country_by_year('1989', country)

highest_value = max(totals.values())
highest_key = max(totals, key=totals.get)

pp.pprint(totals)
print(highest_key, highest_value)

