import sqlite3
from datetime import datetime

DATABASE_NAME = "chat_history.db"
# الاتصال بقاعدة البيانات
def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn
# إنشاء الجداول
def init_db():

    conn = get_connection()
    cursor = conn.cursor()
    # جدول المحادثات
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT NOT NULL,

            created_at TEXT NOT NULL )
    """)
    # جدول الرسائل
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            conversation_id INTEGER NOT NULL,

            role TEXT NOT NULL,

            message TEXT NOT NULL,

            created_at TEXT NOT NULL,

            FOREIGN KEY(conversation_id)
            REFERENCES conversations(id) )
    """)

    conn.commit()
    conn.close()
# إنشاء محادثة جديدة
def create_conversation(title):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO conversations
        (title, created_at)

        VALUES (?,?)

    """,
    (
        title,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    conversation_id = cursor.lastrowid

    conn.commit()
    conn.close()
    return conversation_id
# حفظ رسالة
def save_message(

        conversation_id,
        role,
        message

):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO messages
        (
            conversation_id,
            role,
            message,
            created_at
        )

        VALUES (?,?,?,?)
    """,
    (
        conversation_id,
        role,
        message,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    conn.commit()
    conn.close()
# جميع المحادثات
def get_conversations():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM conversations
        ORDER BY id DESC
    """)
    rows = cursor.fetchall()

    conn.close()

    return rows
# رسائل محادثة
def get_messages(conversation_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM messages
        WHERE conversation_id=?
        ORDER BY id ASC
    """,
    (
        conversation_id,
    ))
    rows = cursor.fetchall()
    conn.close()
    return rows
# حذف محادثة
def delete_conversation(conversation_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM messages=
        WHERE conversation_id=?
    """,
    (
        conversation_id,
    ))
    cursor.execute("""

        DELETE FROM conversations

        WHERE id=?
    """,
    (
        conversation_id,
    ))
    conn.commit()
    conn.close()
# حذف جميع المحادثات
def delete_all_conversations():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM messages")
    cursor.execute("DELETE FROM conversations")
    conn.commit()
    conn.close()
# تشغيل إنشاء القاعدة تلقائياً
init_db()