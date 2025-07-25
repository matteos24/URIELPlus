from urielplus import urielplus
import pandas as pd

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

d_MAX = 0
rows_reg = []
rows_normalized = []
for lang_1 in u.databases.geo_distributions:
    for lang_2 in u.databases.geo_distributions:
        d_reg = u.new_distance("geographic_w1", [lang_1, lang_2])
        d_reg_normalized = u.new_distance("geographic_w1_normalized", [lang_1,lang_2])
        if (d_reg > d_MAX):
            d_MAX = d_reg
        
        rows_reg.append({'lang1': lang_1, 'lang2': lang_2, 'distance': d_reg})
        rows_normalized.append({'lang1': lang_1, 'lang2': lang_2, 'distance': d_reg_normalized})

long_df_reg = pd.DataFrame(rows_reg)  
long_df_normalized = pd.DataFram(rows_normalized)

wide_df_reg = long_df_reg.pivot(index='lang1', columns='lang2', values='distance').sort_index()
wide_df_normalized = long_df_normalized.pivot(index='lang1', columns='lang2', values='distance').sort_index()

wide_df_reg.to_csv("language_distance_combinations_regular.csv")     
wide_df_normalized.to_csv("language_distance_combinations_normalized.csv") 
print("Longest Distance Between Two Languages: " + str(d_MAX))    
