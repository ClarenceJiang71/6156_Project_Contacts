import pymysql
import os


class AccountResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():
        usr = os.environ.get("DBUSER")
        PW = os.environ.get("DBPW")
        h = os.environ.get("DBHOST")

        conn = pymysql.connect(
            user=usr,
            password=PW,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    # This method use account ID as
    def get_by_key(table_name, key):

        sql = "SELECT * FROM contacts."+table_name+" where accountId=%s"
        conn = AccountResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    def get_by_union_info(key):

        sql = "SELECT * FROM contacts.email join contacts.phone using (accountId) where accountId=%s"
        conn = AccountResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

