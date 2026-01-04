import pandas as pd


data =( input('name>'),input('power>'),input('address>') ,input('91+>'),input('Gmail ID>')   )  

series = pd.Series(data, index=['1.','2.','3.','4.','5.',])
print(series)



