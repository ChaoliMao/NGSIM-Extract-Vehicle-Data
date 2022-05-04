import pandas as pd
import detect_vehicles


def find_relationship(file):
    # initialize values
    right_vehicle = None
    left_vehicle = None
    left_vehicle1_class = 0
    left_vehicle1_x_position = 0
    left_vehicle1_y_position = 0
    left_vehicle1_velocity = 0
    left_vehicle1_acceleration = 0
    left_vehicle2_class = 0
    left_vehicle2_x_position = 0
    left_vehicle2_y_position = 0
    left_vehicle2_velocity = 0
    left_vehicle2_acceleration = 0
    left_vehicle3_class = 0
    left_vehicle3_x_position = 0
    left_vehicle3_y_position = 0
    left_vehicle3_velocity = 0
    left_vehicle3_acceleration = 0
    right_vehicle1_class = 0
    right_vehicle1_x_position = 0
    right_vehicle1_y_position = 0
    right_vehicle1_velocity = 0
    right_vehicle1_acceleration = 0
    right_vehicle2_class = 0
    right_vehicle2_x_position = 0
    right_vehicle2_y_position = 0
    right_vehicle2_velocity = 0
    right_vehicle2_acceleration = 0
    right_vehicle3_class = 0
    right_vehicle3_x_position = 0
    right_vehicle3_y_position = 0
    right_vehicle3_velocity = 0
    right_vehicle3_acceleration = 0
    data = []

    for i in range(len(file)):
        # need current lane of ego vehicle to figure out which lanes are next to it
        current_lane = file["Lane_ID"][i]

        # detect whether you are following a vehicle
        front_vehicle = detect_vehicles.sense_front_vehicle(i, file)

        # obtain data on the vehicle in front
        if type(front_vehicle) == int:  # there are no vehicles ahead
            front_vehicle_class = 0
            front_vehicle_x_position = 0
            front_vehicle_y_position = 0
            front_vehicle_velocity = 0
            front_vehicle_acceleration = 0
        else:   # there is a vehicle ahead
            front_vehicle_class = front_vehicle["v_Class"].item()
            front_vehicle_x_position = front_vehicle["Local_X"].item()
            front_vehicle_y_position = front_vehicle["Local_Y"].item()
            front_vehicle_velocity = front_vehicle["v_Vel"].item()
            front_vehicle_acceleration = front_vehicle["v_Acc"].item()

        # left-most lane. There will be no vehicles on the left of the ego vehicle.
        if current_lane != 1:
            left_vehicle = detect_vehicles.sense_vehicle_on_left(current_lane, i, front_vehicle_y_position, file)

        # obtain data for the vehicles on the left depending on how many vehicles there are
        if type(left_vehicle) == int:  # zero vehicles on the left
            left_vehicle1_class = 0
            left_vehicle1_x_position = 0
            left_vehicle1_y_position = 0
            left_vehicle1_velocity = 0
            left_vehicle1_acceleration = 0

            left_vehicle2_class = 0
            left_vehicle2_x_position = 0
            left_vehicle2_y_position = 0
            left_vehicle2_velocity = 0
            left_vehicle2_acceleration = 0

            left_vehicle3_class = 0
            left_vehicle3_x_position = 0
            left_vehicle3_y_position = 0
            left_vehicle3_velocity = 0
            left_vehicle3_acceleration = 0
        elif len(left_vehicle) == 1:  # one vehicle on the left
            left_vehicle1_class = left_vehicle["v_Class"].item()
            left_vehicle1_x_position = left_vehicle["Local_X"].item()
            left_vehicle1_y_position = left_vehicle["Local_Y"].item()
            left_vehicle1_velocity = left_vehicle["v_Vel"].item()
            left_vehicle1_acceleration = left_vehicle["v_Acc"].item()

            left_vehicle2_class = 0
            left_vehicle2_x_position = 0
            left_vehicle2_y_position = 0
            left_vehicle2_velocity = 0
            left_vehicle2_acceleration = 0

            left_vehicle3_class = 0
            left_vehicle3_x_position = 0
            left_vehicle3_y_position = 0
            left_vehicle3_velocity = 0
            left_vehicle3_acceleration = 0
        else:  # more than one vehicle on the left
            for j in range(0, len(left_vehicle)):
                if len(left_vehicle) == 2:  # two vehicles on the left
                    left_vehicle1_class = left_vehicle["v_Class"][left_vehicle.iloc[0].name]
                    left_vehicle1_x_position = left_vehicle["Local_X"][left_vehicle.iloc[0].name]
                    left_vehicle1_y_position = left_vehicle["Local_Y"][left_vehicle.iloc[0].name]
                    left_vehicle1_velocity = left_vehicle["v_Vel"][left_vehicle.iloc[0].name]
                    left_vehicle1_acceleration = left_vehicle["v_Acc"][left_vehicle.iloc[0].name]

                    left_vehicle2_class = left_vehicle["v_Class"][left_vehicle.iloc[1].name]
                    left_vehicle2_x_position = left_vehicle["Local_X"][left_vehicle.iloc[1].name]
                    left_vehicle2_y_position = left_vehicle["Local_Y"][left_vehicle.iloc[1].name]
                    left_vehicle2_velocity = left_vehicle["v_Vel"][left_vehicle.iloc[1].name]
                    left_vehicle2_acceleration = left_vehicle["v_Acc"][left_vehicle.iloc[1].name]

                    left_vehicle3_class = 0
                    left_vehicle3_x_position = 0
                    left_vehicle3_y_position = 0
                    left_vehicle3_velocity = 0
                    left_vehicle3_acceleration = 0

                elif len(left_vehicle) == 3:  # three vehicles on the left
                    left_vehicle1_class = left_vehicle["v_Class"][left_vehicle.iloc[0].name]
                    left_vehicle1_x_position = left_vehicle["Local_X"][left_vehicle.iloc[0].name]
                    left_vehicle1_y_position = left_vehicle["Local_Y"][left_vehicle.iloc[0].name]
                    left_vehicle1_velocity = left_vehicle["v_Vel"][left_vehicle.iloc[0].name]
                    left_vehicle1_acceleration = left_vehicle["v_Acc"][left_vehicle.iloc[0].name]

                    left_vehicle2_class = left_vehicle["v_Class"][left_vehicle.iloc[1].name]
                    left_vehicle2_x_position = left_vehicle["Local_X"][left_vehicle.iloc[1].name]
                    left_vehicle2_y_position = left_vehicle["Local_Y"][left_vehicle.iloc[1].name]
                    left_vehicle2_velocity = left_vehicle["v_Vel"][left_vehicle.iloc[1].name]
                    left_vehicle2_acceleration = left_vehicle["v_Acc"][left_vehicle.iloc[1].name]

                    left_vehicle3_class = left_vehicle["v_Class"][left_vehicle.iloc[2].name]
                    left_vehicle3_x_position = left_vehicle["Local_X"][left_vehicle.iloc[2].name]
                    left_vehicle3_y_position = left_vehicle["Local_Y"][left_vehicle.iloc[2].name]
                    left_vehicle3_velocity = left_vehicle["v_Vel"][left_vehicle.iloc[2].name]
                    left_vehicle3_acceleration = left_vehicle["v_Acc"][left_vehicle.iloc[2].name]

        # right-most lane. There will be no vehicles on the right of the ego vehicle.
        if current_lane != 7:
            right_vehicle = detect_vehicles.sense_vehicle_on_right(current_lane, i, front_vehicle_y_position, file)

        # obtain data for the vehicles on the right depending on how many vehicles there are
        if type(right_vehicle) == int:  # zero vehicles on the right
            right_vehicle1_class = 0
            right_vehicle1_x_position = 0
            right_vehicle1_y_position = 0
            right_vehicle1_velocity = 0
            right_vehicle1_acceleration = 0

            right_vehicle2_class = 0
            right_vehicle2_x_position = 0
            right_vehicle2_y_position = 0
            right_vehicle2_velocity = 0
            right_vehicle2_acceleration = 0

            right_vehicle3_class = 0
            right_vehicle3_x_position = 0
            right_vehicle3_y_position = 0
            right_vehicle3_velocity = 0
            right_vehicle3_acceleration = 0
        elif len(right_vehicle) == 1:   # one vehicle on the right
            right_vehicle1_class = right_vehicle["v_Class"].item()
            right_vehicle1_x_position = right_vehicle["Local_X"].item()
            right_vehicle1_y_position = right_vehicle["Local_Y"].item()
            right_vehicle1_velocity = right_vehicle["v_Vel"].item()
            right_vehicle1_acceleration = right_vehicle["v_Acc"].item()

            right_vehicle2_class = 0
            right_vehicle2_x_position = 0
            right_vehicle2_y_position = 0
            right_vehicle2_velocity = 0
            right_vehicle2_acceleration = 0

            right_vehicle3_class = 0
            right_vehicle3_x_position = 0
            right_vehicle3_y_position = 0
            right_vehicle3_velocity = 0
            right_vehicle3_acceleration = 0
        else:   # more than one vehicle on the right
            for j in range(0, len(right_vehicle)):
                if len(right_vehicle) == 2:     # two vehicles on the right
                    right_vehicle1_class = right_vehicle["v_Class"][right_vehicle.iloc[0].name]
                    right_vehicle1_x_position = right_vehicle["Local_X"][right_vehicle.iloc[0].name]
                    right_vehicle1_y_position = right_vehicle["Local_Y"][right_vehicle.iloc[0].name]
                    right_vehicle1_velocity = right_vehicle["v_Vel"][right_vehicle.iloc[0].name]
                    right_vehicle1_acceleration = right_vehicle["v_Acc"][right_vehicle.iloc[0].name]

                    right_vehicle2_class = right_vehicle["v_Class"][right_vehicle.iloc[1].name]
                    right_vehicle2_x_position = right_vehicle["Local_X"][right_vehicle.iloc[1].name]
                    right_vehicle2_y_position = right_vehicle["Local_Y"][right_vehicle.iloc[1].name]
                    right_vehicle2_velocity = right_vehicle["v_Vel"][right_vehicle.iloc[1].name]
                    right_vehicle2_acceleration = right_vehicle["v_Acc"][right_vehicle.iloc[1].name]

                    right_vehicle3_class = 0
                    right_vehicle3_x_position = 0
                    right_vehicle3_y_position = 0
                    right_vehicle3_velocity = 0
                    right_vehicle3_acceleration = 0

                elif len(right_vehicle) == 3:   # three vehicles on the right
                    right_vehicle1_class = right_vehicle["v_Class"][right_vehicle.iloc[0].name]
                    right_vehicle1_x_position = right_vehicle["Local_X"][right_vehicle.iloc[0].name]
                    right_vehicle1_y_position = right_vehicle["Local_Y"][right_vehicle.iloc[0].name]
                    right_vehicle1_velocity = right_vehicle["v_Vel"][right_vehicle.iloc[0].name]
                    right_vehicle1_acceleration = right_vehicle["v_Acc"][right_vehicle.iloc[0].name]

                    right_vehicle2_class = right_vehicle["v_Class"][right_vehicle.iloc[1].name]
                    right_vehicle2_x_position = right_vehicle["Local_X"][right_vehicle.iloc[1].name]
                    right_vehicle2_y_position = right_vehicle["Local_Y"][right_vehicle.iloc[1].name]
                    right_vehicle2_velocity = right_vehicle["v_Vel"][right_vehicle.iloc[1].name]
                    right_vehicle2_acceleration = right_vehicle["v_Acc"][right_vehicle.iloc[1].name]

                    right_vehicle3_class = right_vehicle["v_Class"][right_vehicle.iloc[2].name]
                    right_vehicle3_x_position = right_vehicle["Local_X"][right_vehicle.iloc[2].name]
                    right_vehicle3_y_position = right_vehicle["Local_Y"][right_vehicle.iloc[2].name]
                    right_vehicle3_velocity = right_vehicle["v_Vel"][right_vehicle.iloc[2].name]
                    right_vehicle3_acceleration = right_vehicle["v_Acc"][right_vehicle.iloc[2].name]

        data.append([
            (file["Vehicle_ID"][i]),
            (file["v_Class"][i]),
            (file["Local_X"][i]),
            (file["Local_Y"][i]),
            (file["v_Vel"][i]),
            (file["v_Acc"][i]),
            front_vehicle_class,
            front_vehicle_x_position,
            front_vehicle_y_position,
            front_vehicle_velocity,
            front_vehicle_acceleration,
            left_vehicle1_class,
            left_vehicle1_x_position,
            left_vehicle1_y_position,
            left_vehicle1_velocity,
            left_vehicle1_acceleration,
            left_vehicle2_class,
            left_vehicle2_x_position,
            left_vehicle2_y_position,
            left_vehicle2_velocity,
            left_vehicle2_acceleration,
            left_vehicle3_class,
            left_vehicle3_x_position,
            left_vehicle3_y_position,
            left_vehicle3_velocity,
            left_vehicle3_acceleration,
            right_vehicle1_class,
            right_vehicle1_x_position,
            right_vehicle1_y_position,
            right_vehicle1_velocity,
            right_vehicle1_acceleration,
            right_vehicle2_class,
            right_vehicle2_x_position,
            right_vehicle2_y_position,
            right_vehicle2_velocity,
            right_vehicle2_acceleration,
            right_vehicle3_class,
            right_vehicle3_x_position,
            right_vehicle3_y_position,
            right_vehicle3_velocity,
            right_vehicle3_acceleration
        ])

    return data


if __name__ == "__main__":

    # load the csv file from file location
    i80 = pd.read_csv('i-80_new.csv')

    result = find_relationship(i80)
    print(result)
