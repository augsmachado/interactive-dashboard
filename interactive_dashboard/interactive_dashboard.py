"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx


class User(rx.Base):
    """The user model."""
    name: str
    email: str
    gender: str


class State(rx.State):
    users: list[User] = [
        User(
            name="Danilo Sousa",
            email="danilo@example.com",
            gender="Male"
        ),
        User(
            name="Zahra Ambessa",
            email="zahra@example.com",
            gender="Female"
        ),
    ]


def show_user(user: User):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
    )


def index() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Name"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Gender"),
            ),
        ),
        rx.table.body(
            rx.foreach(State.users, show_user),
        ),
        variant="surface",
        size="3",
    )


# Define app and the component we just defined (index) to a page using
# `app.add_page(index)`. The function name (in this example index) which defines
# the component, must be what we pass into the add_page. The definition of the
# app and adding a component to a page are required for every Reflex app.
app = rx.App()
app.add_page(index)
