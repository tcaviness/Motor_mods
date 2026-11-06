from DVR8835 import dvr8835

drive=dvr8835(2, 3, 4, 5, 0, 1)

drive.Mode(1)

drive.Foward(36)
drive.stop()
drive.left(50)
drive.stop()
drive.Backward(34)
drive.stop()
drive.right(50)
drive.stop()
drive.Foward(50)
drive.stop()



