import psycopg2




conn = psycopg2.connect("""dbname=Salary_Data 
                           user=postgres
                           password=Limbless123
                           host=localhost
                           port=5432
                        """)
