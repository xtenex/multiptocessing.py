#!/usr/bin/env python3

import multiprocessing

def cont():
    for i in range(1,51):
        print('%d' %(i))

def main():
    proc = []
    cor = multiprocessing.cpu_count()
    if cor > 0:
        for i in range(cor + 1):
            p = multiprocessing.Process(target=cont)
            p.start()
            proc.append(p)

        for pro in proc:
            pro.join()

    else:
        print("Numero de cores = %d" %cor)
        

if __name__ == '__main__':
    main()
