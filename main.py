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
        average = sum(data_points) / len(data_points)
    return average
