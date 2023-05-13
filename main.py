def collect_sensor_data(single_data, data_points):
    # This function handles the task of receiving a single data point from the sensor and storing it.

    data_points.append(single_data)

    if len(data_points) > 20:
        data_points.pop(0)

    return data_points


def calculate_average_distance(data_points):
    # This function is responsible for calculating the average of the last 20 data points.

    if len(data_points) == 0:
        return 0
    # preventing ZeroDivisionError
    else:
        average_distance = sum(data_points) / len(data_points)
    return average_distance


def navigate_robot(single_data, threshold):
    data_points = collect_sensor_data(single_data, navigate_robot.data_points)
    navigate_robot.data_points = data_points

    average_distance = calculate_average_distance(data_points)

    if average_distance > threshold:
        return "Stop"

    else:
        return "Continue"


# Initialize the data_points attribute of navigate_robot function
navigate_robot.data_points = []
