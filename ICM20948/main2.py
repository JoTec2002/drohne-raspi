import time
import board
import adafruit_icm20x

i2c = board.I2C()  # uses board.SCL and board.SDA
icm = adafruit_icm20x.ICM20948(i2c, address=0x68)

while True:
    print(f"Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (icm.acceleration))
    print(f"Gyro X:%.2f, Y: %.2f, Z: %.2f rads/s" % (icm.gyro))
    print(f"Magnetometer X:%.2f, Y: %.2f, Z: %.2f uT" % (icm.magnetic))
    print("")
    time.sleep(0.5)
