def ave_spd(up_time, up_spd, down_spd):

    ti = (up_time * up_spd) / down_spd

    return (2 * (up_time * up_spd)) / (ti + up_time)
