import simulation_condition_reader
import simulation_interface
import simulation_artist

time_duration = 10 #seconds
timestep_length = .01 #reccomended = 0.0001

render_parameters = {'x':[-20,20],
                      'y':[-20,20],
                      'z':[-20,20],
                      'animate mode':True,
                      'flat mode':False}


initial_conditions = simulation_condition_reader.read()
position_array = simulation_interface.simulate(time_duration,initial_conditions)
simulation_artist.visualize_simulation(time_duration,position_array,render_parameters)
