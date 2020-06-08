import math
from decimal import Decimal, getcontext

input_list = input().split()
A = int(input_list[0])
B = input_list[1]
final_B = Decimal(B)
print(math.floor(final_B * A))

