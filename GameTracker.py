import pandas as pd
from matplotlib import pyplot as plt


class GameTracker:
    def __init__(self, data, titles):
        self.data = data
        self.titles = titles

    def plot_monthly_average_player_counts(self):
        plt.axvline(x=0, color="k", linestyle="-", label="Earliest Battlefield Steam data")
        plt.axvline(x=len(max(self.data)) - len(min(self.data)), color="k", linestyle=":", label="Battlefield 2042 "
                                                                                                 "release month")

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
            plt.xlabel("30 day period", labelpad=10)
            plt.ylabel("Avg. player count", labelpad=20)
            plt.title("Steam Battlefield Data", pad=20)
            plt.plot(df["Month"], df["Avg. Player Count"], label=self.titles[count])
            plt.tight_layout()
            count += 1

        plt.legend()
        plt.show()
