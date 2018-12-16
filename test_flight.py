def transmitter_trims():
    roll.set_servo(5,min_roll)#  set to zero
    pitch.set_servo(6,min_pitch)# set to zero
    throttle.set_servo(13,min_throttle)# set to zero 
    yaw.set_servo(19,min_yaw)  # set to zero
    
def arm():
    throttle.set_servo(13,min_throttle)  #set to zero
    yaw.set_servo(19,max_yaw)  # set to max  (full right yaw)
    ## others to minimun
    print 'Display Armed!!!!' 

def arm_with_self_level_on():
    roll.set_servo(5,max_roll)  ## hold  aileron to right when arming or disarming.
    throttle.set_servo(13,min_throttle)  #set to zero
    yaw.set_servo(19,max_yaw)  # set to max  (full right yaw)
    ## others to minimum
    print 'SElf level on!!!'
    print 'Display Armed!!!!' 
    

def disarm():
    throttle.set_servo(13,min_throttle) # set to zero
    yaw.set_servo(19,min_yaw)  #set to min (full left yaw))
    print 'Display Disarmed!!!!'
    
    
def test_throttle():
    x = raw_input("Enter throttle value: ")
    if(min_throttle <= x and x<=max_throttle):
        throttle.set_servo(13,x)
        
def test_yaw():
    x = raw_input("Enter yaw value: ")
    if(min_yaw <= x and x<=max_yaw):
        yaw.set_servo(19,x)
      
def test_pitch():
    x = raw_input("Enter throttle value: ")
    if(min_pitch <= x and x<=max_pitch):
        pitch.set_servo(6,x)
        
def test_roll():
    x = raw_input("Enter throttle value: ")
    if(min_roll <= x and x<=max_roll):
        roll.set_servo(5,x)
        
        
def set_to_middle():
    roll.set_servo(5,middle_roll)# pin 29
    pitch.set_servo(6,middle_pitch)# pin 31
    throttle.set_servo(13,middle_throttle)# pin 33
    yaw.set_servo(19,middle_yaw)# pin 35
