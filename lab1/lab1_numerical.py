from math import sqrt


# Правая часть ДУ
#     dh/dt = f(t, h),
# где h = h(t).
def f(_t: float, h: float) -> float:
    return -q * p * sqrt(2 * g * h) / (A * B) + R / (A * B)


# Делает 1 шаг RK4.
# Основываясь на текущих значениях t и h(t), вычисляет h(t + dt).
def rk4_step(t: float, h: float) -> float:
    k1 = f(t, h)
    k2 = f(t + dt / 2, h + dt / 2 * k1)
    k3 = f(t + dt / 2, h + dt / 2 * k2)
    k4 = f(t + dt, h + dt * k3)
    return h + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


# Решение задачи и вывод ответа.
def solve():
    t = t0
    h = h0

    while h < M:
        h = rk4_step(t, h)
        t += dt

    print(f'h({t}) = {h}')
    print(f'ОТВЕТ: бак заполнится через {round(t, 1)} сек.')


#########################################################################################


q = 0.00025
A = 0.6
B = 0.75
M = 0.8
p = 0.6
R = 0.0018
g = 9.8
t0 = 0
h0 = 0

dt = 0.001

solve()
