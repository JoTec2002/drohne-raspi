from defines import *

try:
    from smbus2 import SMBus

    class I2C_Bus:
        def __init__(self):
            '''
            Setup I2C
            '''
            
            self._acc = SMBus(I2C_PORT)


        def ReadReg(self, reg: int) -> int:
            '''
            Read register value

            :param reg: register to read

            :returns: register value
            '''

            # TODO: Looks like READ_FLAG is not needed for I2C
            return self._acc.read_byte_data(ICM20948_I2C_ADDRESS, reg)


        def ReadRegs(self, reg: int, cnt: int) -> list:
            '''
            Read consecutive cnt registers

            :param reg: First register to read
            :param cnt: number of register values to read

            :returns: list of register values
            '''

            return self._acc.read_i2c_block_data(ICM20948_I2C_ADDRESS, reg, cnt)


        def WriteReg(self, reg: int, data: int) -> None:
            '''
            Write registers value

            :param data:
            :param reg: register to write to
            :oaram data: data byte to write
            '''

            self._acc.write_byte_data(ICM20948_I2C_ADDRESS, reg, data)


        def WriteRegs(self, reg: int, data: list) -> None:
            '''
            Write consecutive cnt registers

            :param reg: First register to write to
            :oaram data: list of data byte to write
            '''

            self._acc.write_i2c_block_data(ICM20948_I2C_ADDRESS, reg, data)

except ImportError:
    print("Warning: smbus not installed")