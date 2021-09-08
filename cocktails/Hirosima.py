from command.base.stock import Stock


class Hirosima(Stock):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'HIROSHIMA'

    def get_name(self):
        return self.name

    def get_description(self):
        return "Do you like shots? Then try this creamy, herbal and sweet, absinthe and sambuca-based cocktail, alcoholic and strong."