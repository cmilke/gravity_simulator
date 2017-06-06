from src import simulation_condition_reader
from src import simulation_interface
from src import simulation_artist

time_duration = 10 #seconds
timestep_length = .001 #reccomended = 0.0001

initial_conditions,colors,markers = simulation_condition_reader.read('initial_conditions.dat')
render_parameters = {'x':[-10,10],
                     'y':[-10,10],
                     'z':[-10,10],
                     'animate mode':True,
                     'flat mode':True,
                     'colors':colors,
                     'markers':markers}

position_array = simulation_interface.simulate(time_duration,timestep_length,initial_conditions)
simulation_artist.visualize_simulation(time_duration,position_array,render_parameters)
