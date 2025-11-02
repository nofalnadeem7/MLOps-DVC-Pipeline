import pandas as pd 
import os 

data={'Name':["Thomas","Grace","Arthur",'John','Ada'],
      'Age':[40,30,45,35,50],
      'Gender':["Male",'Female',"Male","Male","Female"]}

df=pd.DataFrame(data)

data_dir='data'

os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,"sample_data.csv")

df.to_csv(file_path,index=False)

print(f"data saved to sample_data.csv")