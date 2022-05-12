import pandas as pd


def check_swaps(file):
    previous_lane = file["Lane_ID"][0]
    previous_vehicle_id = file["Vehicle_ID"][0]
    previous_following_vehicle = file["Following"][0]
    data = []
    for i in range(1, len(file)):
        current_lane = file["Lane_ID"][i]
        current_vehicle_id = file["Vehicle_ID"][i]
        current_following_vehicle = file["Following"][i]

        if current_vehicle_id == previous_vehicle_id:
            if previous_lane == current_lane:
                previous_following_vehicle = current_following_vehicle
                pass
            else:
                # print("Lane change occured by vehicle", file["Vehicle_ID"][i], "in frames", file["Frame_ID"][i - 1],
                #       "from lanes", previous_lane, "to", current_lane, previous_following_vehicle,
                #       current_following_vehicle)
                data.append([
                    file["Vehicle_ID"][i],
                    file["Frame_ID"][i - 1],
                    file["Local_Y"][i - 1],
                    previous_lane,
                    current_lane,
                    current_following_vehicle
                ])
                previous_lane = current_lane
                previous_following_vehicle = current_following_vehicle
        else:
            previous_lane = current_lane
            previous_vehicle_id = current_vehicle_id

        # print(file["Frame_ID"][i], previous_vehicle_id, previous_lane, current_vehicle_id, current_lane)

    return data


if __name__ == "__main__":
    i80 = pd.read_csv("i-80_new.csv")
    result = check_swaps(i80)
    print(len(result))
