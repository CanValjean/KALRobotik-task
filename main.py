def collect_sensor_data(single_data, data_points):
    # This function handles the task of receiving a single data point from the sensor and storing it.

    data_points.append(single_data)

    if len(data_points) > 20:
        data_points.pop(0)

    return data_points
