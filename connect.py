import pyodbc


conn = pyodbc.connect('DRIVER={SQL Server};SERVER=limbdev.database.windows.net,1433',
                      user='limbdevazure',
                      password='Limbless123',
                      database='limb_base_beta')


# Note conn val is in connect.py, which is gitignored to prevent publishing login to server