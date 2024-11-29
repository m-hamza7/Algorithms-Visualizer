import math
import json

from math import sqrt

# Closest Pair Algorithm
def process_closest_pair(file_path):

    # Read points from the file
    with open(file_path, "r") as file:
        points = json.load(file)

    # Helper function to calculate distance
    def distance(p1, p2):
        return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    # Brute force to find the closest pair (for simplicity)
    min_dist = float("inf")
    closest_pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                closest_pair = (points[i], points[j])

    return points, closest_pair, min_dist

# Karatsuba Multiplication Algorithm
def process_karatsuba(file_path):

    # Read numbers from the file
    with open(file_path, "r") as file:
        num1, num2 = json.load(file)

    def karatsuba(x, y):
        if x < 10 or y < 10:
            return {"inputs": (x, y), "result": x * y, "children": []}

        n = max(len(str(x)), len(str(y)))
        m = n // 2

        high1, low1 = divmod(x, 10**m)
        high2, low2 = divmod(y, 10**m)

        z0 = karatsuba(low1, low2)
        z1 = karatsuba(low1 + high1, low2 + high2)
        z2 = karatsuba(high1, high2)

        result = (z2["result"] * 10**(2*m)) + ((z1["result"] - z2["result"] - z0["result"]) * 10**m) + z0["result"]
        return {
            "inputs": (x, y),
            "result": result,
            "children": [z2, z1, z0],
        }

    return karatsuba(num1, num2)
