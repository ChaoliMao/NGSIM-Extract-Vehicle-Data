import pandas as pd


def obtain_y(i80, file):
    data = []
    for i in range(len(file)):
        if file["Following"][i] == 0:
            # data.append([
            #     file["ID"][i],
            #     file["Frame"][i],
            #     file["Local_Y"][i],
            #     file["Previous_Lane"][i],
            #     file["New_Lane"][i],
            #     file["Following"][i],
            #     0
            # ])
            continue
        else:
            test = i80[
                (i80["Vehicle_ID"] == file["Following"][i]) &
                (i80["Frame_ID"] == file["Frame"][i])
            ]
            if len(test) == 0:
                # data.append([
                #     file["ID"][i],
                #     file["Frame"][i],
                #     file["Local_Y"][i],
                #     file["Previous_Lane"][i],
                #     file["New_Lane"][i],
                #     file["Following"][i],
                #     0
                # ])
                continue
            else:
                data.append([
                    file["ID"][i],
                    file["Frame"][i],
                    file["Local_Y"][i],
                    file["Previous_Lane"][i],
                    file["New_Lane"][i],
                    file["Following"][i],
                    test["Local_Y"].item()
                ])
    return data


if __name__ == "__main__":
    i80 = pd.read_csv("i-80_new.csv")
    swap_data = pd.read_csv("laneswapdata.csv")
    result = obtain_y(i80, swap_data)
    print(result)
