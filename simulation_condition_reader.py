def read():
    mass_list = [1000,1]

    init_pos = [
        [0,0,0],
        [10,0,0]]

    init_vel = [
        [0,0,0],
        [0,10,0]]

    initial_conditions = {'mass':mass_list,
                          'position':init_pos,
                          'velocity':init_vel}

    return initial_conditions
