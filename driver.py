from point import Point,EllipticCurve











def main():

    ec = EllipticCurve(1,6,11)
    for point in ec.points :
        print(str(point.x) + " " + str(point.y))


main()