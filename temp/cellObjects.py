from math import cos, hypot, pi, sin

def b10(num):
    """Decimal to Scientific Notation."""
    return "{:.10e}".format(num)


def dist(p1, p2):
    """Distance between two points."""
    return hypot(p2[0] - p1[0], p2[1] - p1[1])

class Circle:
    """Generates coordinates of circle."""
    def __init__(self, x, y, r, n, SPRING_CONSTANT, REST_LENGTH, RIGIDITY, angle=0):
        self.x = x
        self.y = y
        self.r = r
        self.n = n
        self.angle = angle
        self.SPRING_CONSTANT = SPRING_CONSTANT
        self.REST_LENGTH = REST_LENGTH
        self.RIGIDITY = RIGIDITY

        self.coords = [
            (
                cos(2 * pi / self.n * i + angle) * r + x,
                sin(2 * pi / self.n * i + angle) * r + y,
            )
            for i in range(0, self.n)
        ]
        self.vert_count = len(self.coords)
        self.spring_count = len(self.coords)
        self.beam_count = len(self.coords)

    def gen_spring(self, offset=0):
        return [
            f"{(x)%self.vert_count + offset} "
            f"{(x+1)%self.vert_count + offset} "
            f"{b10(self.SPRING_CONSTANT)} {b10(self.REST_LENGTH)}\n"
            for x in range(self.spring_count)
        ]

    def gen_beam(self, offset=0):
        return [
            f"{(x)%self.vert_count+offset} {(x+1)%self.vert_count+offset} "
            f"{(x+2)%self.vert_count+offset} "
            f"{b10(self.RIGIDITY)}\n"
            for x in range(self.vert_count)
        ]


class Wall:
    """Generates coordinates of a wall"""
    def __init__(self, x1, y1, x2, y2, n, SPRING_CONSTANT, RIGIDITY):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.n = n
        self.SPRING_CONSTANT = SPRING_CONSTANT
        self.RIGIDITY = RIGIDITY

        self.coords = [
            (x1 + i * (x2 - x1) / n, y1 + i * (y2 - y1) / n)
            for i in range(0, n + 1)
        ]

        self.vert_count = len(self.coords)
        self.spring_count = len(self.coords) - 1
        self.beam_count = len(self.coords) - 2

    def gen_spring(self, offset=0):
        return [
            f"{x+offset} {x+offset+1} {b10(self.SPRING_CONSTANT)} "
            f"{b10(dist(self.coords[x], self.coords[x+1]))}\n"
            for x in range(self.spring_count)
        ]

    def gen_beam(self, offset=0):
        return [
            f"{x+offset} {x+1+offset} {x+2+offset} " f"{b10(self.RIGIDITY)}\n"
            for x in range(self.beam_count)
        ]

class Sphere:
    """Generates coordinates of Sphere."""
    def __init__(self, x, y, z, r, n, SPRING_CONSTANT, REST_LENGTH, RIGIDITY, angle=0):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.n = n
        self.angle = angle
        self.SPRING_CONSTANT = SPRING_CONSTANT
        self.REST_LENGTH = REST_LENGTH
        self.RIGIDITY = RIGIDITY

        self.coords = [ # Modify?
            (
                cos(2 * pi / self.n * i + angle) * r + x,
                sin(2 * pi / self.n * i + angle) * r + y,
            )
            for i in range(0, self.n)
        ]
        self.vert_count = len(self.coords)
        self.spring_count = len(self.coords)
        self.beam_count = len(self.coords)


