from prompt_toolkit import Application
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import HSplit, VSplit, Window
from prompt_toolkit.widgets import Box, Frame, TextArea


def main():
    # Create the layout.
    layout = Layout(
        HSplit([
            Frame(
                title='Hello',
                body=TextArea(
                    text='Hello, World!',
                    width=40,
                    height=10
                )
            ),
            Window(height=1, char='-'),
            Box(
                body=TextArea(
                    text='This is a demo of prompt_toolkit.',
                    height=10
                ),
                padding=1
            ),
        ])
    )

    # Create the application.
    application = Application(layout=layout, full_screen=True)

    # Run the application.
    application.run()


if __name__ == '__main__':
    main()
