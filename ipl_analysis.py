import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset

df = pd.read_csv("deliveries.csv")

print(df.head())

sns.set_style("whitegrid")

# -------------------------
# Top 10 Run Scorers
# -------------------------

top_scorers = df.groupby(
    "batter"
)["batsman_runs"].sum()

top_scorers = top_scorers.sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(12,6))

sns.barplot(
    x=top_scorers.index,
    y=top_scorers.values
)

plt.title("Top 10 IPL Run Scorers")

plt.xlabel("Player")

plt.ylabel("Runs")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# -------------------------
# Most Sixes
# -------------------------

most_sixes = df[
    df["batsman_runs"] == 6
]

most_sixes = most_sixes["batter"].value_counts().head(10)

plt.figure(figsize=(12,6))

sns.barplot(
    x=most_sixes.index,
    y=most_sixes.values
)

plt.title("Top 10 Players with Most Sixes")

plt.xlabel("Player")

plt.ylabel("Sixes")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# -------------------------
# Most Fours
# -------------------------

most_fours = df[
    df["batsman_runs"] == 4
]

most_fours = most_fours["batter"].value_counts().head(10)

plt.figure(figsize=(12,6))

sns.barplot(
    x=most_fours.index,
    y=most_fours.values
)

plt.title("Top 10 Players with Most Fours")

plt.xlabel("Player")

plt.ylabel("Fours")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# -------------------------
# Highest Scoring Teams
# -------------------------

top_teams = df.groupby(
    "batting_team"
)["total_runs"].sum()

top_teams = top_teams.sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(12,6))

sns.barplot(
    x=top_teams.index,
    y=top_teams.values
)

plt.title("Highest Scoring IPL Teams")

plt.xlabel("Team")

plt.ylabel("Runs")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# -------------------------
# Insights
# -------------------------

print("\nHighest Run Scorer")

print(top_scorers.idxmax())

print("\nMost Sixes")

print(most_sixes.idxmax())

print("\nMost Fours")

print(most_fours.idxmax())

print("\nHighest Scoring Team")

print(top_teams.idxmax())