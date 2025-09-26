def check_time(func):  # 🟡
    import time
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print('[*] Время выполнения: {:.4f} секунд.'.format(end - start))
        return result

    return wrapper


def add_separators(func):  # 🟡
    def inner():
        result = func()
        print('-' * 35)
        return result

    return inner


def save_call_to_file(func):  # 🟡
    import time
    def inner(*args, **kwargs):
        i_date = time.strftime('%Y-%m-%d_%H:%M:%S')
        func_name = func.__name__  # пишем название функции в файл
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(f'{i_date}: {func_name}\n')

        result = func(*args, **kwargs)
        return result

    return inner
