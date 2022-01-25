from matplotlib import pyplot as plt

from GameTracker import GameTracker
from DataRetriever import DataRetriever

data_2042, title_2042 = DataRetriever("https://steamcharts.com/app/1517290").get_data()
data_bf5, title_bf5 = DataRetriever("https://steamcharts.com/app/1238810").get_data()
data_bf1, title_bf1 = DataRetriever("https://steamcharts.com/app/1238840").get_data()
data_bf4, title_bf4 = DataRetriever("https://steamcharts.com/app/1238860").get_data()
data_insurgency_sandstorm, title_insurgency_sandstorm = DataRetriever("https://steamcharts.com/app/581320").get_data()
data_hll, title_hll = DataRetriever("https://steamcharts.com/app/686810").get_data()
data_ww3, title_ww3 = DataRetriever("https://steamcharts.com/app/674020").get_data()

# FORMAT FOR ADDING NEW STEAM DATA

data_csgo, title_csgo = DataRetriever("https://steamcharts.com/app/730").get_data()
data_bo2, title_bo2 = DataRetriever("https://steamcharts.com/app/202990").get_data()
data_apex_legends, title_apex_legends = DataRetriever("https://steamcharts.com/app/1172470").get_data()

game_data = [  # put the game with the oldest steam data at the bottom
    data_2042,
    data_bf5,
    data_bf1,
    data_bf4,
    # data_insurgency_sandstorm,
    # data_hll,
    # data_ww3,
    # data_bo2,
    # data_apex_legends,
    # data_csgo,
]

game_titles = [  # put the game title in the same order as the list above
    title_2042,
    title_bf5,
    title_bf1,
    title_bf4,
    # title_insurgency_sandstorm,
    # title_hll,
    # title_ww3,
    # title_bo2,
    # title_apex_legends,
    # title_csgo,
]

steam_data = GameTracker(game_data, game_titles)

steam_data.plot_monthly_average_player_counts()
steam_data.plot_monthly_peak_players()
steam_data.plot_monthly_gain()
steam_data.plot_trends()

plt.legend()
plt.show()
