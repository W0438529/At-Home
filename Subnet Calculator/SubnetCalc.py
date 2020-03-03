import sys
import math


def main():
    sys.argv = ['SubnetCalc.py', '-a192.168.0.0', '-h30'] # -- Run without Command Prompt
    x = sys.argv[1]
    x = x.split('-a')
    y = sys.argv[2]
    y = y.split('-h')
    add = x[1]
    num_host = y[1]
    display(add, num_host)


# NETWORK INFORMATION
# display net add and # of hosts -- make into sys.argv
def net_info(add):
    return add


def net_info_host(num_host):
    return num_host


# checking network class
def net_class(add):
    z = "A"
    x = "B"
    y = "C"
    for r in range(1, 127):
        add_list = add.split('.')
        if int(add_list[0]) == r:
            i = f'Network Class: {z}\n# of IP Addr: 16777216'
            return i
    for r in range(128, 191):
        add_list = add.split('.')
        if int(add_list[0]) == r:
            j = f'Network Class: {x}\n# of IP Addr: 65536'
            return j
    for r in range(192, 223):
        add_list = add.split('.')
        if int(add_list[0]) == r:
            k = f'Network Class: {y}\n# of IP Addr: 256'
            return k


# calculate subnet size from desired hosts
def subnet_size(num_host):
    subnetsize = 2
    while int(num_host) > subnetsize:
        subnetsize *= 2
    return subnetsize


# ADDRESS INFORMATION

# decimal octets
def dec_octets(add):
    return add


# convert to binary octets
def bin_octets(add):
    add_list = add.split('.')
    a = '{:08b}'.format(int(add_list[0]))
    b = '{:08b}'.format(int(add_list[1]))
    c = '{:08b}'.format(int(add_list[2]))
    d = '{:08b}'.format(int(add_list[3]))
    return f'{a}.{b}.{c}.{d}'


# convert to hex octets
def hex_octets(add):
    add_list = add.split('.')
    a = '{:02X}'.format(int(add_list[0]))
    b = '{:02X}'.format(int(add_list[1]))
    c = '{:02X}'.format(int(add_list[2]))
    d = '{:02X}'.format(int(add_list[3]))
    return f'{a}.{b}.{c}.{d}'


# convert to 32bit binary
def bin32_dec_number(add):
    add_list = add.split('.')
    a = '{:08b}'.format(int(add_list[0]))
    b = '{:08b}'.format(int(add_list[1]))
    c = '{:08b}'.format(int(add_list[2]))
    d = '{:08b}'.format(int(add_list[3]))
    x = (a, b, c, d)
    z = ''.join(x)
    return z


# calculate the CIDR number
def calc_cidr(num_host):
    sub = math.log2(int(num_host))
    cidr = (32 - round(sub))
    return cidr


# calculate the Subnet mask and Binary Mask
def subnet(num_host):
    cidr = calc_cidr(num_host)
    sub_bin_list = []
    while len(sub_bin_list) < cidr:
        sub_bin_list.append("1")
    while len(sub_bin_list) < 32:
        sub_bin_list.append("0")
    k = ''.join(sub_bin_list[0:8])
    l = ''.join(sub_bin_list[8:16])
    m = ''.join(sub_bin_list[16:24])
    n = ''.join(sub_bin_list[24:])
    i = f'Subnet Mask: {int(k, 2)}.{int(l, 2)}.{int(m, 2)}.{int(n, 2)} or /{cidr}\nBinary Mask: {k}.{l}.{m}.{n}'
    return i


# calculate the number of subnets
def num_subnets(num_host):
    sub_size = subnet_size(num_host)
    x = 0
    if sub_size <= 256:
        x = 256 // sub_size
    elif 256 < sub_size <= 65536:
        x = 65536 // sub_size
    elif 65536 < sub_size <= 1677216:
        x = 1677216 // sub_size
    return x


def display(add, num_host):
    a = net_info(add)
    x = net_info_host(num_host)
    b = subnet_size(num_host)
    c = dec_octets(add)
    y = bin32_dec_number(add)
    d = bin_octets(add)
    e = hex_octets(add)
    g = net_class(add)
    i = subnet(num_host)
    j = num_subnets(num_host)
    print('Network Information\n-------------------')
    print(f'Network Address: {a}')
    print(f'# of Hosts Per Subnet: {x}')
    print(f'Calculated Subnet Size: {b}')
    print('Address Information\n-------------------')
    print(f'Decimal Octets: {c}')
    print(f'Decimal Addres: {int(y, 2)}')
    print(f'Binary Octets: {d}')
    print(f'Hex Octets: {e}')
    print('NetMask Information\n-------------------')
    print(g)
    print(i)
    print(f'# of Subnets: {j}')




if __name__ == '__main__':
    main()



