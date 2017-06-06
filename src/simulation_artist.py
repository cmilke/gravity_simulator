import functools
import colorsys
import matplotlib
import matplotlib.pyplot as Plotter
import matplotlib.animation as Animator
from mpl_toolkits.mplot3d import Axes3D


_trail_length_divisor = 50 #make this smaller to make the trail longer


def initialize_render(render_parameters, number_bodies, flat_mode):
    figure = Plotter.figure()
    axes = figure.add_subplot(1,1,1,projection='3d')
    axes.w_xaxis.set_pane_color((0,0,0,0))
    axes.w_yaxis.set_pane_color((0,0,0,0))
    axes.w_zaxis.set_pane_color((0,0,0,0))

    if flat_mode:
        axes.view_init(90,0)
        zmin=-1
        zmax=1

    render_parameters['axes'] = axes
    render_parameters['figure'] = figure


def set_axes_limits(params):
    params['axes'].set_xlim3d(params['x'][0],params['x'][1])
    params['axes'].set_ylim3d(params['y'][0],params['y'][1])
    params['axes'].set_zlim3d(params['z'][0],params['z'][1])
    params['axes'].patch.set_facecolor('black')


def render_image(render_parameters, body_list):
    for i,body in enumerate(body_list):
        x = body[0]
        y = body[1]
        z = body[2]
        color = render_parameters['colors'][i]
        marker = render_parameters['markers'][i]
        set_axes_limits(render_parameters)
        Plotter.plot(x,y,z,color=color,marker=marker)
    Plotter.savefig('image.png')


def animate(visible_step, **kwargs):
    body_list = kwargs['body_list']
    time_duration = kwargs['time_duration']
    render_parameters= kwargs['render_parameters']

    number_steps = len(body_list[0][0])
    number_visible_steps = int(time_duration*10) #ten frames per second
    animation_trail_length = int(number_steps / _trail_length_divisor)

    end = int(visible_step * number_steps / number_visible_steps)
    start = end - animation_trail_length
    if start < 0: start = 0

    Plotter.cla()
    set_axes_limits(render_parameters)

    for i,body in enumerate(body_list):
        x = body[0][start:end]
        y = body[1][start:end]
        z = body[2][start:end]
        color = render_parameters['colors'][i]
        marker = render_parameters['markers'][i]
        render_parameters['axes'].plot(x,y,z,color=color,marker=marker)


def render_animation(time_duration,body_list,render_parameters):
    number_visible_steps = int(time_duration*10) #ten frames per second
    figure = render_parameters['figure']
    animator = functools.partial(animate,
                                 time_duration=time_duration,
                                 body_list=body_list,
                                 render_parameters=render_parameters)

    pretty_animation = Animator.FuncAnimation(figure,animator,
                        number_visible_steps,interval=100,blit=False)
    pretty_animation.save('animation.mp4')


def visualize_simulation(time_duration, body_list, render_parameters):
    animate_mode = render_parameters['animate mode']
    flat_mode = render_parameters['flat mode']

    number_bodies = len(body_list)
    initialize_render(render_parameters,number_bodies,flat_mode)
    render_image(render_parameters,body_list)
    if animate_mode:
        render_animation(time_duration,body_list,render_parameters)
    print('Simulation rendered, program complete.')
