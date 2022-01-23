from GameTracker import GameTracker
from DataRetriever import DataRetriever

data_2042 = DataRetriever("https://steamcharts.com/app/1517290").get_data()
data_bf5 = DataRetriever("https://steamcharts.com/app/1238810").get_data()
data_bf1 = DataRetriever("https://steamcharts.com/app/1238840").get_data()
data_bf4 = DataRetriever("https://steamcharts.com/app/1238860").get_data()

game_data = [data_2042, data_bf5, data_bf1, data_bf4]
game_titles = ["Battlefield 2042", "Battlefield V", "Battlefield 1", "Battlefield 4"]

steam_data = GameTracker(game_data, game_titles)
steam_data.plot_monthly_average_player_counts()
