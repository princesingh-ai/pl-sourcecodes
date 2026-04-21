import json

try:
    with open("normaljson.json", "r") as f:
        data = json.load(f)
        print(data)

except FileNotFoundError:
    print("The file name is inncorrect or the file does not exist.")

except json.JSONDecodeError:
    print("The file does not contain valid JSON.")

except Exception as e:
    print(f"An error occurred: {e}")