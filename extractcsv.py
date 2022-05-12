import pandas as pd
import main

# load the csv file from file location
file = pd.read_csv('i-80_new.csv')

result = main.check_swaps(file)

df = pd.DataFrame.from_records(result, columns=["ID", "Frame", "Local_Y", "Previous_Lane", "New_Lane", "Following"])
df.to_csv("laneswapdata.csv", index=False)
