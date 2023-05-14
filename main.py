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


def navigate_robot(single_data, threshold=10):
    # This function could use the average distance to determine whether the robot should "Continue" or "Stop".
    data_points = collect_sensor_data(single_data, navigate_robot.data_points)
    navigate_robot.data_points = data_points

    average_distance = calculate_average_distance(data_points)

    if average_distance <= threshold:
        return "Stop"

    else:
        return "Continue"


# Initialize the data_points attribute of navigate_robot function
navigate_robot.data_points = []

# Sample Inputs

sample1 = [25, 3, 94, 69, 40, 98, 23, 88, 77, 94, 50, 37, 17, 51, 41, 69, 20, 85, 15, 62]
# average = 52.9
sample2 = [35, 64, 4, 13, 38, 65, 10, 49, 72, 34, 50, 33, 95, 4, 76, 76, 78, 3, 40, 48]
# average = 44.35
sample3 = [15, 97, 91, 52, 33, 57, 4, 71, 7, 6, 58, 34]
# average = 43.75
sample4 = [9, 21, 35, 20, 59]
# average = 28.8
sample5 = []


# average = 0

# testing Sample Inputs
def sample_test_collect_sensor_data(data_list, data_points):
    # This function handles the task of receiving a sensor data list from the sensor and storing it.

    for single_data in data_list:
        data_points.append(single_data)

    if len(data_points) > 20:
        data_points.pop(0)

    return data_points


def sample_test_navigate_robot(data_list, threshold=10):
    # This function is responsible for calculating the average of the last 20 data points of the data list
    sample_test_navigate_robot.data_points = []

    data_points = sample_test_collect_sensor_data(data_list, sample_test_navigate_robot.data_points)
    sample_test_navigate_robot.data_points = data_points

    average_distance = calculate_average_distance(data_points)

    print(average_distance)

    if average_distance <= threshold:
        return "Stop"

    else:
        return "Continue"


print(sample_test_navigate_robot(sample1))
print(sample_test_navigate_robot(sample2))
print(sample_test_navigate_robot(sample3))
print(sample_test_navigate_robot(sample4))
print(sample_test_navigate_robot(sample5))
