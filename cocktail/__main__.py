import os

import yaml

if __name__ == '__main__':

    if os.stat("config.yaml").st_size != 0:
        with open('config.yaml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            prefix = data['prefix']
            discord_white_list = data['discord_white_list']
            telegramm_bot_white_list = data['telegramm_white_list']
            tg_token = '1715292978:AAFkL03sQvvDDiepDOs8sGrUR1o34WgS46c'
            dis_token = 'ODYzNzQ1OTcxOTYzMDM1NjY4.YOrYHw.Vde49GWYiiuv6uIUH8QYchL2Rpg'
    else:
        raise Exception("File is empty")
    # db_manager = DbConnectionManager()
    # url_repo = db_manager.get_url_repository()
    dis_bot = DiscordBot(prefix, db_manager.get_url_repository())

