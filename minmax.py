import numpy as np
import pandas as pd
data={
    'name':['ram','sita','gita','retu','invalid'],
    'age':[30,40,45,50,65]
}
df=pd.DataFrame(data)
print("Original data/n")
print(df)
invalid_data=df[df['name'].str.contains('invalid',case=False,na=False)]
print(invalid_data)
