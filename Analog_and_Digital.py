'''
    Demo for analog signal to digital.
    Analog signal is the stream of continous
    data. However,digital signal contains only discreet values of
    voltage or any other parameter. The device that can convert
    analog signal into digital is called : analog-to-digital converter(ADC).
    ADC divides analog signal into small pieces of data. The smaller the piece,
    the closer the approximation of digital signal. On the other hand,
    this require more resourses: memory, electronic devices quality, and etc.
    In this demo the amplitude of the wave means voltage of the signal.
    Hence, this demo disretize the voltage of the analog wave.



    Description:
    sampling: the number of records per second. Meaning, how many times
              per second our device can read the value of time.
              This purely depends on the quality of ADC.
              In this demo, samling defines the number of ticks on X-axis(time).
              For example, if sampling=500. This means ADC reads the wave data
              every 1/500 seconds.
              NOTE: The input magnitude MUST be even number.


    quantization: the number of values the voltage range is divided into.
                  Since digital implies certain values, we can have only certain
                  voltages. For example, if we have oscillating voltage between
                  -5 and 5 volts; and quantization=400. This means that the Y-axis(voltage)
                  will be divided into 400 intervals. Meaning [ 5-(-5)] / 400,
                  which is 1/40.

    Inital values of sampling and quantization are very small. Therefore,
    the error in our example is very great. Increase gradually the values to
    obeserve how the digital signal becomes better.

'''

#### Change sampling rate and quantization rate

# Sampling value must be even number
sampling=40
quantization=24


############# No change below this line #################

if (sampling % 2!=0):
    raise ValueError("The sampling must be even number")

#if (quantization)
omega=20
A=5
period=2*pi/omega
time=arange(0,period, period/2000)

# Create analog graph object
graph_main=graph(title="<b>Analog to Digital</b> ",
                 width=800,
                 height=600,
                 xtitle="Time (s)",
                 ytitle="Voltage (V)")
analog=gcurve(color=color.blue, label="Analog")


# Create graph object



# Create digital graph object
digital=gcurve(color=color.red, label="Digital. S=%s. Q=%s" %(sampling, quantization))
digital.plot(pos=(0,0))
time_digital=arange(0, period+0.5/sampling, 1/sampling)

# Quantize positive A.
# Quantizing only positive A is enough because of symmetry
delta_A=A/(quantization/2)
discreet_A=arange(-A,A+delta_A, delta_A)

# Draw analog graph
for t in time:
    y=A*sin(omega*t)
    analog.plot(pos=(t, y))

y_closest_array=[]
counter=0
for t in time_digital:
    current_y=A*sin(omega*t)

    min_dist=10000
    y_closest=0
    for i in discreet_A:
        if abs(current_y-i)<min_dist:
            min_dist=abs(current_y-i)
            y_closest=i
    y_closest_array.append(y_closest)



for i in range(len(y_closest_array)-1):
    t_1=time_digital[i]
    t_2=time_digital[i+1]
    print(t_1)
    print(t_2)
    y_1=y_closest_array[i]
    y_2=y_closest_array[i+1]

    y_top=max(y_1,y_2)
    digital.plot(pos=(t_1, y_top))
    digital.plot(pos=(t_2, y_top))
