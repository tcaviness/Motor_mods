from DVR8833 import drv8833


drive = drv8833(5, 6, 7, 8)

drive.foward(50)
drive.stop()

drive.reverse(50)
drive.stop()

drive.motor_a(35, 1)
drive.stop()

drive.motor_b(50, 0)
drive.stop()
