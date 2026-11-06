from TB6612FNG import tb6612xx

drive = tb6612xx(2,3,4,5,7)

drive.foward()
drive.stop()
drive.turn_left()
drive.stop()
drive.turn_right()
drive.reverse()
drive.stop()
drive.deinit()