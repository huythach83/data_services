import geopandas as gpd
import pandas as pd
import sys
from os import path
from tqdm import tqdm

try:
    src_file = sys.argv[1]
except:
    print('Please using this script with the following syntax:\n\npython Extract_point.py <source file>')
else:
    dest_file = path.basename(src_file).split('.')[0]+'.csv'
    
    print('Reading source file...')
    gdf = gpd.read_file(src_file)

    result = []

    print('Extracting point...')
    with tqdm(total=gdf.shape[0]) as pbar:
        for idx, row in gdf.iterrows():
            for coord in row['geometry'].coords:
                result.append([row['OBJECTID'], *coord])
            
            pbar.update()

    print('Writing CSV...')
    rdf = pd.DataFrame(result)
    rdf.to_csv(dest_file, index=False, header=False)

    print('Done!')