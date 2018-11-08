GlowScript 2.7 VPython



'''
  Description:
  This is a demo for AM modulated wave formation.
  The carrier signal with no information is combined with a base band wave 
  which carries the neccessary information.
  At any instance of time the amplitude of the resulting wave equals to the 
  sum of instantaneous amplitudes of 2 waves.
  
  Input values:
  A_c: amplitude of carrier signal
  w_c: angular frequency of carrier signal
  
  A_m: amplitude of base band signal
  w_m: angular frequency of base band signal

  Change the values of A_c, w_c, A_m, w_m.
  In particular, observe cases:
    - A_c  >  A_m
    - A_c  <  A_m
    - A_c  =  A_m
  and observe how the resulting graph varies with
  these parameters.



'''



#### Change the input parameters ###################
A_c=10
w_c=40
A_m=20
w_m=5






############## No changes below this line ###########


T_c=2*pi/w_c
T_m=2*pi/w_m
t_limit=max(T_c, T_m)

time=arange(0,1.5*t_limit, 1.5*t_limit/400)

scene_1=canvas(title='Carrier wave', width=800, height=300)

##### Changes for scaling ####
A_c=A_c/40
A_m=A_m/40


x0=time[0]
y0=A_c*sin(w_c*x0)
z0=0

shift=-1
curve_1=curve(pos=vector(shift,y0,z0))

for t in time:

    result=A_c*sin(w_c*t)
    curve_1.append(vector(t+shift, result,0))
    



scene_2=canvas(title='Base band wave',width=800, height=300)


y0=A_m*sin(w_m*x0)
curve_2=curve(pos=vector(shift,y0,z0))

for t in time:

    result=A_m*sin(w_m*t)
    curve_2.append(vector(t+shift, result,0))



scene_3=canvas(title="Result", width=800, height=300)

shift=3*shift

y0=( A_c + A_m*sin(w_m*time[0]))*sin(w_c*time[0])

curve_3=curve(pos=vector(shift,y0,z0))

time=arange(0,5*t_limit, 5*t_limit/500)
for t in time:
    result=(A_c + A_m*sin(w_m*t))*sin(w_c*t)
    curve_3.append(vector(t+shift, result, 0))
