import json
import csv

def json_to_csv(json_file, csv_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)

        if not data:
            print("The JSON file is empty.")
            return

        # Assuming the JSON data is a list of dictionaries
        keys = data[0].keys()

        with open(csv_file, 'w', newline='') as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

        print(f"Successfully converted '{json_file}' to '{csv_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{json_file}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{json_file}' does not contain valid JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    json_file = "data.json"
    csv_file = "data.csv"
    json_to_csv(json_file, csv_file)

if __name__ == "__main__":
    main()