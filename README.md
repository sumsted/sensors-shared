**Sensor Shared**

Use memory map to share sensor data with the robot code. Ultrasonic sensors take time to read, ~100ms each.  To prevent blocking in the robot control code use shared memory to shre the last read data.

**sensor.py** shows how you could read sensors and push the results to shared memory

**sensor_client.py** shows how to read and process the results