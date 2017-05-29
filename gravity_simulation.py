import simulation_interface
import simulation_artist


#INITIAL CONDITIONS
_time_duration = 10 #seconds
_timestep_length = .01 #reccomended = 0.0001
_number_steps = int(_time_duration*10 / _timestep_length)


_mass_list = [1000,1]


_init_pos = [
    [0,0,0],
    [10,0,0]]

_init_vel = [
    [0,0,0],
    [0,10,0]]

_initial_conditions = {'mass':_mass_list,
                      'position':_init_pos,
                      'velocity':_init_vel}


_position_array = simulation_interface.simulate(_time_duration,_initial_conditions)
simulation_artist.render_simulation(_time_duration,_position_array)
