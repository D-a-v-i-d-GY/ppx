import numpy as np

# equation of the plane is ax + by + cz = d, coordinates of the point are x, y, z

def project_on_plane(a, b, c, d, x, y, z):
    # t and t0 are some parameters
    t0 = d / (a ** 2 + b ** 2 + c ** 2)
    t = (d - a * x - b * y - c * z) / (a ** 2 + b ** 2 + c ** 2)

    # r is vector from the origin to the projection of the point, r0 is perpendicular vector from the origin to the plane
    r0 = np.array([a * t0, b * t0, c * t0])
    r = np.array([a * t + x, b * t + y, c * t + z])

    # i and j are basis vector of the plane, I have chosen them so that j intersects z axis and i x j is in the same direction as r0
    j = np.array([- a * t0, - b * t0, d / c - c * t0])
    j = j / np.linalg.norm(j)
    i = np.cross(j, r0)
    i = i / np.linalg.norm(i)

    # returns coordinates of the point's projection on plane in plane's coordinate system
    return np.dot(r - r0, i), np.dot(r - r0, j)
