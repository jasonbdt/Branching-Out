import json
from typing import Any

USERS_FILE = "users.json"


def get_users() -> list[dict[str, Any]] | None:
    """
    Read ``users.json`` file and returns the values as dictionary.
    Returns None if file was unable to load.

    Raises:
        FileNotFoundError: File with users not found.

    Returns:
        dict[str, Any]: A collection of users as dictionary.
    """
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Unable to load users, file not found!")


def display_users(users: list[dict[str, Any]]) -> None:
    """
    Displays each user in ``users`` on a new line.

    Args:
        users (dict[str, Any]): List of user dictionaries.

    Returns:
        None
    """
    for user in users:
        print(user)


def filter_users_by_name(name: str) -> None:
    """
    Filter users by name and display the results.

    Args:
        name (str): Name of the user to filter by.

    Returns:
        None
    """
    users = get_users()
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    display_users(filtered_users)


def filter_users_by_age(age):
    """
    Filter users by age and display the results.

    Args:
        age (str): Age of the user to filter by.

    Returns:
        None
    """
    users = get_users()
    filtered_users = [user for user in users if user["age"] == int(age)]
    display_users(filtered_users)


def filter_users_by_email(email):
    """
    Filter users by email and display the results.

    Args:
        email (str): Email of the user to filter by.

    Returns:
        None
    """
    users = get_users()
    filtered_users = [user for user in users if user["email"] == email]
    display_users(filtered_users)


def main():
    filter_option = input(
        "What would you like to filter by? (Currently, only "
        "'age', 'email' and 'name' is supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = input("Enter an age to filter users: ").strip()
        filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
