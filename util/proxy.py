import os


def set_proxy():
    print(os.environ)
    PROXY = os.environ['VPN_PROXY']
    os.environ["http_proxy"] = PROXY
    os.environ["https_proxy"] = PROXY


if __name__ == '__main__':
    set_proxy()