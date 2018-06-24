import numpy as np
import pprint
pp = pprint.PrettyPrinter(width=150) 

world_alcohol = np.genfromtxt("data/world_alcohol.csv", dtype = "U75", delimiter=",", skip_header = 1)


canada_1986 = (world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == 'Canada')
alcohol_CAN_1986 = world_alcohol[canada_1986, :]
alcohol_CAN_1986[alcohol_CAN_1986[:,4] == '',4] = '0'
alcohol_consumed_CAN_1986 = alcohol_CAN_1986[:,4].astype(float)
total_canadian_drinking = alcohol_consumed_CAN_1986.sum()

pp.pprint(total_canadian_drinking)
