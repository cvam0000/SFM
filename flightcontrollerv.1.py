from RPIO import PWM
import time
# initialize servo objects with PWM function
roll = PWM.Servo()
pitch = PWM.Servo()
throttle = PWM.Servo()
yaw = PWM.Servo()
aux = PWM.Servo()
# start PWM on servo specific GPIO no, this is not the pin no but it is the GPIO no 
roll.set_servo(5,1520)# pin 29
pitch.set_servo(6,1520)# pin 31
throttle.set_servo(13,1100)# pin 33
yaw.set_servo(19,1520)# pin 35
aux.set_servo(26,1010)# pin 37, pin 39 is Ground

# assign global min and max values
th_min = 1100
th_max = 2400
r_min = 1100
r_max = 1900
p_min = 1100
p_max = 1900
y_min = 1100
y_max = 1900
a_min = 980
a_max = 2300
th = 1100
r = 1520
p = 1520
y = 1520
a = False
th1 = 0

try:
    while True:
        string = raw_input ('Enter Command: ')
        word = string.split()
        word1 = word[0]
        
        if word1 == 'ARM':
	    th = 1100
            throttle.set_servo(13,th)
            time.sleep(1)
            yaw.set_servo(19,1100)
            time.sleep(1)
            yaw.set_servo(19,1520)
            time.sleep(1)
            print 'System is armed'
            continue

        elif word1 == 'FLY':

            # mapping for MANUAL MODE
            if word[1] == 'MANUAL':
                print 'Flight control: MANUAL'
                try:
                    while True:
                        k = raw_input("FLY: ")
                        # mapping TH = UP
                        if k == 'w':
                            th = th + 10
                            if (th < th_min):
                                throttle.set_servo(13,1100)
                                th = 1100
                            elif (th > th_max):
                                throttle.set_servo(13,2400)
                                th = 2400
                            elif (th > th_min & th < th_max):
                                throttle.set_servo(13,th)
                            print 'TH: ' + str(th)
                            continue

                        # mapping TH = DOWN
                        if k == 's':
                            th = th - 10
                            if (th < th_min):
                                throttle.set_servo(13,1100)
                                th = 1100
                            elif (th > th_max):
                                throttle.set_servo(13,2400)
                                th = 2400
                            elif (th > th_min & th < th_max):
                                throttle.set_servo(13,th)
                            print 'TH: ' + str(th)
                            continue

                        # mapping YA = LEFT
                        if k == 'a':
                            y = y - 10
                            if (y < y_min):
                                yaw.set_servo(19,1100)
                                y = 1100
                            elif (y > y_max):
                                yaw.set_servo(19,1900)
                                y = 1900
                            elif (y > y_min & y < y_max):
                                yaw.set_servo(19,y)
                            print 'YA: ' + str(y)
                            continue

                        # mapping YA = RIGHT
                        if k == 'd':
                            y = y + 10
                            if (y < y_min):
                                yaw.set_servo(19,1100)
                                y = 1100
                            elif (y > y_max):
                                yaw.set_servo(19,1900)
                                y = 1900
                            elif (y > y_min & y < y_max):
                                yaw.set_servo(19,y)
                            print 'YA: ' + str(y)
                            continue

                        # mapping PI = UP
                        elif k == '8':
                            p = p + 10
                            if (p < p_min):
                                pitch.set_servo(6,1100)
                                p = 1100
                            elif (p > p_max):
                                pitch.set_servo(6,1900)
                                p = 1900
                            elif (p > p_min & p < p_max):
                                pitch.set_servo(6,p)
                            print 'PI: ' + str(p)
                            continue
            
                        # mapping PI = DOWN
                        if k == '2':
                            p = p - 10
                            if (p < p_min):
                                pitch.set_servo(6,1100)
                                p = 1100
                            elif (p > p_max):
                                pitch.set_servo(6,1900)
                                p = 1900
                            elif (p > p_min & p < p_max):
                                pitch.set_servo(6,p)
                            print 'PI: ' + str(p)
                            continue

                        # mapping RO = LEFT
                        if k == '4':
                            r = r - 10
                            if (r < r_min):
                                roll.set_servo(5,1100)
                                r = 1100
                            elif (r > r_max):
                                roll.set_servo(5,1900)
                                r = 1900
                            elif (r > r_min & r < r_max):
                                roll.set_servo(5,r)
                            print 'RO: ' + str(r)
                            continue

                        # mapping RO = RIGHT
                        if k == '6':
                            r = r + 10
                            if (r < r_min):
                                roll.set_servo(5,1100)
                                r = 1100
                            elif (r > r_max):
                                roll.set_servo(5,1900)
                                r = 1900
                            elif (r > r_min & r < r_max):
                                roll.set_servo(5,r)
                            print 'RO: ' + str(r)
                            continue

                        # mapping for NO KEY
                        if k == -1:
			    if th1 != th:
                                throttle.set_servo(13,th)
                            else:
                                pass
                            if r != 1520:
                                roll.set_servo(5,1520)
                            else:
                                pass
                            if p !=1520:
                                pitch.set_servo(6,1520)
                            else:
                                pass
                            if y != 1520:
                                yaw.set_servo(19,1520)
                            else:
                                pass
                            th1 = th
                            print 'STABLE'
                            continue

                        # mapping for AUX
                        if k == ' ':
                            a = not(a)
                            if a == True:
                                aux.set_servo(26,2300)
                                print 'Self Level is ON'
                            elif a == False:
                                aux.set_servo(26,980)
                                print 'Self Level is OFF'
                                continue

                        # mapping for BREAK CONDITION
                        if k == 'j':
                            aux.set_servo(26,2300)
                            throttle.set_servo(13,th)
                            roll.set_servo(5,1520)
                            pitch.set_servo(6,1520)
                            yaw.set_servo(19,1520)
                            break
                        
                        else:
                            continue
                                
                except KeyboardInterrupt:
                    pass

        elif word1 == 'DARM':
            throttle.set_servo(13,1100)
            time.sleep(1)
            yaw.set_servo(19,1900)
            time.sleep(1)
            yaw.set_servo(19,1520)
            time.sleep(1)
            print 'System is disarmed'

        elif word1 == 'LAND':
            throttle.set_servo(13,th-10)
            time.sleep(10)
            print 'The Eagle has landed!'
            break
        
        else:
            print 'Wrong Input'
        
        time.sleep(0.1)
            
except KeyboardInterrupt:
	pass

roll.stop_servo(5)
pitch.stop_servo(6)
throttle.stop_servo(13)
yaw.stop_servo(19)
aux.stop_servo(26)
