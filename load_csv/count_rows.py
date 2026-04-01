import csv

def count_rows(file_path):
    try:
        with open(file_path, "r", newline="") as file:
            reader = csv.reader(file)
            row_count = sum( 1 for row in reader)
            return row_count
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"Error while counting rows: {e}")

def main():
    file_path = "data.csv"
    row_count = count_rows(file_path)
    if row_count is not None:
        print(f"The number of rows in the file '{file_path}' is: {row_count}")

if __name__ == "__main__":
    main()