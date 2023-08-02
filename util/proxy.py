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

if __name__ == '__main__':
    test_cuda()