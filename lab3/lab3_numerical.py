# Правая часть ДУ
#     dP/dt = f(t, P),
# где P = P(t).
def f(t: float, P: float) -> float:
    return b(t) * P


# Делает 1 шаг RK4.
# Основываясь на текущих значениях t и P(t), вычисляет P(t + dt).
def rk4_step(t: float, P: float) -> float:
    k1 = f(t, P)
    k2 = f(t + dt / 2, P + dt / 2 * k1)
    k3 = f(t + dt / 2, P + dt / 2 * k2)
    k4 = f(t + dt, P + dt * k3)
    return P + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


# Решение задачи и вывод ответа.
def solve():
    t = t0
    P = P0

    while t < t1:
        P = rk4_step(t, P)
        t += dt

    print(f'P({t}) = {P}')
    print(f'ОТВЕТ: через указанное время с начала роста популяция бактерий будет составлять {round(P)} особей')


#########################################################################################


t0 = 0
P0 = 500
def b(t: float) -> float: return 1 / (1 + 2 * t)
t1 = 6

dt = 0.001

solve()
