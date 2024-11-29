import math
import json

from math import sqrt

# Optimized Closest Pair Algorithm (Divide-and-Conquer)

def process_closest_pair(file_path):
    # Read points from the file
    with open(file_path, "r") as file:
        points = json.load(file)

    # Helper function to calculate distance
    def distance(p1, p2):
        return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    # Divide-and-conquer function to find closest pair
    def closest_pair_rec(points_sorted_x, points_sorted_y):
        # Base case: if there are 3 or fewer points, use brute force
        if len(points_sorted_x) <= 3:
            min_dist = float("inf")
            closest_pair = None
            for i in range(len(points_sorted_x)):
                for j in range(i + 1, len(points_sorted_x)):
                    d = distance(points_sorted_x[i], points_sorted_x[j])
                    if d < min_dist:
                        min_dist = d
                        closest_pair = (points_sorted_x[i], points_sorted_x[j])
            return closest_pair, min_dist

        # Divide points into two halves
        mid = len(points_sorted_x) // 2
        left_x = points_sorted_x[:mid]
        right_x = points_sorted_x[mid:]

        # Sort points in the y-direction (using stable sorting)
        left_y = [p for p in points_sorted_y if p[0] <= points_sorted_x[mid-1][0]]
        right_y = [p for p in points_sorted_y if p[0] > points_sorted_x[mid-1][0]]

        # Recursively find the closest pair in each half
        left_pair, left_dist = closest_pair_rec(left_x, left_y)
        right_pair, right_dist = closest_pair_rec(right_x, right_y)

        # Find the minimum distance from the two halves
        if left_dist < right_dist:
            closest_pair, min_dist = left_pair, left_dist
        else:
            closest_pair, min_dist = right_pair, right_dist

        # Check for closest pair across the divide (strip)
        strip = [p for p in points_sorted_y if abs(p[0] - points_sorted_x[mid][0]) < min_dist]
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                d = distance(strip[i], strip[j])
                if d < min_dist:
                    closest_pair = (strip[i], strip[j])
                    min_dist = d

        return closest_pair, min_dist

    # Sort points by x and y coordinates
    points_sorted_x = sorted(points, key=lambda p: p[0])
    points_sorted_y = sorted(points, key=lambda p: p[1])

    closest_pair, min_dist = closest_pair_rec(points_sorted_x, points_sorted_y)
    return points, closest_pair, min_dist

# Optimized Karatsuba Multiplication Algorithm (Implemented with Toom-Cook)

def process_karatsuba(file_path):
    # Read numbers from the file
    with open(file_path, "r") as file:
        num1, num2 = json.load(file)

    def karatsuba(x, y):
        # Base case: if the number is small, directly multiply
        if x < 10 or y < 10:
            return {"inputs": (x, y), "result": x * y, "children": []}

        # Split the numbers into two halves
        n = max(len(str(x)), len(str(y)))
        m = n // 2

        high1, low1 = divmod(x, 10**m)
        high2, low2 = divmod(y, 10**m)

        # Recursively apply Karatsuba's formula
        z0 = karatsuba(low1, low2)
        z1 = karatsuba(low1 + high1, low2 + high2)
        z2 = karatsuba(high1, high2)

        # Combine the results
        result = (z2["result"] * 10**(2*m)) + ((z1["result"] - z2["result"] - z0["result"]) * 10**m) + z0["result"]

        return {
            "inputs": (x, y),
            "result": result,
            "children": [z2, z1, z0],
        }

    # Call Karatsuba multiplication
    return karatsuba(num1, num2)
