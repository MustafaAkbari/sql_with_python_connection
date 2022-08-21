from connection_sql import DbConnections

print("There is a database by the name of employee\nIt's columns are emp_id, emp_name, emp_last_name\n"
      "You can update, delete_employee, insert and read from this table")
print("To delete_employee press '1'\nTo insert press '2'\nTo update press '3'\nTo read press '4'"
      "\nTo read a single row press '5'\nTo exit from program press '0'")
connect = DbConnections()

while True:
      user_choice = input("take a choice >> ")

      if user_choice == "1":
            connect.delete_by_id(int(input("Type an id to delete >> ")))
      elif user_choice == "2":
            connect.insert_table(int(input("emp_id: ")), input("emp_name: "), input("emp_last_name: "))
      elif user_choice == "3":
            connect.update_by_id(input("New name: "), input("Last_name: "), int(input("The id you want to update: ")))
      elif user_choice == "4":
            connect.fetch_all()
      elif user_choice == "5":
            connect.fetch_by_id(int(input("Enter an id: ")))
      elif user_choice == "0":
            break
      else:
            print("Wrong Entry!")

