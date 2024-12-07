import csv

def count_columns_in_csv(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        # Read the first row to count the number of columns
        first_row = next(reader)
        column_count = len(first_row)
        
    return column_count

# Test the function with the path to your CSV file
csv_file_path = "Binarized_Data_Group_1"
column_count = count_columns_in_csv(csv_file_path)
print(f"The {csv_file_path} file has {column_count} columns.")
print(column_count/175)

csv_file_path = "Binarized_Data_Group_2"
column_count = count_columns_in_csv(csv_file_path)
print(f"The {csv_file_path} file has {column_count} columns.")
print(column_count/175)
csv_file_path = "Binarized_Data_Group_3"
column_count = count_columns_in_csv(csv_file_path)
print(f"The {csv_file_path} file has {column_count} columns.")
print(column_count/175)
csv_file_path = "Binarized_Data_Group_10"
column_count = count_columns_in_csv(csv_file_path)
print(f"The {csv_file_path} file has {column_count} columns.")
print(column_count/172)
csv_file_path = "Binarized_Data_Group_11"
column_count = count_columns_in_csv(csv_file_path)
print(f"The {csv_file_path} file has {column_count} columns.")
print(column_count/172)



