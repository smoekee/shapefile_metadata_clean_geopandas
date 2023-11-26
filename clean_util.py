import geopandas as gpd
import pandas as pd
import fiona


#filter shapefile attributes by specific columns
counties_gdf = gpd.read_file('substations.shp',
            include_fields=['ID', 'NAME', 'CITY', 'ZIPCODE', 'LINES', 'geometry']                 
                             )

#write filtered dataframe to shapefile
counties_gdf.to_file('clean_substataion.shp')



### EXTRA UTILITIES ###

## for col in counties_gdf.columns:
#    print(col)

## pd.options.display.max_columns = None