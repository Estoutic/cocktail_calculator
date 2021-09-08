import os

import yaml

from discord_bot.DiscordBot import DiscordBot
from service.DbManager import DbConnectionManager

if __name__ == '__main__':

    if os.stat("config.yaml").st_size != 0:
        with open('config.yaml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            prefix = data['prefix']
            token = data['token']
    else:
        raise Exception("File is empty")
    # db_manager = DbConnectionManager()
    # url_repo = db_manager.get_url_repository()
    dis_bot = DiscordBot(prefix)

    dis_bot.run(token)