import matplotlib.pyplot as plt
import numpy as np

def first_func(x):
    return (8 * np.cos(x) - x - 6).item()

def second_func(x):
    return x**3 + x**2 + 9

def plot(x_list, func_list, n):
    plt.plot(x_list, func_list)
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"График функции №{n}")
    plt.savefig(f"{n}.png")
    
def plot_all(x_left, x_right, x_count):
    x_list = np.linspace(x_left, x_right, x_count)
    func1_list = [first_func(x) for x in x_list]
    func2_list = [second_func(x) for x in x_list]
    plot(x_list, func1_list, 1)
    plot(x_list, func2_list, 2)
    plt.close()

def get_interval(func, x_left, x_right, step):
    y_list = []
    x = x_left
    y_list.append(func(x))
    x += step
    y_list.append(func(x))
    while y_list[-2] * y_list[-1] >= 0: # пока не найдены пересечения оси X
        x += step
        y_list.append(func(x))
    print(f"Значения в X, начиная от {x_left}:", y_list)
    return [x - 1, x]

def first_fi(x):
    return np.arccos((x + 6) / 8).item()

def second_fi(x):
    return -(x**2 + 9)**(1 / 3)

def get_root(interval_points, fi_func, eps, n):
    root_list = []
    for id_inter in range(len(interval_points) - 1):
        x_prev = interval_points[id_inter]
        for i in range(1500):
            x_temp = fi_func(x_prev)
            if abs(x_temp - x_prev) <= eps:
                root_list.append(x_temp)
                break
            x_prev = x_temp
    print(f"Корни уравнения №{n}, при ε={eps}:", root_list)
    return root_list
    
func1_eps = 0.0001
func2_eps = 0.01

plot_all(-10, 10, 40)

interval_points_1 = get_interval(first_func, 0, 5, 0.5)
interval_points_2 = get_interval(second_func, -10, 10, 0.5)

root_list_1 = get_root(interval_points_1, first_fi, func1_eps, 1)
root_list_2 = get_root(interval_points_2, second_fi, func2_eps, 2)

