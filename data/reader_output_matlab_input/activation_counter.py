import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# File paths for the 5 CSV files (update with your actual file paths)
csv_files = ["Binarized_Data_Group_1", "Binarized_Data_Group_2", "Binarized_Data_Group_3", "Binarized_Data_Group_10", "Binarized_Data_Group_11"]
# Number of regions (rows) and files (columns)
num_regions = 7
num_files = len(csv_files)

# Initialize the matrix with zeros
matrix = np.zeros((num_regions, num_files), dtype=float)

# Populate the matrix
for col, file in enumerate(csv_files):
    # Load the binarized data (-1 and 1) from the current CSV file
    data = pd.read_csv(file, header=None).to_numpy()

    # Count the activations (number of `1` values) for each region
    activations = np.sum(data == 1, axis=1)

    # Calculate the activation frequency (fraction of columns with activations)
    num_columns = data.shape[1]
    region_activation_frequency = activations / num_columns

    # Assign the values to the matrix
    matrix[:, col] = region_activation_frequency


labels = ["ASD","TD \n(ABIDE)","ASD + \nADHD","TD \n(ADHD200)","ADHD"]
# Display the matrix
plt.figure(figsize=(8, 6))
plt.imshow(matrix, cmap="hot", aspect="auto")
plt.colorbar(label="Activation Frequency")
plt.xticks(ticks=range(num_files), labels=[f"{i}" for i in labels])
plt.yticks(ticks=range(num_regions), labels=[f"Region {i + 1}" for i in range(num_regions)])
plt.title("Activation Frequency per Region for each group")
plt.xlabel("Groups")
plt.ylabel("Regions")
plt.show()