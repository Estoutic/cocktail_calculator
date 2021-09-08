import discord

from command.base.Command import Command


class Menu(Command):

    def __init__(self, menu, prefix) -> None:
        super().__init__()
        self.menu = menu
        self.prefix = prefix

    def execute(self, send_func, args: [str]):
        embed = discord.Embed(colour=discord.Colour.from_rgb(106, 192, 245))
        embed.add_field(name="special menu from Estoutic",
                        value="https://github.com/Estoutic/cocktail_calculator",
                        inline=False, )
        for key in self.menu:
            embed.add_field(name=self.menu[key].get_name(), value=self.menu[key].get_description(), inline=False)

        send_func(None, embed)

    def get_help(self):
        return ("Show all cocktails\n" +
                "Usage: `" + self.prefix + self.get_name() + "`")

    def get_name(self):
        return 'menu'
