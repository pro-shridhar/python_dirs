def area_of_country(name, area):

    world = 148940000
    percent = (area * 100) / world

    return f"{name} is {percent:.2f}% of the total world's landmass"


print(area_of_country("Switzerland", 41284))
