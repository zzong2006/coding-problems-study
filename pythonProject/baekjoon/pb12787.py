import sys


def solution():
    get_input = sys.stdin.readline
    t = int(get_input().strip())
    for i in range(t):
        w, p = get_input().strip().split()
        # print(p)
        if w == '1':
            divided = p.split('.')
            sum_up = ""
            for i in divided:
                bin_temp = format(int(i), 'b')
                if len(bin_temp) < 8:
                    bin_temp = '0' * (8 - len(bin_temp)) + bin_temp
                sum_up += bin_temp

            print(int(sum_up, 2))

        else:
            # decimal -> ip
            a = format(int(p), 'b')
            if len(a) < 8 * 8:
                a = '0' * (64 - len(a)) + a
            ip = ""
            for i in range(8):
                k = a[8 * i: 8 + (8 * i)]
                ip += str(int(k, 2))
                if i != 7:
                    ip += '.'
            print(ip)


solution()
