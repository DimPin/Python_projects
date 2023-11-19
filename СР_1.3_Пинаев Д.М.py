import multiprocessing
import time
import random

def sum_list():
    list1=[] #объявляем список
    list2=[] #объявляем список 2
    for i in range(1,10):
        list1.append(random.randint(0, 100))
        list2.append(random.randint(0, 100))
    summ=sum(list1)+sum(list2)
    print(f'Сумма списков равна:{summ}')

def heavy(n, i, proc):
    factor = 1
    for x in range(2, n+1):
        factor = factor * x
    print(f"Вычисление № {i} процессор {proc}")

def sequential(calc, proc):
    print(f"Запускаем поток № {proc}")
    for i in range(calc):
        heavy(10, i, proc)
    sum_list()
    print(f"{calc} циклов вычислений закончены. Процессор № {proc}")

def pooled(core=None):
    # вычисляем количество ядер процессора
    n_proc = core
    # вычисляем количество операций на процесс
    calc = 4
    # создаем список инициализации функции
    # sequential(calc, proc) для каждого процесса
    init = map(lambda x: (calc, x), range(n_proc))
    with multiprocessing.Pool() as pool:
        pool.starmap(sequential, init)

    print(calc, n_proc, core)
    return (calc, n_proc, core)

if __name__ == "__main__":
    start = time.time()
    # в целях эксперемента, укажем количество
    # ядер больше чем есть на самом деле
    calc, n_proc, n = pooled(10)
    end = time.time()
    text = '' if n is None else 'задано '
    print(f"Всего {text}{n_proc} ядер процессора")
    print(f"На каждом ядре произведено {calc} циклов вычислений")
    print(f"Итого {n_proc * calc} циклов за: ", end - start)