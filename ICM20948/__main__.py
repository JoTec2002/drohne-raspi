# Raw magnetometer data (is it accessible over SPI?)
# DPM Data
# Incorporate in Versatile Framework

import time
from ICM20948 import ICM20948
from bus import I2C_Bus





imu = ICM20948()

for i in range(10):
    bus = I2C_Bus()
    imu._setup(bus)

    if imu.AK09916_initialized:
        break
    print(i)


# Print out reading every second
while True:
    print('  '.join(['{:> 7.3}'.format(float(x)) for x in imu.measure()]))
    time.sleep(1)
