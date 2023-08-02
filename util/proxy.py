import os
PROXY = os.environ['VPN_PROXY']
os.environ["http_proxy"] = PROXY
os.environ["https_proxy"] = PROXY


def set_proxy():
    PROXY = os.environ['VPN_PROXY']
    os.environ["http_proxy"] = PROXY
    os.environ["https_proxy"] = PROXY

def test_cuda():
    import torch
    print(torch.cuda.is_available())


# write a decorator , to print the running time of wrapped function and print running time.
def timeit(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"running time of {func.__name__} is {time.time() - start}")
        return result
    return wrapper

if __name__ == '__main__':
    test_cuda()