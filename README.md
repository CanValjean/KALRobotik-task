# KALRobotik-task

In this repository a solution to a problem statement about a robot which contains ultrasonic sensors. The sensor sends data to the robot's software every 100ms. 
The task was to write a function in Python that does the following:

+ Receives a single data point from the sensor each time it is called and stores it. The function should keep track of the last 20 data points it has received.
+ Calculates the average distance of these 20 data points.
+ If the average distance falls below a predefined threshold, let's say 10cm, the robot should stop to avoid a collision. The function should return "Stop".
+ Write a  function that takes a single distance as its argument each time it is called, and returns either "Continue" or "Stop" based on the criteria above. Assume the distance is in centimeters.

To solve this problem, the following three functions were used:

## collect_sensor_data
This function handles the task of receiving a single data point from the sensor and storing it. The function takes two arguments: a single data point and a list of previous data points. The function appends the single data point to the list of previous data points. If the length of the list exceeds 20, the first data point is removed.

## calculate_average_distance
This function is responsible for calculating the average of the last 20 data points. The function takes a list of data points as its argument and returns the average of the last 20 data points.

## navigate_robot
This function uses the average distance to determine whether the robot should "Continue" or "Stop". The function takes two arguments: the average distance and the predefined threshold (in this case, 10cm). If the average distance is less than the threshold, the function returns "Stop". Otherwise, it returns "Continue".

## Sample Inputs
1. [25, 3, 94, 69, 40, 98, 23, 88, 77, 94, 50, 37, 17, 51, 41, 69, 20, 85, 15, 62]
52.9
2. [35, 64, 4, 13, 38, 65, 10, 49, 72, 34, 50, 33, 95, 4, 76, 76, 78, 3, 40, 48]
44.35
3. [15, 97, 91, 52, 33, 57, 4, 71, 7, 6, 58, 34]
43.75
4. [9, 21, 35, 20, 59]
28.8
5. []
0

