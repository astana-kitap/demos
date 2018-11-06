GlowScript 2.7 VPython

'''
    Perdiod and Frequency Demo
    This script is to demonstrate difference between
    perdoid and frequency.
    Change the value of f_red on line 15.
    Change the value of T_green on line 19.
    Then, observe how oscillations changes.
    
'''

#### Frequency(Hz) of the RED ball
# NOT GREATER THAN 400 Hz. Otherwise animation will not work
f_red=4


#### Period(s) of the GREEN ball ###########
T_green= 1





##################################################################

# Draw coordinate plane axes
x_axis=arrow( pos=vector(-3,0,0), axis=vector(6,0,0),shaftwidth=0.05)
y_axis=arrow( pos=vector(0,0,0), axis=vector(0,3,0),shaftwidth=0.05)
z_axis=arrow( pos=vector(0,0,0), axis=vector(0,0,3),shaftwidth=0.05)

# Define objects
ball_1=sphere(pos=vector(-2,0,0), radius=0.5, color=color.red)
ball_2=sphere(pos=vector(2,0,0), radius=0.5, color=color.green)


# Define angular frequencies
w_1=2*pi*f_red
w_2=2*pi/T_green

#Define amplitudes
A1=3
A2=3


#time settings
t=0
dt=0.001


# start animation
while True:
    rate(40)
    t=t+dt
    ball_1.pos.y= A1*sin(w_1*t)  
    ball_2.pos.y= A2*sin(w_2*t)

