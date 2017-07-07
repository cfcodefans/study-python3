import unittest
import numpy

radius_of_earth: int = 6.371e6


class PythonPlayground(unittest.TestCase):
    def before_test(self):
        print("\nstart")

    def test_arithmetic(self):
        answer: int = 42
        # Basic arithmetic
        a = 3 * answer + 4
        b = radius_of_earth ** 2 + (a + 3) ** 0.5
        answer += 7
        c: float = 5 / 4
        d: float = 5 / 4.
        e: float = 1.0 * 5 / 4
        print(a, b, answer, c, d, e)

    def test_triangle_func(self):
        import math
        f: float = math.sqrt(4)
        g: float = radius_of_earth * math.sin(math.pi / 180.0 * 23.4)
        print(f, g)

    def test_control(self):
        print("\n")
        for h in range(7):
            i: int = h ** 2
            print(i)

        k: int = 42
        m: int = 43
        while k < 130 or m == 140:
            k += 1
            m += k

        print(k, m)

        if k > 42:
            print("Hi")
        elif m > 43:
            print("Hello")
        else:
            print("Bye")

    def test_numpy(self):

        n: numpy.core.ndarray = numpy.zeros(5)
        n[0] = 20.
        n[4] = 99.
        print(n)
        print(n[-1])

        p: numpy.core.ndarray = numpy.zeros([2, 3])
        p[0, 1] = 7
        p[1, 2] = 8
        print(p)
        p = 1. + 2. * p
        print(p)
        print(p[0])
        q: numpy.core.ndarray = p
        q[0, 0] = 42
        print(p)

    def test_numpy_ndarry(self):
        print()
        va: numpy.ndarray = numpy.array([1, 2])
        print(type(va))
        vb: numpy.ndarray = numpy.array([2, 1])
        print(va - vb)

    def test_func(self):
        def three_times(u):
            r = 2 * u
            return r + u

        print(three_times(1), three_times(7))

    def test_sin_cos(self):
        import math
        import numpy
        import matplotlib.pyplot

        def sin_cos() -> (numpy.core.ndarray, numpy.core.ndarray, numpy.core.ndarray):
            num_points: float = 50
            x: numpy.core.ndarray = numpy.zeros(num_points)
            sin_x: numpy.core.ndarray = numpy.zeros(num_points)
            cos_x: numpy.core.ndarray = numpy.zeros(num_points)
            for i in range(num_points):
                x[i] = i * (math.pi * 2 / num_points)
                sin_x[i] = math.sin(x[i])
                cos_x[i] = math.cos(x[i])
            return x, sin_x, cos_x

        x, sin_x, cos_x = sin_cos()
        matplotlib.pyplot.plot(x, sin_x)
        matplotlib.pyplot.plot(x, cos_x)
        matplotlib.pyplot.show()

    def test_euler_free_fall(self):
        import math
        import numpy
        import matplotlib.pyplot

        def forword_euler() -> (numpy.core.ndarray, numpy.core.ndarray, numpy.core.ndarray):
            h: float = 0.1  # s
            g: float = 9.81  # m /s2

            num_steps: int = 50

            steps_ = num_steps + 1
            t: numpy.core.ndarray = numpy.zeros(steps_)
            x: numpy.core.ndarray = numpy.zeros(steps_)
            v: numpy.core.ndarray = numpy.zeros(steps_)

            for step in range(num_steps):
                t[step + 1] = h * (step + 1)
                x[step + 1] = x[step] + h * v[step]
                v[step + 1] = v[step] - g * h
            return t, x, v

        t, x, v = forword_euler()

        def plot_me():
            axes_height = matplotlib.pyplot.subplot(211)
            matplotlib.pyplot.plot(t, x)
            axes_velocity = matplotlib.pyplot.subplot(212)
            matplotlib.pyplot.plot(t, v)
            axes_height.set_ylabel("Height in m")
            axes_velocity.set_ylabel("Velocity in m/s")
            axes_velocity.set_xlabel("Time in s")
            matplotlib.pyplot.show()

        plot_me()

    def test_acceleration(self):
        import numpy
        earth_mass: float = 5.97e24
        moon_mass: float = 7.35e22
        gravitational_constant = 6.67e-11

        def acceleration(moon_position: numpy.ndarray, spaceship_position: numpy.ndarray) -> numpy.ndarray:
            pass

        pass

    def test_linalg_norm(self):
        import numpy as np
        from numpy import linalg as LA
        # a: np.ndarray = np.arange(9) - 4
        # print(a)
        # b = a.reshape((3, 3))
        # print(b)
        #
        # print(LA.norm(a))
        print(LA.norm([2, 2]))
        print(LA.norm([2, 2, 2]))
        print(LA.norm(np.array([1, 2]) - np.array([2, 1])))

    def test_static_orbit(self):
        import numpy
        import math

        earth_mass = 5.97e24  # kg
        gravitational_constant = 6.67e-11  # N m2 / kg2

        print()
        re = gravitational_constant * earth_mass * (60 * 60 * 24) ** 2 / (4 * (math.pi ** 2))
        print(math.pow(re, 1 / 3))


import numpy
import math

earth_mass = 5.97e24  # kg
moon_mass = 7.35e22  # kg
gravitational_constant = 6.67e-11  # N m2 / kg2

re = gravitational_constant * earth_mass * 86400 ** 2 / 4 * (math.pi ** 2)
print(re ** -3)
pass


# The origin, or (0,0), is at the center of the earth
# in this example, so it doesn't make any sense to
# set either the moon_position or spaceship_position
# equal to (0,0). Depending on your solution, doing this
# may throw an error!  Please note that moon_position and
# spaceship_position are both numpy arrays, and the
# returned value should also be a numpy array.

def acceleration(moon_position, spaceship_position):
    # nonsense = numpy.linalg.norm(moon_position) * spaceship_position
    v_moon_spaceship = moon_position - spaceship_position
    v_earth_spaceship = - spaceship_position
    G = gravitational_constant
    nonsense = G * (
        moon_mass / numpy.linalg.norm(v_moon_spaceship) ** 3 * v_moon_spaceship + earth_mass / numpy.linalg.norm(
            v_earth_spaceship) ** 3 * v_earth_spaceship)
    return nonsense


if __name__ == '__main__':
    unittest.main
