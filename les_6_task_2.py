import random
import sys
print(sys.version, sys.platform)
# 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] win32
# size = 368(all)


def pro(ls):
    mai = ls.index(max(ls))
    mii = ls.index(min(ls))
    ls[mai], ls[mii] = ls[mii], ls[mai]

    print("*" * 50)
    x = locals().values()
    y = 0
    for i in x:
        print(f"type = {i.__class__}, size = {sys.getsizeof(i)}, object = {i}")
        y += sys.getsizeof(i)
    print(y)


lss = [random.randint(0, 100) for i in range(30)]
pro(lss)
