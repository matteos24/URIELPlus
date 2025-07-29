from urielplus import urielplus
import pandas as pd


u = urielplus.URIELPlus()

u.reset()

#Configuration
u.set_cache(True)

#Integrating databases
u.integrate_databases()

u.set_aggregation('A')
'''
#Imputation
u.softimpute_imputation()
'''
#Distance Calculation
print(u.new_distance("featural", "stan1290", "stan1293"))


u.integrate_ethnologue_geo(0)
print(u.new_distance("geographic_w1", ["ghot1243", "alum1246"]))
print(u.new_distance("geographic_w1_normalized", ["ghot1243", "alum1246"]))

u.integrate_ethnologue_geo(1)
print(u.new_distance("geographic_w1", ["ghot1243", "alum1246"]))
print(u.new_distance("geographic_w1_normalized", ["ghot1243", "alum1246"]))
