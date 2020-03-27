#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import geopandas as gpd

data = pd.read_csv('data.csv')

data= data[['Country, Other', 'Total Cases']]
world_data = gpd.read_file(r'/Users/rudrioza/Desktop/ML/coronaVirusOutbreak/Countries.shp')
world_data.replace('South Korea' , 'S. Korea', inplace=True)
world_data.replace('United States' , 'USA', inplace=True)
world_data.replace('United Kingdom' , 'UK', inplace=True)
data.replace('Hong Kong','China', inplace=True)
world_data.replace('United Arab Emirates' , 'UAE', inplace=True)
world_data.replace('Macau' , 'Macao', inplace=True)
world_data.replace('The former Yugoslav Republic of Macedonia' , 'North Macedonia', inplace=True)
data.drop['Total:']

data.rename(columns = {'Country, Other': 'name'}, inplace=True)
world_data.rename(columns = {'CNTRY_NAME': 'name'}, inplace=True)

combined = world_data.merge(data, on="name")


combined.to_file(r'/Users/rudrioza/Desktop/ML/coronaVirusOutbreak/combined.shp')



