# interactive_dashboard

This application is a simple web-based dashboard for managing customer data, built using the Reflex framework. It allows users to add new customer entries and visualize gender distribution through a bar chart.

## Features

-   Add new users with their name, email, and gender.
-   Display a list of users in a table format.
-   Visualize gender distribution using a bar chart.

## File Structure

/interactive_dashboard/interactive_dashboard.py: Main application code.

## Code Overview

### User Model

Represents a user with attributes for name, email, and gender.

```python
class User(rx.Base):
    name: str
    email: str
    gender: str
```

### State Management

Maintains a list of users and prepares data for visualization.

```python
class State(rx.State):
    users: list[User] = [...]
    users_for_graph: list[dict] = []
```

### Adding Users

Adds a new user and updates the gender distribution data.

```python
def add_user(self, form_data: dict):
    self.users.append(User(**form_data))
    self.transform_data()
```

### User Display

Renders a user in a table row format.

```python
def show_user(user: User):
    ...
```

### User Input Form

Creates a dialog for adding new users with input fields for name, email, and gender.

```python
def add_customer_button() -> rx.Component:
    ...
```

### Visualization

Generates a bar chart to visualize the gender distribution of users.

```python
def graph():
    ...
```

### Main Application

Initializes the application and sets the main page to display the user table and graph.

```python
app = rx.App(...)
app.add_page(index, ...)
```

# Instalation

-   Ensure you have Python installed, then create and start a virtual environment

```bash
make create-venv
```

-   Install the dependencies in your machine

```bash
make install
```

-   Run the project in your machine

```bash
make run-local
```

-   After run, the app will be running at: http://localhost:3000 and the backend will be running at: http://0.0.0.0:8000. Open your web browser and navigate to the local server address (usually http://localhost:3000).
-   Use the "Add User" button to input new user data.
-   View the list of users and the corresponding gender distribution chart.

# Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

# License

This project is licensed under the Apache License 2.0.
See the LICENSE file for details.
