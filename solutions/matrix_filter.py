import numpy as np
import pprint
pp = pprint.PrettyPrinter(width=150) 

world_alcohol = np.genfromtxt("data/world_alcohol.csv", dtype = "U75", delimiter=",", skip_header = 1)

country_algeria = world_alcohol[world_alcohol[:,2] == 'Algeria',:]
pp.pprint(list(country_algeria[0:10]))