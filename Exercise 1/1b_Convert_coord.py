import geopandas as gpd
import sys
from os import path

try:
    src_file = sys.argv[1]
    src_crs = sys.argv[2]
    dest_crs = sys.argv[3]
except:
    print('Please using this script with the following syntax:\n\npython 1b_Convert_coord.py <source file>  <source CRS> <dest. CRS>')
else:
    dest_file = path.basename(src_file).split('.')[0]+'_'+dest_crs.replace(':', '')+'.shp'
    
    print('\nSource filename', src_file,
        '\nSource CRS:', src_crs,
        '\nDestination CRS:', dest_crs,
        '\nResult filename:', dest_file)
    
    c = input('\nContinue? [Y/n]')
    
    if (c=='') or (c.lower()=='y'):

        df = gpd.read_file(src_file)

        # Set the projection of the datafram
        df.crs = src_crs

        # Convert the projection to destination CRS
        df_convert = df.to_crs(dest_crs)

        # Save to file
        df_convert.to_file(dest_file)
        
        print('Done!')
    else:
        print('Operation aborted!')

