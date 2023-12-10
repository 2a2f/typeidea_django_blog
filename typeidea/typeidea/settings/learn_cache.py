import functools
import time


CACHE = {}


def cache_it(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = repr(*args, **kwargs)
        try:
            result = CACHE[key]
        except KeyError:
            result = func(*args, **kwargs)
            CACHE[key] = result
        return result
    return inner


@cache_it
def query(sql):
    time.sleep(1)
    result = 'execute %s' % sql
    return result


if __name__ == '__main__':
    start = time.time()
    query('SELECT * FROM blog_post')
    print(time.time() - start)

    start = time.time()
    query('SELECT * FROM blog_post')
    print(time.time() - start)
