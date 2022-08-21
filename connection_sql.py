import mysql.connector as connector


class DbConnections:
    def __init__(self):
        self.my_connection = connector.connect(host="localhost",
                                               port="3306",
                                               user="root",
                                               password="rose67",
                                               database="python_test"
                                               )

        if self.my_connection.is_connected():
            print("Successfully connected to mysql")
        else:
            print("Not connected to mysql")

    def create_table(self, table_name, id, name, last_name):
        create_table = f"create table if not exists {table_name}" \
                       f" ({id} int primary key, {name} varchar(30), {last_name} varchar(30))"
        create_query = self.my_connection.cursor().execute(create_table)

    def insert_table(self, emp_id, emp_name, emp_last_name):
        insert_table = f"insert into employee (emp_id, emp_name, emp_last_name)" \
                       f" values ({emp_id}, '{emp_name}', '{emp_last_name}')"
        print(insert_table)
        insert_query = self.my_connection.cursor()
        insert_query.execute(insert_table)
        self.my_connection.commit()
        print("data inserted.")

    def fetch_all(self):
        select_query = f"select * from employee"
        show_table = self.my_connection.cursor()
        show_table.execute(select_query)
        for row in show_table:
            print(f"Employee id: {row[0]}")
            print(f"Employee name: {row[1]}")
            print(f"Employee lastname: {row[2]}")
            print()
            print()

    def fetch_by_id(self, by_id):
        select_query = f"select * from employee where emp_id = {by_id}"
        show_row = self.my_connection.cursor()
        show_row.execute(select_query)
        for row in show_row:
            print(row)

    def delete_by_id(self, row_id):
        delete_query = f"delete from employee where emp_id = {row_id}"
        delete_from_table = self.my_connection.cursor()
        delete_from_table.execute(delete_query)
        self.my_connection.commit()
        print(f"a row with the id {row_id} was deleted")

    def update_by_id(self, new_name, new_last_name, id):
        update_query = f"update employee set emp_name = '{new_name}'," \
                       f"emp_last_name = '{new_last_name}' where emp_id = {id}"
        update_table = self.my_connection.cursor()
        update_table.execute(update_query)
        self.my_connection.commit()
        print(f"the row updated from id {id} to {new_name} ")


