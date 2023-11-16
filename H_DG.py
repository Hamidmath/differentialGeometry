class H_DG:
    # For triple of consequent points of curve p1, p2, p3, we work on finding perpendicular bisectors of lines p2p1 and p3p2 
    def perpendicular_bisectors(H, p1, p2, p3):
        v1 = [p2[i] - p1[i] for i in range(3)]
        v2 = [p3[i] - p3[i] for i in range(3)]
        n = [
          v1[1]*v2[2] - v1[2]*v2[1], 
          v1[2]*v2[0] - v1[0]*v2[2], 
          v1[0]*v2[1] - v1[1]*v2[0]
        ]
        midPoint =  [(f+g)/2 for (f,g) in zip(p1,p2)]
        b = [
          v1[1]*n[2] - v1[2]*n[1], 
          v1[2]*n[0] - v1[0]*n[2], 
          v1[0]*n[1] - v1[1]*n[0]
        ]
        b_mag = sum([b[i]**2 for i in range(3)])**0.5    
        d = [b[i]/b_mag for i in range(3)]
        res1 = {
            "x": (midPoint[0] ,d[0]),
            "y":(midPoint[1],d[1]),
            "z":(midPoint[2],d[2])
            }
        midPoint =  [(f+g)/2 for (f,g) in zip(p2,p3)]
        b = [
          v2[1]*n[2] - v2[2]*n[1], 
          v2[2]*n[0] - v2[0]*n[2], 
          v2[0]*n[1] - v2[1]*n[0]
        ]
        b_mag = sum([b[i]**2 for i in range(3)])**0.5    
        d = [b[i]/b_mag for i in range(3)]
        res2 = {
            "x": (midPoint[0] ,d[0]),
            "y":(midPoint[1],d[1]),
            "z":(midPoint[2],d[2])
            }
        return [res1, res2]

    # check that two vectors are parallel or not
    def are_parallel(H, v1, v2):
        dot_product = sum([a * b for a, b in zip(v1, v2)])
        mag1 = sum([a**2 for a in v1]) ** 0.5
        mag2 = sum([a**2 for a in v2]) ** 0.5
        return dot_product == mag1 * mag2
    
    # find intersection of two lines acoording to their features
    def intersection(H, lines):
        a1, b1 = lines[0]["x"]
        c1, d1 = lines[0]["y"]
        e1, f1 = lines[0]["z"]
        a2, b2 = lines[1]["x"]
        c2, d2 = lines[1]["y"]
        e2, f2 = lines[1]["z"]
        if H.are_parallel([b1,d1,f1], [b2,d2,f2]):
            return "NoIntersection"
        D = b1 * d2 - b2 * d1
        D1 = (a2 - a1) * d2 - (c2 - c1) * b2
        D2 = b1 * (c2 - c1) - d1 * (a2 - a1)
        t1 = D1 / D
        t2 = D2 / D
        x = a1 + b1 * t1
        y = c1 + d1 * t1
        z = e1 + f1 * t1
        return [x, y, z]
    #calculate the radius of a circle that pases through p1, p2, p3 and the curvature about p2
    def curvature(H, p1, p2, p3):
        lines = H.perpendicular_bisectors(p1, p2, p3)
        center = H.intersection(lines)
        if center == "NoIntersection":
            return math.inf
        radius = sum([(p2[i]-center[i])**2 for i in range(3))**0.5
        return 1/radius


H = H_DG()
p1 = [1, 0, 0]
p2 = [0, 0, 0]
p3 = [0, 0, 1]

print("Curvature about p2 :", H.curvature(p1, p2, p3))

#-------------
#----output
'''Curvature about p2 : 0.70710678118'''
