import json
import random
import os

# Ensure the datasets folder exists
DATASET_FOLDER = "datasets"
os.makedirs(DATASET_FOLDER, exist_ok=True)

def generate_closest_pair_inputs():
    for i in range(10):
        num_points = random.randint(100, 200)  # Random number of points between 100 and 200
        points = [[round(random.uniform(-1000, 1000), 2), round(random.uniform(-1000, 1000), 2)] for _ in range(num_points)]
        file_path = os.path.join(DATASET_FOLDER, f"closest_pair_input_{i+1}.json")
        with open(file_path, "w") as f:
            json.dump(points, f, indent=4)

def generate_karatsuba_inputs():
    for i in range(10):
        num1 = random.randint(1000000, 9999999)  # 7-digit integer
        num2 = random.randint(1000000, 9999999)  # 7-digit integer
        file_path = os.path.join(DATASET_FOLDER, f"karatsuba_input_{i+1}.json")
        with open(file_path, "w") as f:
            json.dump([num1, num2], f, indent=4)

if __name__ == "__main__":
    print("Generating inputs...")
    generate_closest_pair_inputs()
    generate_karatsuba_inputs()
    print(f"Inputs generated and saved in the '{DATASET_FOLDER}' folder.")
