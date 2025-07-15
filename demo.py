from urielplus import urielplus

u = urielplus.URIELPlus()

u.reset()

#Configuration
u.set_cache(True)

u.codes = "Iso"
"""
#Integrating databases
u.integrate_databases()

u.set_aggregation('A')

#Imputation
u.softimpute_imputation()

#Distance Calculation
print(u.new_distance("featural", "stan1290", "stan1293"))

"""
u.integrate_ethnologue_geo()
print(str(u.new_distance("geographic_w1", ["ben", "amh"])))
print(str(u.new_distance("geographic_w1_normalized", ["ben", "amh"])))
print(str(u.new_geographic_distance(["ben","amh"])))