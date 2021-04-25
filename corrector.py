# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/4/22 15:22
"""

import pycorrector

# TODO: 有哪些纠错方法？从简单到复杂分别有哪些？

def main():
    text = [
        '这件事情针让人想象难以',
        '这周末我要去配副眼睛',
        '感帽了',
        '你儿字今年几岁了',
        '少先队员因该为老人让坐',
    ]

    pass
    corrected_sent, detail = pycorrector.correct('少先队员因该为老人让坐')
    print(corrected_sent, detail)
    pass


if __name__ == "__main__":
    main()
