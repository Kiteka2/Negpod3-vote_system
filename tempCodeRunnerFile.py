    connection = mysql.connector.connect(**db_config)

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    try:
        # Create a user with a wildcard for username and hostname
        cursor.execute("CREATE USER '%'@'%' IDENTIFIED BY 'password';")

        # Grant all privileges on all databases and tables
        cursor.execute("GRANT ALL PRIVILEGES ON *.* TO '%'@'%';")

        # Apply changes
        connection.commit()
        print("Access granted to everyone.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()