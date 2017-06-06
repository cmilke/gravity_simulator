_gravitational_constant = 6.674e-11
_distance_scale_factor = 1e-9
_period_scale_factor = 5e-5
_velocity_scale_factor = _distance_scale_factor / _period_scale_factor
_mass_scale_factor = _gravitational_constant * ( _distance_scale_factor**3 / _period_scale_factor**2 )



def read(conditions_file_name):
    conditions_file = open(conditions_file_name,'r')

    mass_list = [] 
    init_pos = []
    init_vel = []
    colors = []
    markers = []
    for line in conditions_file.readlines()[1:]:
        split_line = line.split(';')
        mass_string = split_line[0]
        position_strings = split_line[1].split()
        velocity_strings = split_line[2].split()
        color_string = split_line[3].strip()
        marker_string = split_line[4].strip()

        mass = float(mass_string) * _mass_scale_factor
        mass_list.append(mass)
        colors.append(color_string)
        markers.append(marker_string)

        pos_x = float(position_strings[0]) * _distance_scale_factor
        pos_y = float(position_strings[1]) * _distance_scale_factor
        pos_z = float(position_strings[2]) * _distance_scale_factor
                                                                   
        vel_x = float(velocity_strings[0]) * _velocity_scale_factor
        vel_y = float(velocity_strings[1]) * _velocity_scale_factor
        vel_z = float(velocity_strings[2]) * _velocity_scale_factor

        init_pos.append([pos_x,pos_y,pos_z])
        init_vel.append([vel_x,vel_y,vel_z])

    initial_conditions = {'mass':mass_list,
                          'position':init_pos,
                          'velocity':init_vel}

    return initial_conditions, colors, markers
