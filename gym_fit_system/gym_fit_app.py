# gym_fit_app.py
from connect_db import get_connection
from users_dao import UsersDAO
from user import User

def menu():
    print("\n=== Gym Fit System ===")
    print("1) List users")
    print("2) Add user")
    print("3) Update membership")
    print("4) Delete user")
    print("5) Exit")

def main():
    connection = get_connection()
    dao = UsersDAO(connection)

    try:
        while True:
            menu()
            option = input("Choose an option: ").strip()

            if option == "1":
                users = dao.get_all_users()
                if not users:
                    print("No users found.")
                else:
                    for u in users:
                        # print bonito (você pode trocar o formato)
                        print(f"Id: {u.id} | Name: {u.name} | Lastname: {u.lastname} | Membership: {u.membership}")

            elif option == "2":
                name = input("Name: ").strip()
                lastname = input("Lastname: ").strip()
                membership = input("Membership: ").strip()

                user = User(name=name, lastname=lastname, membership=membership)
                new_id = dao.add_user(user)
                print(f"User added with id: {new_id}")

            elif option == "3":
                user_id = int(input("User id to update: ").strip())
                membership = input("New membership: ").strip()

                ok = dao.update_membership(user_id, membership)
                if ok:
                    print("Membership updated successfully.")
                else:
                    print("User not found.")

            elif option == "4":
                user_id = int(input("User id to delete: ").strip())
                ok = dao.delete_user(user_id)

                if ok:
                    print("User deleted successfully.")
                else:
                    print("User not found.")

            elif option == "5":
                print("Bye!")
                break

            else:
                print("Invalid option. Try again.")

    finally:
        connection.close()

if __name__ == "__main__":
    main()
