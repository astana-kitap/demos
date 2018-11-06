GlowScript 2.7 VPython


#Change omega value
omega=1
amplitude=5






##############################################################
x_axis=arrow(pos=vector(0,1.5,0), axis=vector(amplitude+2,0,0), shaftwidth=0.05)
y_axis=arrow(pos=vector(0,1.5,0), axis=vector(0,amplitude+2,0), shaftwidth=0.05)


ball=sphere(pos=vector(amplitude,1.5,0), radius=0.3, 
            color=color.green, make_trail=True)



square =box(pos=vector(amplitude,-(amplitude+2),0 ), size=vector(1,1,1))

distance=square.pos.x+amplitude+3

spring=helix(pos=vector(-(amplitude+3),-(amplitude+2),0), 
             axis=vector(distance,0,0),
             radius=0.5, coils=15)

wall=box(pos=vector(-(amplitude+3),-(amplitude+2),0), size=vector(0.1, 3,3) )

t=0
dt=0.005



while True:
    rate(300)
    ball.rotate(angle=omega*dt, axis=vector(0,0,1), origin=vector(0,1.5,0))
    t=t+dt
    square.pos.x=amplitude*cos(omega*t)
    spring.axis=square.pos-spring.pos
    
    
