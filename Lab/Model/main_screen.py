import multitasking

from Model.base_model import BaseScreenModel

multitasking.set_max_threads(10)


class MainScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.MainScreen.main_screen.MainScreenView` class.
    """

    def __init__(self, base):
        self.base = base
        # Dict:
        #     'login': 'User Login'
        #     'password': '12345'
        self.user_data = dict()
        self._data_validation_status = None

    @property
    def data_validation_status(self):
        return self._data_validation_status

    @data_validation_status.setter
    def data_validation_status(self, value):
        self._data_validation_status = value
        # We notify the View -
        # :class:`~View.MainScreen.main_screen.MainScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers()

    @multitasking.task
    def chek_data(self):
        """
        Get data from the database and compares this data with the data entered
        by the user.
        This method is completely asynchronous. It does not return any value.
        """

        data = self.base.get_data_from_base_users()
        data_validation_status = False

        for key in data:
            if data[key] == self.user_data:
                data_validation_status = True
                break
        self.data_validation_status = data_validation_status

    def set_user_data(self, key, value):
        """Sets a dictionary of data that the user enters."""

        self.user_data[key] = value

    def reset_data_validation_status(self):
        self.data_validation_status = None

