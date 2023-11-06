# ПРИМЕЧАНИЕ
# Здесь везде C -- это константа C3 из аналитического решения,
#             p -- это параметр p1.




from math import sin, cos, pi, sqrt

import numpy as np
import matplotlib.pyplot as plt


# Решает систему уравнений и находит значения C и p.
def solve(Bx: float, By: float) -> tuple[float, float]:
    # Начальные приближения.
    # Прим.: должны быть "достаточно" близко к решению, иначе метод может не сойтись.
    #        Для p_0 можно построить график параметрической функции (x(p), y(p)) и посмотреть,
    #        при каком p точка лежит "достаточно" близко к точке B. В данном случае это около p = pi.
    C_0 = 1.
    p_0 = pi
    Z = np.asarray([C_0, p_0]).T

    eps = 0.0001
    max_iter = 10000

    for _ in range(max_iter):
        C, p = Z

        f1 = C * (p - sin(p)) - Bx
        f2 = C * (1. - cos(p)) - By
        df1dc = p - sin(p)
        df1dp = C * (1. - cos(p))
        df2dc = 1. - cos(p)
        df2dp = C * sin(p)

        W = np.asarray([
            [df1dc, df1dp],
            [df2dc, df2dp]
        ])

        F = np.asarray([f1, f2]).T

        Z_new = Z - np.linalg.inv(W) @ F
        diff = np.linalg.norm(Z_new - Z)
        Z = Z_new

        if diff < eps:
            break
    else:
        raise Exception("Метод Ньютона разошёлся. "
                        "Попробуйте другие начальные приближения `C_0` и `p_0`.")

    C, pB = Z

    return C, pB


def main():
    g = 9.8
    Ax = 0.
    Ay = 0.
    Bx = 6.
    By = 2.

    ###########################################################################

    pA = 0.
    C, pB = solve(Bx, By)
    T = sqrt(C / g) * pB

    print(f"C = {C}, pB = {pB}, T = {T}")

    p = np.linspace(pA, pB, 100, endpoint=True)
    x = [C * (p_ - sin(p_)) for p_ in p]
    y = [C * (1. - cos(p_)) for p_ in p]

    plt.plot(x, y)
    plt.plot(Ax, Ay, 'ro')
    plt.plot(Bx, By, 'ro')

    plt.gca().invert_yaxis()
    plt.grid()
    plt.title(f'Брахистохрона - циклоида. Время движения: {round(T, 2)} с.')
    plt.show()


if __name__ == '__main__':
    main()
