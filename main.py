import json
import os
import random

LOST_FILE = "lost_items.json"
FOUND_FILE = "found_items.json"


# ---------- DATABASE FUNCTIONS ----------

def load_data(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            json.dump([], f)

    with open(filename, "r") as f:
        return json.load(f)


def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def generate_id():
    return random.randint(1000, 9999)


# ---------- CRUD OPERATIONS ----------

def insert_item(status):
    filename = LOST_FILE if status == "lost" else FOUND_FILE
    data = load_data(filename)

    item = {
        "id": generate_id(),
        "item_name": input("Item Name: "),
        "description": input("Description: "),
        "location": input("Location: "),
        "date": input("Date: "),
        "category": input("Category (optional): "),
        "contact": input("Contact (optional): "),
        "status": status
    }

    data.append(item)
    save_data(filename, data)

    print("Item added successfully!\n")


def search_items():
    keyword = input("Enter keyword to search: ").lower()

    lost = load_data(LOST_FILE)
    found = load_data(FOUND_FILE)

    results = []

    for item in lost + found:
        combined = (
            item["item_name"] +
            item["description"] +
            item["location"] +
            item["category"]
        ).lower()

        if keyword in combined:
            results.append(item)

    if not results:
        print("No items found.\n")
        return

    for item in results:
        print("\nItem ID:", item["id"])
        print("Name:", item["item_name"])
        print("Location:", item["location"])
        print("Status:", item["status"])


def update_item():
    item_id = int(input("Enter Item ID to update: "))

    for filename in [LOST_FILE, FOUND_FILE]:
        data = load_data(filename)

        for item in data:
            if item["id"] == item_id:
                item["item_name"] = input("New name: ")
                item["description"] = input("New description: ")
                item["location"] = input("New location: ")

                save_data(filename, data)
                print("Item updated.\n")
                return

    print("Item not found.\n")


def delete_item():
    item_id = int(input("Enter Item ID to delete: "))

    for filename in [LOST_FILE, FOUND_FILE]:
        data = load_data(filename)

        new_data = [item for item in data if item["id"] != item_id]

        if len(new_data) != len(data):
            save_data(filename, new_data)
            print("Item deleted.\n")
            return

    print("Item not found.\n")


# ---------- SMART MATCHING ----------

def calculate_match_score(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())

    common = words1.intersection(words2)

    score = len(common) / max(len(words1), len(words2)) * 100
    return score, common


def match_items():
    lost_items = load_data(LOST_FILE)
    found_items = load_data(FOUND_FILE)

    print("\nMatching lost and found items...\n")

    for lost in lost_items:
        for found in found_items:

            score, common = calculate_match_score(
                lost["item_name"], found["item_name"]
            )

            if score >= 40:
                print("Possible Match Found!")
                print("Lost:", lost["item_name"])
                print("Found:", found["item_name"])
                print("Common words:", common)
                print("Match confidence:", round(score, 2), "%\n")


# ---------- MAIN MENU ----------

def main():
    while True:
        print("\n==== FIND MY STUFF ====")
        print("1 Add Lost Item")
        print("2 Add Found Item")
        print("3 Search Items")
        print("4 Match Lost and Found")
        print("5 Update Item")
        print("6 Delete Item")
        print("7 Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_item("lost")

        elif choice == "2":
            insert_item("found")

        elif choice == "3":
            search_items()

        elif choice == "4":
            match_items()

        elif choice == "5":
            update_item()

        elif choice == "6":
            delete_item()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


main()
