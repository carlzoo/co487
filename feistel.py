#!/usr/bin/python

#TODO: fix operations with hex

#permutation constants
S0={0x0:0x1,
    0x1:0x9,
    0x2,0x2,
    0x3:0x9,
    0x4:0xa,
    0x5:0x7,
    0x6:0xf,
    0x7:0xe,
    0x8:0x6,
    0x9:0xb,
    0xa:0xc,
    0xb:0x8,
    0xc:0x4,
    0xd:0x3,
    0xe:0x2,
    0xf:0x0}

S1={0x0:0x6,
    0x1:0xb,
    0x2,0xb,
    0x3:0xa,
    0x4:0xa,
    0x5:0xc,
    0x6:0xc,
    0x7:0xd,
    0x8:0xd,
    0x9:0x1,
    0xa:0x1,
    0xb:0x2,
    0xc:0x2,
    0xd:0x4,
    0xe:0x5,
    0xf:0x7}

def append_hex(a,b):
    sizeof_b = 0
    while((b>>sizeof_b) > 0):
        sizeof_b += 1

    sizeof_b += sizeof_b % 4

    return a << sizeof_b) | b

def encm(m,k,n):
    mx = m >> 6
    my = m & 0x000000111111
    if n == 1:
        return (my << 6) & (mx ^ f(my,k))
    else:
        mz = (my << 6) & (mx ^ f(my,k))
        return encm(mz, k, n-1)

def f(z,k):
    z1 = z & 0x110000
    z2 = (m & 0x001100) >> 2
    z3 = m & 0x000011
    n1_1 = z1 >> 1
    n1_2 = z1 & 0x10
    n2_1 = z2 >> 1
    n2_2 = z2 & 0x10
    n3_1 = z3 >> 1
    n3_2 = z3 & 0x10
    p1_1 = S0[n1_1]
    p1_2 = S1[n1_2]
    p2_1 = S0[n2_1]
    p2_2 = S1[n2_2]
    p3_1 = S0[n3_1]
    p3_2 = S1[n3_2]
    if(z1 >> 1) == 0x1:
        tmp = p1_1
        p1_1 = p1_2
        p1_2 = tmp
    if (z2 >> 1) == 0x1:
        tmp = p2_1
        p2_1 = p2_2
        p2_2 = tmp
    if (z3 >> 1) == 0x1:
        tmp = p3_1
        p3_1 = p3_2
        p3_2 = tmp
    tmp = p1_1
    p2_1 = p1_1
    p1_1 = tmp
    tmp = p1_2
    p1_2 = p3_2
    p3_2=tmp
    tmp = p2_2
    p3_1 = p2_2
    p2_2 = tmp
    return (p1_1 << 5) & (p1_2 << 4) & (p2_1 << 3) & (p2_2 << 2) & (p3_1 << 1) & p1

def decm(m,k,n):
    mx = m & 0x000000111111
    my = m >> 6
    if n == 1:
        return (my << 6) & (mx ^ f(my,k))
    else:
        mz = (my << 6) & (mx ^ f(my,k))
        return decm(mz, k, n-1)
