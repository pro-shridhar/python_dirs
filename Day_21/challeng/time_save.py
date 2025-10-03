def time_saved(s_lim, s_avg, d):

    t1 = (d / s_lim) * 60
    t2 = (d / s_avg) * 60

    return round(t1 - t2, 1)
