# Challenge

1. We have three files: PreStuTrips.txt and PostStutrips.txt and convert.shp.

    a. Please import the PreStuTrips.txt and PostStutrips.txt files into a Microsoft SQL server database and find the differences between the PostStutrips.txt and the PreStuTrips.txt

    b. Please convert the convert.shp file from the negative coordinates “GCS_WGS_1984” to the positive coordinates “NAD_1983_StatePlane_Virginia_South_FIPS_4502_Feet”

2. From the line shapefile named Pierce, write a program to list all the points insides the line shapefile Pierce as the following CSV format file:

```csv
    ObjectID, X1, Y1
    ObjectID, X2,Y2
    .......
    .......
    ObjectID, X n, Yn
```

> With (X1, Y1), (X2, Y2)..., (Xn, Yn) are all the respective points inside all the lines of the line shapefile Pierce.

>ObjectID is the value on the same column of each single line inside the line shapefile Pierce

## I. Challenge 1a

### I.1. Solution

a. Upon inspecting the source text file (**PreStuTrips.txt** and **PostStutrips.txt**):

- Each row has 3 columns, and the columns names have mixed up between ***Student ID*** and ***Edulog ID***
- The data might be scrapped from a website with pagination, hence the ***Pag    x*** text
- All the data is taken at Apr/13/2020
- The columns name appear at the beginning of each page
- There's an blank line at the end of each page.
- The data of each column is separated by a bunch of space. The same with columns name.

Upon further inspection, I knew that the text ***Student ID*** only appears once in the first page. I decided to do the following step:

- Remove all the columns name from each page, except the first page.
- Replace each instance of multiple spaces (at least 2 spaces) with comma (,)
- Remove all the blank line
- Remove all the line with date and Page indicator

The result will be a *.csv* file that can be use to import into MS SQL database

### I.2. Tool

>1a_Clean_text_files.py

***Usage***

> python 1a_Clean_text_files.py \<filename\>

***Requirements***

- Python

After import into MS SQL as 2 tables: ***pre*** for **PreStuTrips.txt** and ***post*** for **PostStutrips.txt**, we can use the following querry to compare 2 tables:

```SQL
SELECT * FROM pre
EXCEPT
SELECT * FROM post
```

The above query compare the difference between ***pre*** and ***post***. There're 48 rows in total

And then I reverse the query

```SQL
SELECT * FROM post
EXCEPT
SELECT * FROM pre
```

It will compare the difference between ***post*** and ***pre***. This time there're 6 rows

This happened because the number of row of ***pre*** table larger than that of ***post*** by 48 rows, and in ***post***, there're 6 rows that have different values compared to those of ***pre***.

### I.3. Result

Detailed result can be viewed in file **1a_Compare_db_result.md**

## II. Challenge 1b

### II.1. Solution

Using python with ***geopandas*** library, we can easily convert the coordinates of shapefile between CRS.

### II.2. Tool

> 1b_Convert_coord.py

***Usage***

> python 1b_Convert_coord.py \<source file\> \<source CRS\> \<dest CRS\>

***Requirements***

- python >= 3.7
- geopandas >= 0.7.0
- pyproj >= 2.1

### II.3. Result

The result can be seen in **convert_ESRI102747.shp**

## III. Challenge 2

### III.1 Solution

Using Python with ***geopandas*** and ***pandas*** we can extract the point from the shapefile

### III.2 Tool

>Extract_point.py

***Usage***

> python Extract_point.py \<source file\>

***Requirements***

- python >= 3.7
- pandas >= 1.0.4
- geopandas >= 0.7.0

### III.3 Result

The result is in the file **Pierce_ShpFrmGeo_Projected.csv**

## IV. Geopandas installation guide

Since geopandas is very hard to install if you don't using Anaconda, we can follow the guide to install it:

>Note: you should create a virtual environment for this

```sh
pip install wheel
pip install pipwin

pipwin install numpy
pipwin install pandas
pipwin install shapely
pipwin install gdal
pipwin install fiona
pipwin install pyproj
pipwin install six
pipwin install rtree
pipwin install geopandas
```