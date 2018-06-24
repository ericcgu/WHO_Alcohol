import numpy as np
import pprint
pp = pprint.PrettyPrinter(width=150) 

world_alcohol = np.genfromtxt("data/world_alcohol.csv", dtype = "U75", delimiter=",", skip_header = 1)

is_value_empty = world_alcohol[:,4] == ''
world_alcohol[is_value_empty,4] = '0'
pp.pprint(list(world_alcohol[0:10]))