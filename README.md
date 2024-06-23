# Customer Database Management System

This repository contains a comprehensive Python application for managing customer data. The application leverages Tkinter for the graphical user interface (GUI) and SQLite for database operations, providing a user-friendly platform for data entry, retrieval, update, and deletion.

## Features

- **Execute SQL Commands**: Users can input and execute custom SQL queries directly from the interface.
- **Data Management**:
  - **Add Records**: Add new customer records with details such as name, email, and city.
  - **Update Records**: Modify existing customer information.
  - **Delete Records**: Remove customer records that are no longer needed.
- **Display Data**: Fetch and display all customer records in a list format for easy viewing and selection.
- **Interactive Interface**: Responsive and intuitive GUI for efficient database interactions.

## File Overview

### `GUI_Interface.py`

This file contains the main application code for the GUI. It includes:

- **Tkinter GUI**: Set up the main application window and widgets for user interaction.
- **Functions**:
  - `execute_sql()`: Executes user-inputted SQL commands.
  - `populate_table()`: Fetches and displays all records from the database.
  - `add_record()`: Adds a new customer record to the database.
  - `select_item(event)`: Selects a record from the list for viewing or editing.
  - `delete_record()`: Deletes a selected customer record.
  - `update_record()`: Updates an existing customer record.
- **Event Handling**: Binds functions to GUI events for user interactions.
- **App Initialization**: Starts the Tkinter main loop to run the application.

### `Customer_Database.py`

This file contains the `Database` class for handling SQLite operations. It includes:

- **Database Initialization**: Creates a `Customer` table if it doesn't exist.
- **CRUD Operations**:
  - `fetch()`: Retrieves all records from the `Customer` table.
  - `insert()`: Adds a new record to the `Customer` table.
  - `remove()`: Deletes a record from the `Customer` table by ID.
  - `update()`: Updates an existing record in the `Customer` table.
  - `execute_query()`: Executes custom SQL queries and returns results.
- **Connection Management**: Manages the SQLite database connection lifecycle.
