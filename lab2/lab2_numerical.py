from math import log


# Правая часть ДУ
#     dT/dt = f(t, T),
# где T = T(t).
def f(_t: float, T: float) -> float:
    return -k * (T - Te)


# Делает 1 шаг RK4.
# Основываясь на текущих значениях t и T(t), вычисляет T(t + dt).
def rk4_step(t: float, h: float) -> float:
    k1 = f(t, h)
    k2 = f(t + dt / 2, h + dt / 2 * k1)
    k3 = f(t + dt / 2, h + dt / 2 * k2)
    k4 = f(t + dt, h + dt * k3)
    return h + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


# Решение задачи и вывод ответа.
def solve():
    t = t0
    T = T0

    while T > T2:
        T = rk4_step(t, T)
        t += dt

    print(f'T({t}) = {T}')
    print(f'ОТВЕТ: тело остынет до заданной температуры через {round(t / 60, 1)} мин.')


#########################################################################################


Te = 20
t0 = 0
T0 = 100
t1 = 600
T1 = 60
T2 = 25

dt = 0.001

k = 1 / (t1 - t0) * log((T0 - Te) / (T1 - Te))  # см. аналит. решение, формула (*)

solve()
