import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider


class GameTracker:
    def __init__(self, data, titles):
        self.data = data
        self.titles = titles
        self.largest_game_data = max(len(x) for x in self.data)
        self.fig, self.axs = plt.subplots(2, 2)
        self.fig.tight_layout(pad=6.0)
        self.setup_graph()
        self.axis_position_1 = plt.axes([0.18, 0.95, 0.65, 0.03], facecolor="white")
        self.slider_position_1 = Slider(self.axis_position_1, "Position", 0, self.largest_game_data)
        self.slider_position_1.valtext.set_visible(False)

        self.axis_position_2 = plt.axes([0.18, 0.91, 0.65, 0.03], facecolor="white")
        self.slider_position_2 = Slider(self.axis_position_2, "Zoom", 0, self.largest_game_data)
        self.slider_position_2.valtext.set_visible(False)

        self.avg_players = []
        self.peak_players = []
        self.gain_players = []
        for item in self.data:
            for game in item:
                if game[1] != "NaN" and game[1] != "-":
                    self.avg_players.append(float(game[1]))
                if game[4] != "NaN" and game[1] != "-":
                    self.peak_players.append(float(game[4]))
                if game[2] != "NaN" and game[2] != "-":
                    self.gain_players.append(float(game[2]))

        self.slider_position_1.on_changed(self.update)
        self.slider_position_2.on_changed(self.update)

    def setup_graph(self):
        bf_title_index = -1
        try:
            bf_title_index = self.titles.index("Battlefield™ V")
        except ValueError:
            print("title not found")
            try:
                bf_title_index = self.titles.index("Battlefield 1 ™")
            except ValueError:
                print("title not found")
                try:
                    bf_title_index = self.titles.index("Battlefield 4™")
                except ValueError:
                    print("title not found")
        if bf_title_index != -1:
            first_battlefield_steam_data_index = self.largest_game_data - len(self.data[bf_title_index])
            self.axs[0, 0].axvline(x=first_battlefield_steam_data_index, color="k", linestyle=":", label="Earliest "
                                                                                                         "Battlefield "
                                                                                                         "Steam Data")
            self.axs[0, 1].axvline(x=first_battlefield_steam_data_index, color="k", linestyle=":", label="Earliest "
                                                                                                         "Battlefield "
                                                                                                         "Steam Data")
            self.axs[1, 0].axvline(x=first_battlefield_steam_data_index, color="k", linestyle=":", label="Earliest "
                                                                                                         "Battlefield "
                                                                                                         "Steam Data")
        bf_2042_title_index = -1
        try:
            bf_2042_title_index = self.titles.index("Battlefield™ 2042")
        except ValueError:
            print("Battlefield™ 2042 title not found")
        if bf_2042_title_index != -1:
            bf2042_title_index = self.titles.index("Battlefield™ 2042")
            first_battlefield2042_steam_data_index = self.largest_game_data - len(self.data[bf2042_title_index])
            self.axs[0, 0].axvline(x=first_battlefield2042_steam_data_index, color="#40dfbd", linestyle=":",
                                   label="Battlefield 2042 Release")
            self.axs[0, 1].axvline(x=first_battlefield2042_steam_data_index, color="#40dfbd", linestyle=":",
                                   label="Battlefield 2042 Release")
            self.axs[1, 0].axvline(x=first_battlefield2042_steam_data_index, color="#40dfbd", linestyle=":",
                                   label="Battlefield 2042 Release")
        self.axs[0, 0].axhline(y=0, color="0.85", linestyle="-")
        self.axs[0, 1].axhline(y=0, color="0.85", linestyle="-")
        self.axs[1, 0].axhline(y=0, color="0.85", linestyle="-")
        for game in self.data:
            for i in range(self.largest_game_data - len(game)):
                game.append(["N/A", "NaN", "NaN", "NaN", "NaN"])
        for game in self.data:
            game.reverse()

    def plot_monthly_average_player_counts(self):
        count = 0
        for game in self.data:
            average_player_count = []
            month_name = []
            month = []
            i = 0
            for item in game:
                average_player_count.append(float(item[1]))
                month_name.append(item[0])
                month.append(i)
                i += 1
            game = {
                "Month": month,
                "Avg. Player Count": average_player_count
            }
            df = pd.DataFrame(game, columns=["Month", "Avg. Player Count"])
            self.axs[0, 0].set_xticks(df["Month"], month_name, rotation=80, fontsize=6)
            self.axs[0, 0].tick_params(axis="y", labelsize=5)
            self.axs[0, 0].set_ylabel("Players", fontsize=9)
            self.axs[0, 0].set_title("Avg. Player Count", fontsize=9)
            self.axs[0, 0].plot(df["Month"], df["Avg. Player Count"], label=self.titles[count])
            count += 1
        # self.slider_position_1.on_changed(self.update)

    def plot_monthly_peak_players(self):
        count = 0
        for game in self.data:
            peak_player_count = []
            month_name = []
            month = []
            i = 0
            for item in game:
                peak_player_count.append(float(item[4]))
                month_name.append(item[0])
                month.append(i)
                i += 1
            game = {
                "Month": month,
                "Peak Players": peak_player_count
            }
            df = pd.DataFrame(game, columns=["Month", "Peak Players"])
            self.axs[0, 1].set_xticks(df["Month"], month_name, rotation=80, fontsize=6)
            self.axs[0, 1].tick_params(axis="y", labelsize=5)
            self.axs[0, 1].set_ylabel("Players", fontsize=9)
            self.axs[0, 1].set_title("Peak Player Count", fontsize=9)
            self.axs[0, 1].plot(df["Month"], df["Peak Players"], label=self.titles[count])
            count += 1

    def plot_monthly_gain(self):
        count = 0
        for game in self.data:
            start_amount = 0
            for o in game:
                if o[1] != "NaN":
                    start_amount = float(o[1])
                    break
            player_gain = []
            month_name = []
            month = []
            i = 0
            for item in game:
                if item[2] == "-":
                    player_gain.append(start_amount)
                else:
                    player_gain.append(float(item[2]))
                month_name.append(item[0])
                month.append(i)
                i += 1
            game = {
                "Month": month,
                "Avg. Players Gained": player_gain
            }
            df = pd.DataFrame(game, columns=["Month", "Avg. Players Gained"])
            self.axs[1, 0].set_xticks(df["Month"], month_name, rotation=80, fontsize=6)
            self.axs[1, 0].tick_params(axis="y", labelsize=5)
            self.axs[1, 0].set_ylabel("Players", fontsize=9)
            self.axs[1, 0].set_title("Avg. Players Gained", fontsize=9)
            self.axs[1, 0].plot(df["Month"], df["Avg. Players Gained"], label=self.titles[count])
            count += 1

    def update(self, val):
        pos_1 = self.slider_position_1.val
        zoom_level = self.largest_game_data - self.slider_position_2.val + 1
        self.axs[0, 0].axis([pos_1, pos_1 + zoom_level, min(self.avg_players), max(self.avg_players)])
        self.axs[0, 1].axis([pos_1, pos_1 + zoom_level, min(self.peak_players), max(self.peak_players)])
        self.axs[1, 0].axis([pos_1, pos_1 + zoom_level, min(self.gain_players), max(self.avg_players)])
        self.fig.canvas.draw_idle()
