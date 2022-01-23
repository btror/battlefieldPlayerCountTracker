import pandas as pd
from matplotlib import pyplot as plt


class GameTracker:
    def __init__(self, data, titles):
        self.data = data
        self.titles = titles

    def plot_monthly_average_player_counts(self):
        plt.axhline(y=0, color="0.85", linestyle="-")
        plt.axvline(x=0, color="k", linestyle=":", label="Earliest Battlefield Steam Data")
        plt.axvline(x=len(max(self.data)) - len(min(self.data)), color="#40dfbd", linestyle=":",
                    label="Battlefield 2042 "
                          "Release")

        for i in range(len(max(self.data)) - len(min(self.data))):
            min(self.data).append(["N/A", "NaN", "NaN", "NaN", "NaN"])

        for game in self.data:
            game.reverse()

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
            plt.xticks(df["Month"], month_name, rotation=80, fontsize=6)
            plt.subplots_adjust(bottom=0.3)
            plt.xlabel("30 Day Period", labelpad=10)
            plt.ylabel("Avg. Player Count", labelpad=20)
            plt.title("Steam Battlefield Data", pad=20)
            plt.plot(df["Month"], df["Avg. Player Count"], label=self.titles[count])
            plt.tight_layout()
            count += 1

        plt.legend()
        plt.show()

    def plot_monthly_peak_players(self):
        plt.axhline(y=0, color="0.85", linestyle="-")
        plt.axvline(x=0, color="k", linestyle=":", label="Earliest Battlefield Steam Data")
        plt.axvline(x=len(max(self.data)) - len(min(self.data)), color="#40dfbd", linestyle=":", label="Battlefield "
                                                                                                       "2042 "
                                                                                                       "Release")

        for i in range(len(max(self.data)) - len(min(self.data))):
            min(self.data).append(["N/A", "NaN", "NaN", "NaN", "NaN"])

        for game in self.data:
            game.reverse()

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
            plt.xticks(df["Month"], month_name, rotation=80, fontsize=6)
            plt.subplots_adjust(bottom=0.3)
            plt.xlabel("30 Day Period", labelpad=10)
            plt.ylabel("Peak Players", labelpad=20)
            plt.title("Steam Battlefield Data", pad=20)
            plt.plot(df["Month"], df["Peak Players"], label=self.titles[count])
            plt.tight_layout()
            count += 1

        plt.legend()
        plt.show()

    def plot_monthly_gain(self):
        plt.axhline(y=0, color="0.85", linestyle="-")
        plt.axvline(x=0, color="k", linestyle=":", label="Earliest Battlefield Steam Data")
        plt.axvline(x=len(max(self.data)) - len(min(self.data)), color="#40dfbd", linestyle=":",
                    label="Battlefield 2042 "
                          "Release")

        for i in range(len(max(self.data)) - len(min(self.data))):
            min(self.data).append(["N/A", "NaN", "NaN", "NaN", "NaN"])

        for game in self.data:
            game.reverse()

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
            plt.xticks(df["Month"], month_name, rotation=80, fontsize=6)
            plt.subplots_adjust(bottom=0.3)
            plt.xlabel("30 Day Period", labelpad=10)
            plt.ylabel("Avg. Players Gained", labelpad=20)
            plt.title("Steam Battlefield Data", pad=20)
            plt.plot(df["Month"], df["Avg. Players Gained"], label=self.titles[count])
            plt.tight_layout()
            count += 1

        plt.legend()
        plt.show()
