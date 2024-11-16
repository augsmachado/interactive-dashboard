"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx


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
            rx.table.row(
                rx.table.cell("Danilo Sousa"),
                rx.table.cell("danilo@example.com"),
                rx.table.cell("Male"),
            ),
            rx.table.row(
                rx.table.cell("Zahra Ambessa"),
                rx.table.cell("zahra@example.com"),
                rx.table.cell("Female"),
            ),
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
