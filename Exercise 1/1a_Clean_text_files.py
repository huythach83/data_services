import sys
import re
from os import path

filename=path.basename(sys.argv[1])

ws = re.compile(r"\s\s+")   # Multiple spaces

newfilename = filename.split('.')[0]+'_processed.csv'

with open(filename, 'r') as file:
    content = file.read().split('\n')   # Split the content of file into list.

# Clean up the content    
content = [ws.sub(',', i.strip()) for i in content if (not i.startswith('Edulog')) and (i.find('Pag')==-1) and (i != '')]

with open(newfilename, 'w') as file:
    file.write('\n'.join(content))

print('Done!')