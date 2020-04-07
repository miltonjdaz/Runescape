# Airflow DAG: loads S3 data into Postgres database

I've had this project in mind for a while: combining my tech skills with data that I recorded on my own. Graduate work, searching for a job, and planning a wedding requires a lot of effort so I wanted to do a task that can be easily done but still provide a lot of data. As such, I thought of playing Old School Runescape again. I had not played Old School Runescape in a while but I knew I could get a consistent amount of data from killing the same monster in the game and record the different drops it provides. I decided on brutal black dragons because they have 59 unique drops to be recorded. 

All the items dropped by the brutal black dragon can be found here: https://oldschool.runescape.wiki/w/Brutal_black_dragon

First, I made an excel sheet with a column for the date and for every item offered after the monster is defeated. After each kill, the brutal black dragon drops certain items. After seeing what they were, I would record which items were dropped along with the quantity of each item. 

I have an Airflow DAG that uploads the recorded csv data into S3. From S3, I download the data and connect it to a PostgreSQL database. With the database, one can make SQL queries to learn more from the data. With this project, I used BASH, git, Python, PostgreSQL, GitHub, and Airflow. I am happy with the results and look forward to my next project. 

