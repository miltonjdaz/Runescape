# Airflow DAG: loads S3 data into Postgres database

I've had this project in mind for a while. I wanted to combine my tech skills with an easy everyday occurrence. I had not played Old School Runescape in a while but I knew I could get a consistent amount of data from killing the same monster in the game and record the different drops it provides. I decided on brutal black dragons because they have 59 unique drops to be recorded. 

I have an Airflow DAG that uploads the recorded csv data into S3. From S3, I download the data and connect it to a PostgreSQL database. With the database, one can make SQL queries to learn more from the data. With this project, I used BASH, git, Python, PostgreSQL, GitHub, and Airflow. I am happy with the results and look forward to my next project. 

