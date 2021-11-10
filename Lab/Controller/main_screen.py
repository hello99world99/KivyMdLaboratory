from typing import NoReturn
import importlib

import View.MainScreen.main_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.MainScreen.main_screen)


class MainScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = View.MainScreen.main_screen.MainScreenView(
            controller=self, model=self.model
        )

    def set_user_data(self, key, value) -> NoReturn:
        """Called every time the user enters text into the text fields."""

        self.model.set_user_data(key, value)

    def on_tap_button_login(self) -> NoReturn:
        """Called when the `LOGIN` button is pressed."""

        self.view.show_dialog_wait()
        self.model.chek_data()

    def reset_data_validation_status(self, *args) -> NoReturn:
        self.model.reset_data_validation_status()

    def get_view(self) -> View.MainScreen.main_screen.MainScreenView:
        return self.view
