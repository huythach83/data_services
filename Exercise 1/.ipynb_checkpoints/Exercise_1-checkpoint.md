## Challenge

We have three files: PreStuTrips.txt and PostStutrips.txt and convert.shp.

a. Please import the PreStuTrips.txt and PostStutrips.txt files into a Microsoft SQL server database and find the differences between the PostStutrips.txt and the PreStuTrips.txt

b. Please convert the convert.shp file from the negative coordinates
“GCS_WGS_1984” to the positive coordinates “NAD_1983_StatePlane_Virginia_South_FIPS_4502_Feet”

## Challenge 1a

### Solution

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

### Tool

1a_Clean_text_files.py

***Usage***

> python 1a_Clean_text_files.py \<filename\>

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

### Result

Detailed result can be viewed in file **1a_Compare_db_result.md**