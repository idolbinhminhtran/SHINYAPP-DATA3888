from shiny import App, ui, render


app_ui = ui.page_navbar(
    
    ui.nav_panel(
        "Home",
        ui.h1("Welcome to the Home tab"),
        ui.p("This is the home page content.")
    ),
    ui.nav_panel(
        "About",
        ui.h2("About this App"),
        ui.p("This app is a scaffold for a Python Shiny application with a navbar.")
    ),
    ui.nav_panel(
        "Contact",
        ui.h3("Contact Information"),
        ui.p("Email: example@example.com")
    ),
    
    title="volatility Explorer"
)


def server(input, output, session):
    
    pass

app = App(app_ui, server)

if __name__ == "__main__":
    app.run()
