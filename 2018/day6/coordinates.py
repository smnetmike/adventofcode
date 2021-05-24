def getNearestCenter(pt, centers):
    distances = [abs(pt[0] - x[0]) + abs(pt[1] - x[1]) for x in centers]
    minDist = min(distances)
    if distances.count(minDist) > 1:
        return None
    ind = distances.index(minDist)
    return centers[ind]

def largest_non_infinite_array(centers):

    xs = [x[0] for x in centers]
    ys = [x[1] for x in centers]
    minx = min(xs)
    maxx = max(xs)
    miny = min(ys)
    maxy = max(ys)
    centersDict = {}
    infCenters = []
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            nearestCenter = getNearestCenter((x, y), centers)
            if nearestCenter is None:
                continue
            if x == minx or x == maxx or y == miny or y == maxy:
                infCenters.append(nearestCenter)
            if nearestCenter not in centersDict:
                centersDict[nearestCenter] = []
            centersDict[nearestCenter].append((x, y))
    #for pt in centersDict:
    #    print("{} : {} \n".format(pt, len(centersDict[pt])))

    # Removing infinite areas center
    for cent in infCenters:
        centersDict.pop(cent, None)
    centersDictLen = {pt : len(centersDict[pt]) for pt in centersDict}
    maxPt = max(centersDictLen, key=centersDictLen.get)
    print(maxPt, centersDictLen[maxPt])

def getDistanceFromCenters(pt, centers):
    distances = [abs(pt[0] - x[0]) + abs(pt[1] - x[1]) for x in centers]
    return sum(distances)

def regionSize(centers, limit):
    xs = [x[0] for x in centers]
    ys = [x[1] for x in centers]
    minx = min(xs)
    maxx = max(xs)
    miny = min(ys)
    maxy = max(ys)

    region = []
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            totalDist = getDistanceFromCenters((x,y), centers)
            if totalDist < limit:
                region.append((x,y))

    return len(region)

def main():

    f = open("input.txt", "r")
    lines = f.readlines()
    coordinates = []
    for line in lines:
        arr = line.split(",")
        coord = (int(arr[0]), int(arr[1]))
        coordinates.append(coord)

    # largest_non_infinite_array(coordinates)

    size = regionSize(coordinates, 10000)
    print("Region size: {}".format(size))

if __name__ == '__main__':
    main()