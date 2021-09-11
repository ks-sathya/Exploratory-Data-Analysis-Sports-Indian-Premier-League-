'''Kaushik S
Data Science and Business Analytics Intern @ TSF
Task #5 : Exploratory Data Analysis : Sports (Indian Premier League)'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
desired_width=400
pd.set_option('display.width',desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',18)
data = pd.read_csv("matches.csv")
print((data.head()))
print("Above are the data extracted from the matches file\n\n\n")
pd.set_option('display.max_columns',21)
Data = pd.read_csv("deliveries.csv")
print(Data.head())
print("Above is the data extracted from the deliveries file\n\n\n")
season_data=data[['id','season','winner']]
complete_data=Data.merge(season_data,how='inner',left_on='match_id',right_on='id')
print(data.columns.values)
print("\n")
pd.set_option('display.max_columns',18)
data = data.drop(columns=["umpire3"],axis=1)
print(data.head())
print("\n")
wins_per_season = data.groupby("season")["winner"].value_counts()
print(wins_per_season)
print("\n")
plt.figure(figsize = (18,10))
sns.countplot('season',data=data,palette="winter")
plt.title("Number of Matches played in each IPL season",fontsize=20)
plt.xlabel("season",fontsize=15)
plt.ylabel('Matches',fontsize=15)
plt.show()
plt.figure(figsize = (18,10))
sns.countplot(x='winner',data=data, palette='cool')
plt.title("Numbers of matches won by team ",fontsize=20)
plt.xticks(rotation=50)
plt.xlabel("Teams",fontsize=15)
plt.ylabel("No of wins",fontsize=15)
plt.show()
data['win_by']=np.where(data['win_by_runs']>0,'Bat first','Bowl first')
Win=data.win_by.value_counts()
labels=np.array(Win.index)
sizes = Win.values
colors = ['#FFBF00','#FA8072']
plt.figure(figsize = (10,8))
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True,startangle=90)
plt.title('Match Result',fontsize=20)
plt.axis('equal')
plt.show()
plt.figure(figsize = (18,10))
sns.countplot('season',hue='win_by',data=data,palette='hsv')
plt.title("Numbers of matches won by batting and bowling first ",fontsize=20)
plt.xlabel("Season",fontsize=15)
plt.ylabel("Count",fontsize=15)
plt.show()
Toss=data.toss_decision.value_counts()
labels=np.array(Toss.index)
sizes = Toss.values
colors = ['#FFBF00', '#FA8072']
plt.figure(figsize = (10,8))
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True,startangle=90)
plt.title('Toss result',fontsize=20)
plt.axis('equal')
plt.show()
plt.figure(figsize = (18,10))
sns.countplot('season',hue='toss_decision',data=data,palette='afmhot')
plt.title("Numbers of matches won by Toss result ",fontsize=20)
plt.xlabel("Season",fontsize=15)
plt.ylabel("Count",fontsize=15)
plt.show()
# we will print winner season wise
final_matches=data.drop_duplicates(subset=['season'], keep='last')
final_matches[['season','winner']].reset_index(drop=True).sort_values('season')
# we will plot pie chart on Winning percentage in final
match = final_matches.win_by.value_counts()
labels=np.array(Toss.index)
sizes = match.values
colors = ['gold', 'purple']
plt.figure(figsize = (10,8))
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True,startangle=90)
plt.title('Match Result',fontsize=20)
plt.axis('equal')
plt.show()
Toss=final_matches.toss_decision.value_counts()
labels=np.array(Toss.index)
sizes = Toss.values
colors = ['#FFBF00', '#FA8072']
plt.figure(figsize = (10,8))
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True,startangle=90)
plt.title('Toss Result',fontsize=20)
plt.axis('equal')
plt.show()
# we will print name of top player in IPL
plt.figure(figsize = (18,10))
top_players = data.player_of_match.value_counts()[:10]
fig, ax = plt.subplots()
ax.set_ylim([0,20])
ax.set_ylabel("Count")
ax.set_title("Top player of the match Winners")
top_players.plot.bar()
sns.barplot(x = top_players.index, y = top_players, orient='v', palette="hsv");
plt.show()
# We will print IPL Finals venues and winners along with the number of wins.
print(final_matches.groupby(['city','winner']).size())
print("\n")
# we will print number of season won by teams
print(final_matches["winner"].value_counts())
print("\n")
print(final_matches[['toss_winner','toss_decision','winner']].reset_index(drop=True))
print("\n")
print(final_matches[['winner','player_of_match']].reset_index(drop=True))
print("\n")
print(len(final_matches[final_matches['toss_winner']==final_matches['winner']]['winner']))
print("\n")
four_data=complete_data[complete_data['batsman_runs']==4]
print(four_data.groupby('batting_team')['batsman_runs'].agg([('runs by fours','sum'),('fours','count')]))
print("\n")
# we will plot graph on four hit by players
batsman_four=four_data.groupby('batsman')['batsman_runs'].agg([('four','count')]).reset_index().sort_values('four',ascending=0)
ax=batsman_four.iloc[:10,:].plot('batsman','four',kind='bar',color='black')
plt.title("Numbers of fours hit by playes ",fontsize=20)
plt.xticks(rotation=50)
plt.xlabel("Player name",fontsize=15)
plt.ylabel("No of fours",fontsize=15)
plt.show()
# we will plot graph on no of four hit in each season
ax=four_data.groupby('season')['batsman_runs'].agg([('four','count')]).reset_index().plot('season','four',kind='bar',color = 'red')
plt.title("Numbers of fours hit in each season ",fontsize=20)
plt.xticks(rotation=50)
plt.xlabel("season",fontsize=15)
plt.ylabel("No of fours",fontsize=15)
plt.show()
# we will print no of sixes hit by team
six_data=complete_data[complete_data['batsman_runs']==6]
print(six_data.groupby('batting_team')['batsman_runs'].agg([('runs by six','sum'),('sixes','count')]))
print("\n")
# we will plot graph of six hit by players
batsman_six=six_data.groupby('batsman')['batsman_runs'].agg([('six','count')]).reset_index().sort_values('six',ascending=0)
ax=batsman_six.iloc[:10,:].plot('batsman','six',kind='bar',color='green')
plt.title("Numbers of six hit by playes ",fontsize=20)
plt.xticks(rotation=50)
plt.xlabel("Player name",fontsize=15)
plt.ylabel("No of six",fontsize=15)
plt.show()
# we will plot graph on no of six hit in each season
ax=six_data.groupby('season')['batsman_runs'].agg([('six','count')]).reset_index().plot('season','six',kind='bar',color = 'blue')
plt.title("Numbers of fours hit in each season ",fontsize=20)
plt.xticks(rotation=50)
plt.xlabel("season",fontsize=15)
plt.ylabel("No of fours",fontsize=15)
plt.show()
# We will print the top 10 leading run scorer in IPL
batsman_score=Data.groupby('batsman')['batsman_runs'].agg(['sum']).reset_index().sort_values('sum',ascending=False).reset_index(drop=True)
batsman_score=batsman_score.rename(columns={'sum':'batsman_runs'})
print("*** Top 10 Leading Run Scorer in IPL ***")
print(batsman_score.iloc[:10,:])
print("\n")
# we will print no of matches played by batsman
No_Matches_player= Data[["match_id","player_dismissed"]]
No_Matches_player =No_Matches_player .groupby("player_dismissed")["match_id"].count().reset_index().sort_values(by="match_id",ascending=False).reset_index(drop=True)
No_Matches_player.columns=["batsman","No_of Matches"]
print(No_Matches_player .head(5))
print("\n")
# Dismissals in IPL
plt.figure(figsize=(18,10))
ax=sns.countplot(Data.dismissal_kind)
plt.title("Dismissals in IPL",fontsize=20)
plt.xlabel("Dismissals kind",fontsize=15)
plt.ylabel("count",fontsize=15)
plt.xticks(rotation=90)
plt.show()
wicket_data=Data.dropna(subset=['dismissal_kind'])
wicket_data=wicket_data[~wicket_data['dismissal_kind'].isin(['run out','retired hurt','obstructing the field'])]
# we will print ipl most wicket taking bowlers
print(wicket_data.groupby('bowler')['dismissal_kind'].agg(['count']).reset_index().sort_values('count',ascending=False).reset_index(drop=True).iloc[:10,:])
print(
'''\nThe highest number of match played in IPL season was 2013,2014,2015.
\nThe highest number of match won by Mumbai Indians i.e 4 match out of 12 matches.
\nTeams which Bowl first has higher chances of winning then the team which bat first.
\nAfter winning toss more teams decide to do fielding first.
\nIn finals teams which decide to do fielding first win the matches more then the team which bat first.
\nIn finals most teams after winning toss decide to do fielding first.
\nTop player of match winning are CH gayle, AB de villers.
\nIt is interesting that out of 12 IPL finals,9 times the team that won the toss was also the winner of IPL.\n
The highest number of four hit by player is Shikar Dhawan.
\nThe highest number of six hit by player is CH gayle.
\nTop leading run scorer in IPL are Virat kholi, SK Raina, RG Sharma.\n
The highest number of matches played by player name are SK Raina, RG Sharma.\n
Dismissals in IPL was most by Catch out.
\nThe IPL most wicket taken blower is SL Malinga.''')

