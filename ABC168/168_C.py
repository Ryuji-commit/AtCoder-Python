import math

A, B, H, M = map(int, input().split())
A_rad = H/12*360 + ((M/60)*(360/12))
B_rad = M/60*360
rad = abs(A_rad - B_rad)
if rad >= 180:
    rad = 360 - rad

cosAB = round(math.cos(math.radians(rad)), 13)
C = ((A**2 + B**2) - 2*A*B*cosAB)**0.5
print(C)
