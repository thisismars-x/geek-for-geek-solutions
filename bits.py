''' Utilities for bit manipulation. '''

def Count_Set_Bits(n: int) -> int:
    count = 0

    while n:
        n &= (n - 1)
        count += 1

    return count

def Set_Bit_At(n: int, index: int) -> int:
    return n | (1 << index)

def Clear_Bit_At(n: int, index: int) -> int:
    return n & ~(1 << index);

def Toggle_Bit_At(n: int, index: int) -> int:
    return n ^ (1 << index)

def Check_Bit_Status(n: int, index: int) -> bool:
    return n & (1 << index) != 0

def Check_Power_Two(n: int) -> bool:
    return (n & n - 1) == 0

def Position_Of_Rightmost_Bit(n: int) -> int:
    from math import log2
    return int(log2(n & -n))

def Swap_Without_Temps(a, b):
    a = a ^ b
    b = b ^ a
    a = a ^ b

    return a, b
