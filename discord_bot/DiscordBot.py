import asyncio

import discord as discord

from cocktails.Hirosima import Hirosima
from command.Menu import Menu
from command.base.Command import Command
from command.base.stock import Stock


class DiscordBot(discord.Client):
    def __init__(self, prefix: str):
        super().__init__()
        self.commands = {}
        self.prefix = prefix
        self.menu = {}
        self.register_command(Menu(self.menu, self.prefix))
        self.add_to_menu(Hirosima())

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

        text = message.content
        self.guild = message.guild
        if not text.startswith(self.prefix):
            return
        text = text[len(self.prefix):]
        splited_args = text.split()
        cmd = text.split()[0]

        if cmd not in self.commands:
            return
        if len(splited_args) > 1:
            args = splited_args[1:]
        else:
            args = []
        loop = asyncio.get_event_loop()

        def test(msg, embed=None):
            loop.create_task(message.channel.send(msg, embed=embed))

        if self.commands[cmd].execute is not None:
            self.commands[cmd].execute(test, args)

    def get_tuple(self):
        return self.commands

    def register_command(self, command: Command):
        self.commands[command.get_name()] = command

    def add_to_menu(self, stock: Stock):
        self.menu[stock.get_name()] = stock
