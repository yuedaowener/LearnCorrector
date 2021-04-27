# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/4/27 20:22
"""


def get_small_data(n_sample=1000):
    fp_r = r"data/processed_data/all_same_765376/all_data_765376.txt"
    fp_w = f"data/processed_data/all_same_765376/all_data_765376_{n_sample}.txt"
    n = 0
    with open(fp_r, 'r', encoding='utf-8') as fr, open(fp_w, 'w', encoding='utf-8') as fw:
        for i, line in enumerate(fr):
            fw.write(line.strip() + '\n')
            n += 1
            if n >= n_sample:
                break


def main():
    get_small_data(1000)

    pass


if __name__ == "__main__":
    main()
