from matplotlib import pyplot as plt

from GameTracker import GameTracker
from DataRetriever.DataRetriever import SteamDataRetriever

data_2042, title_2042 = SteamDataRetriever("https://steamcharts.com/app/1517290").get_data()
data_bf5, title_bf5 = SteamDataRetriever("https://steamcharts.com/app/1238810").get_data()
data_bf1, title_bf1 = SteamDataRetriever("https://steamcharts.com/app/1238840").get_data()
data_bf4, title_bf4 = SteamDataRetriever("https://steamcharts.com/app/1238860").get_data()
data_iss, title_iss = SteamDataRetriever("https://steamcharts.com/app/581320").get_data()
data_hll, title_hll = SteamDataRetriever("https://steamcharts.com/app/686810").get_data()
data_ww3, title_ww3 = SteamDataRetriever("https://steamcharts.com/app/674020").get_data()

# FORMAT FOR ADDING NEW STEAM DATA
data_csgo, title_csgo = SteamDataRetriever("https://steamcharts.com/app/730").get_data()
data_bo2, title_bo2 = SteamDataRetriever("https://steamcharts.com/app/202990").get_data()

game_data = [  # put the game with the oldest steam data at the bottom
    data_2042,
    data_bf5,
    data_bf1,
    data_bf4,
    # data_iss,
    data_hll,
    # data_ww3,
    # data_bo2,
    # data_csgo,
]

game_titles = [  # put the game title in the same order as the list above
    title_2042,
    title_bf5,
    title_bf1,
    title_bf4,
    # title_iss,
    title_hll,
    # title_ww3,
    # title_bo2,
    # title_csgo,
]

steam_data = GameTracker(game_data, game_titles)

# steam_data.plot_monthly_average_player_counts()
# steam_data.plot_monthly_peak_players()
# steam_data.plot_monthly_gain()
# steam_data.plot_trends()

plt.show()
