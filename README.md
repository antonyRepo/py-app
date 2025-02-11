# Sample Car Sales Application

## Overview
This is a Python-based desktop application built using the `tkinter` library for the user interface and `SQLite` for database management. The application allows users to input and save car sales details, including:
- Car Model
- Color
- Price
- Customer Name

Each submission is saved to a local SQLite database, and the program displays the saved details after submission.

---

## Requirements
To run this application, you need:
- **Python 3.x** (preferably 3.6 or higher)
- **Tkinter** (comes pre-installed with Python)
- **SQLite3** (comes pre-installed with Python)
- **DB Browser for SQLite** (Download to access the DB file) - Referrence video - https://www.youtube.com/watch?v=1Iy87jyA3Xs

---

## Setup Instructions
1. **Clone or Download the Code**:
   - Download the Python script (`app.py`) or clone the repository - [py-app](https://github.com/antonyRepo/py-app.git)

2. **Run the Application**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script using the following command:
     ```bash
     python app.py
     ```

3. **Database File**:
   - The application will automatically create a SQLite database file named `car_sales.db` in the same directory as the script.

---

## How to Use the Application
1. **Launch the Application**:
   - Run the script as described in the setup instructions.
   - A window titled **"Car Sales Application"** will open.

2. **Input Car Details**:
   - Fill in the following fields:
     - **Car Model**: Enter the model of the car (e.g., "Toyota Camry").
     - **Color**: Enter the color of the car (e.g., "Red").
     - **Price**: Enter the price of the car (e.g., "25000").
     - **Customer Name**: Enter the name of the customer (e.g., "John Doe").

3. **Submit the Details**:
   - Click the **"Submit"** button to save the details to the database.
   - A message box will appear displaying the saved details.

4. **Clear Fields**:
   - After submission, the input fields will be cleared automatically, allowing you to enter new details.

5. **View Database**:
   - To view all saved car sales, open the `car_sales.db` file using a SQLite browser (e.g., [DB Browser for SQLite](https://sqlitebrowser.org/)).

---

## Database Schema
The application uses a SQLite database with the following schema:

### Table: `sales`
| Column Name    | Data Type | Description                     |
|----------------|-----------|---------------------------------|
| `id`           | INTEGER   | Primary key, auto-incremented. |
| `car_model`    | TEXT      | Model of the car.              |
| `color`        | TEXT      | Color of the car.              |
| `price`        | REAL      | Price of the car.              |
| `customer_name`| TEXT      | Name of the customer.          |

---

## Example Usage
1. **Input**:
   - Car Model: `Toyota Camry`
   - Color: `Red`
   - Price: `25000`
   - Customer Name: `John Doe`

2. **Submit**:
   - Click the **"Submit"** button.

3. **Output**:
   - A message box will display:
     ```
     Sale Details:

     Car Model: Toyota Camry
     Color: Red
     Price: $25000.00
     Customer Name: John Doe
     ```

4. **Database Entry**:
   - The `sales` table will have a new row:
     | id  | car_model     | color | price  | customer_name |
     |-----|---------------|-------|--------|---------------|
     | 1   | Toyota Camry  | Red   | 25000  | John Doe      |

---

## Future Enhancements
[To Do]
