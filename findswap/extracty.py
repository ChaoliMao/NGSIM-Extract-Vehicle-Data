import pandas as pd
import obtainYy

# load the csv file from file location
i80 = pd.read_csv("i-80_new.csv")
swap_data = pd.read_csv("laneswapdata.csv")
result = ObtainY.obtain_y(i80, swap_data)

df = pd.DataFrame.from_records(result, columns=["ID", "Frame", "Local_Y", "Previous_Lane", "New_Lane", "Following",
                                                "Following_Y"])
df.to_csv("swapdata.csv", index=False)
