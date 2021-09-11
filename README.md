![james-barker-v3-zcCWMjgM-unsplash](https://user-images.githubusercontent.com/61615072/130869144-886b678e-69f1-4a89-aea1-c777d9003a76.jpg)
Photo by James Barker on Unsplash

# ScrapingPyDogs
Scraping dogs information from a website to use it for a MySql database, to show my knowledge of Python and MySQL.
There are three main files:
- main.py
- df_manipulation.py
- from_df_to_SQL.py


The _main.py_ file contains the code to connect to the website, fetch all the necessary information, downloading them and, finally writing to a _csv_ and _excel_ output format.

The _df_manipulation.py_ is needed to insert inside the previous _csv_ some other columns that are a mathematical combinations of some others like, for example, the column _adaptability_, that is the mean of the respective columns in the individual dog's _adaptability_ field.

The last file, _from_df_to_SQL.py_, connects to *MySQL Workbench*, create the database, the tables and insert the data from the _csv_. At the bottom, to test the accuracy of the script, there is a _SELECT_ statement that fetch all dogs' name that are of 'Mixed Breed Dogs' breed.
