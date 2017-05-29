import math
import ctypes
import colorsys
import numpy
import matplotlib
import matplotlib.pyplot as Plotter
import matplotlib.animation as Animator
from mpl_toolkits.mplot3d import Axes3D

simulation_engine = ctypes.CDLL('/home/cmilke/Documents/physics_masters/classical/gravity_simulator/simulation_engine.so')
simulation_engine.get_error.restype = ctypes.c_double

#INITIAL CONDITIONS
number_bodies = 2
number_dimensions = 3
time_duration = 300 #in tenths of a second
timestep_length = .01 #reccomended = 0.0001
number_steps = int(time_duration / timestep_length)
number_visible_steps = int(time_duration) #ten frames per second

trail_length_divisor = 50 #make this smaller to make the trail longer
animation_trail_length = int(number_steps / trail_length_divisor)
static_mode = False
flat_mode = True
show_energy_errors = True

xmin=-20
xmax=+20
ymin=-20
ymax=+20
zmin=-20
zmax=+20

mass_list = [1000,1]


init_pos = [
    [0,0,0],
    [10,0,0]]

init_vel = [
    [0,0,0],
    [0,10,0]]



def run_gravity_simulation_engine():
    c_timestep_length = ctypes.c_double(timestep_length)
    masses = (ctypes.c_double * number_bodies)()
    c_init_pos  = (ctypes.c_double * number_dimensions * number_bodies)()
    c_init_vel = (ctypes.c_double * number_dimensions * number_bodies)()
    for body in range(0,number_bodies):
        masses[body] = mass_list[body]
        for comp in range(0,number_dimensions):
            c_init_pos[body][comp] = init_pos[body][comp]
            c_init_vel[body][comp] = init_vel[body][comp]

    body_array = ctypes.pointer(ctypes.pointer(ctypes.pointer(ctypes.c_double())))
    print("Running simulation engine...")
    simulation_engine.run(number_bodies,number_dimensions,number_steps,
                          c_timestep_length,masses, 
                          c_init_pos,c_init_vel,ctypes.byref(body_array))
    print("Engine finished, transferring data...")


    body_list = []
    for i in range(0,number_bodies):
        dimension_list = []
        for j in range(0,number_dimensions):
            step_list = []
            for k in range(0,number_steps):
                step_list.append(body_array[i][j][k])
            dimension_list.append(step_list)
        body_list.append(dimension_list)

    ("Data transfer complete, rendering...")
    return body_list




def render_simulation(body_list):
    figure = Plotter.figure()
    axes = figure.add_subplot(1,1,1,projection='3d')

    if flat_mode:
        axes.view_init(90,0)
        zmin=-1
        zmax=1



    colors = []
    for i in range(0,number_bodies):
        luminosity = 0.5
        saturation = 1
        hue = i / float(number_bodies)
        rgbcolor = colorsys.hls_to_rgb(hue,luminosity,saturation)
        hexcolor = matplotlib.colors.to_hex(rgbcolor)
        colors.append(hexcolor)

    def animate(visible_step):
        end = int(visible_step * number_steps / number_visible_steps)
        start = end - animation_trail_length
        if start < 0: start = 0

        Plotter.cla()
        axes.set_xlim3d(xmin,xmax)
        axes.set_ylim3d(ymin,ymax)
        axes.set_zlim3d(zmin,zmax)
        if show_energy_errors:
            error = simulation_engine.get_error(visible_step);
            error_text = str.format('{0:.10f}',error)
            axes.text2D(0.0, 0.9, error_text, fontsize=20, transform=axes.transAxes)

        for i,body in enumerate(body_list):
            x = body[0][start:end]
            y = body[1][start:end]
            z = body[2][start:end]
            color = colors[i]
            axes.plot(x,y,z,color)


    for i,body in enumerate(body_list):
        x = body[0]
        y = body[1]
        z = body[2]
        color = colors[i]
        axes.set_xlim3d(xmin,xmax)
        axes.set_ylim3d(ymin,ymax)
        axes.set_zlim3d(zmin,zmax)
        Plotter.plot(x,y,z,color)
    Plotter.savefig('image.png')
    if not static_mode:
        pretty_animation = Animator.FuncAnimation(figure,animate,
                            number_visible_steps,interval=100,blit=False)
        pretty_animation.save('animation.mp4')



body_position_array = run_gravity_simulation_engine()
render_simulation(body_position_array)
