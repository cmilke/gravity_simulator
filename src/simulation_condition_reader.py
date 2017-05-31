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

        mass_list.append(float(mass_string))
        colors.append(color_string)
        markers.append(marker_string)

        pos_x = float(position_strings[0])
        pos_y = float(position_strings[1])
        pos_z = float(position_strings[2])

        vel_x = float(velocity_strings[0])
        vel_y = float(velocity_strings[1])
        vel_z = float(velocity_strings[2])

        init_pos.append([pos_x,pos_y,pos_z])
        init_vel.append([vel_x,vel_y,vel_z])

    initial_conditions = {'mass':mass_list,
                          'position':init_pos,
                          'velocity':init_vel}

    return initial_conditions, colors, markers
