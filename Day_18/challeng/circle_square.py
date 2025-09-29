def square_areas_difference(r):

    inscrib_area = (r * 2) ** 2
    circum_area = ((r * 2) ** 2) * 0.5
    return inscrib_area - circum_area
