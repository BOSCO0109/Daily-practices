import pandas as ps 
from io import StringIO

raw_data = '''OrderID, CustomerName, Age, Gender, City, OrderAmount, OrderDate, Status
1001, Alice Johnson, 28, Female, new york, $250.00, 2023-01-15, Delivered
1002, Bob Smith, , Male, Los Angeles, $300, 2023-02-01, delivered
1003,    Charlie Green, 35, male, San Francisco, , 2023-02-05, Returned
1004, Dana White, 42, Female, Chicago, $450.75, 2023-03-10, Delivered
1005, Eve Black, 28, FEMALE,  new york , $200.00, 2023-03-12, Cancelled
1002, Bob Smith, , Male, Los Angeles, $300, 2023-02-01, delivered
1006, Frank Ocean, 30, Male, Miami, $350.00, 2023-04-02, Delivered
1007, Grace Lee, , , Houston, $275.25, , Delivered
1008, Henry Ford, 45, Male, BOSTON, $500.00, 2023-05-01, returned
1009, Isha K, 38, Female, Chicago, $400.00, 2023-05-08, Delivered
'''

read_file = ps.read_csv(StringIO(raw_data))
read_file = read_file.sort_values('OrderID',ascending=True)
read_file.columns = read_file.columns.map(lambda x : x.strip() if isinstance(x,str) else x)
read_file['CustomerName'] = read_file['CustomerName'].str.title()
read_file['Gender'] = read_file['Gender'].str.title()
read_file['OrderAmount'] = read_file['OrderAmount'].replace(r'[\$\\]','',regex=True)
read_file['Status'] = read_file['Status'].str.title()
read_file['City'] = read_file['City'].str.title()
read_file['Age'] = ps.to_numeric(read_file['Age'],errors='coerce')
age_mean = read_file['Age'].mean()
read_file['Age']= read_file['Age'].fillna(age_mean).astype(int)
read_file['OrderAmount'] = ps.to_numeric(read_file['OrderAmount'],errors='coerce')
OrderAmount_mean = read_file['OrderAmount'].mean()
read_file['OrderAmount'] = read_file['OrderAmount'].fillna(OrderAmount_mean).astype(int)

Age_mean_result = read_file['Age'].mean()
Age_max_result = read_file['Age'].max()
Age_min_result = read_file['Age'].min()
order_mean_result = read_file['OrderAmount'].mean()
order_max_result = read_file['OrderAmount'].max()
order_min_result = read_file['OrderAmount'].min()

total_order = len(read_file['OrderAmount'])
print(total_order)
