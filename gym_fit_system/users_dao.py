# users_dao.py
from typing import List, Optional
from user import User

class UsersDAO:
    def __init__(self, connection):
        self.connection = connection

    def get_all_users(self) -> List[User]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, lastname, membership FROM users")
        rows = cursor.fetchall()
        cursor.close()
        return [User(id=r[0], name=r[1], lastname=r[2], membership=r[3]) for r in rows]

    def add_user(self, user: User) -> int:
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO users (name, lastname, membership) VALUES (%s, %s, %s)",
            (user.name, user.lastname, user.membership)
        )
        self.connection.commit()
        new_id = cursor.lastrowid
        cursor.close()
        return new_id

    def update_membership(self, user_id: int, membership: str) -> bool:
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE users SET membership = %s WHERE id = %s",
            (membership, user_id)
        )
        self.connection.commit()
        updated = cursor.rowcount > 0
        cursor.close()
        return updated

    def delete_user(self, user_id: int) -> bool:
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        self.connection.commit()
        deleted = cursor.rowcount > 0
        cursor.close()
        return deleted

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, lastname, membership FROM users WHERE id = %s", (user_id,))
        row = cursor.fetchone()
        cursor.close()
        if not row:
            return None
        return User(id=row[0], name=row[1], lastname=row[2], membership=row[3])
