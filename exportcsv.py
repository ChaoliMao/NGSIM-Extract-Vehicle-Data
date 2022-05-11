import pandas as pd
import main

# load the csv file from file location
file = pd.read_csv('i-80_new.csv')

result = main.find_relationship(file)

df = pd.DataFrame.from_records(result, columns=["ID", "Frame", "Ego_Vehicle_Class", "Ego_Vehicle_X", "Ego_Vehicle_Y",
                                                "Ego_Vehicle_Vel", "Ego_Vehicle_Acc", "Front_Vehicle_Class",
                                                "Front_Vehicle_X", "Front_Vehicle_Y", "Front_Vehicle_Vel",
                                                "Front_Vehicle_Acc", "Left_Vehicle1_ID", "Left_Vehicle1_Class", "Left_Vehicle1_X",
                                                "Left_Vehicle1_Y", "Left_Vehicle1_Vel", "Left_Vehicle1_Acc",
                                                "Left_Vehicle1_Lane", "Left_Vehicle2_ID", "Left_Vehicle2_Class", "Left_Vehicle2_X",
                                                "Left_Vehicle2_Y", "Left_Vehicle2_Vel", "Left_Vehicle2_Acc",
                                                "Left_Vehicle2_Lane", "Left_Vehicle3_ID", "Left_Vehicle3_Class", "Left_Vehicle3_X",
                                                "Left_Vehicle3_Y", "Left_Vehicle3_Vel", "Left_Vehicle3_Acc",
                                                "Left_Vehicle3_Lane", "Right_Vehicle1_ID", "Right_Vehicle1_Class", "Right_Vehicle1_X",
                                                "Right_Vehicle1_Y", "Right_Vehicle1_Vel", "Right_Vehicle1_Acc",
                                                "Right_Vehicle1_Lane", "Right_Vehicle2_ID", "Right_Vehicle2_Class", "Right_Vehicle2_X",
                                                "Right_Vehicle2_Y", "Right_Vehicle2_Vel", "Right_Vehicle2_Acc",
                                                "Right_Vehicle2_Lane", "Right_Vehicle3_ID", "Right_Vehicle3_Class", "Right_Vehicle3_X",
                                                "Right_Vehicle3_Y", "Right_Vehicle3_Vel", "Right_Vehicle3_Acc",
                                                "Right_Vehicle3_Lane"])
df.to_csv("i-80_extracted_1.csv", index=False)
