def petrol(distance, tank_range, stations):
    distances = [stations[0]]
    for i in range(1, len(stations)):
        distances.append(stations[i] - stations[i - 1])
    distances.append(distance - stations[-1])
    print(distances)

    tmp = 0
    n = 0
    while len(distances) > 0:
        if tmp + distances[0] <= tank_range:
            tmp += distances[0]
            distances.pop(0)
        else:
            tmp = 0
            n += 1

    return n

distance = None
tank_range = None
stations = None
with open("petrol2.in", 'r') as f:
    l1 = f.readline()
    _, distance, tank_range = [int(i) for i in l1.split()]
    l2 = f.readline()
    stations = [int(i) for i in l2.split()]

# distance = 10
# tank_range = 4
# stations = [3,4,6]

n = petrol(distance=distance, tank_range=tank_range, stations=stations)
print("Number of stations = %d" % n)
