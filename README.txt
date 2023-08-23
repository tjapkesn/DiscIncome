###ABOUT###
The goal of this project was to estimate discretionary income around the world. Discretionary income is defined as post tax income left over after accounting for basic expenses: like housing, food, transportation, and healthcare. I have, for now, shelved this project due to: the  complexity of the problem being much larger than I had forseen, less international data being availible for things like rent than I had expected, and a significant SQL mistake resulting in the database needing repair. Overall, it seemed the longer I worked on the project that things seemed more and more difficult, that my final results would be less and less widely applicable, intereptable, and rigorous than I had initially hoped. So I have decided to stop work on this project to work on one I that I may be more passionate about. This readme exists to document things that are in the repo, steps I took in this project, what I have learned from working this project, and what I would do differently were I to do a project like this in the future.
###WHAT'S IN THIS REPO###
-This README
-The original tables collected during the data gathering phase
-A backup of the SQL database I was working with during this project
-Various Jupyter Notebooks that I used to transform the original tables and then import them to the postgresql database
-A Python file defining a function to calculate taxes and social security contributions (untested)
###WHAT HAVE I LEARNED?###
-Looking for data needed for a project
-Working with data that often doesn't fit well together (different names for same country, data describing different timeframs, etc)
-Cleaning and transforming tables to a more workable form in SQL
-Using sqlalchemy to send pandas dataframes to postgresql databases
###WHAT WOULD I HAVE DONE DIFFERENTLY###
-Backup whatever I plan to work on to github before working on it
-Check for data availibility before setting project expectations
-Use sqlite as opposed to something like postgresql
-Break down the project into subprojects before starting (Do you still want to do this? Or is just the rent, tax, or income portion enough to be their own project?)
###DETAILS###

UNDER CONSTRUCTION



