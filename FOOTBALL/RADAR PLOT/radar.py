import pandas as pd
import matplotlib.pyplot as plt
from soccerplots.radar_chart import Radar 


def radarChart(player1,player2):
    #Read in the data
    df = pd.read_csv('/home/ayodeji/Downloads/Compressed/Football-Analytics-master/player_data.csv')
    #Sorting players names
    df['Player'] = df['Player'].str.split('\\', expand=True)[0]
    #Selecting data for the players being compared
    df = df[(df['Player']== player1) | (df['Player']== player2)].reset_index()
    #Creating a squad data frame
    df_squad = df.drop(['Rk', 'Nation', 'Pos', 'Age', 'Born', '90s', 'Gls',
       'Sh', 'SoT', 'SoT%', 'Sh/90', 'SoT/90', 'G/Sh', 'G/SoT', 'Dist', 'FK',
       'PK', 'PKatt', 'xG', 'npxG', 'npxG/Sh', 'G-xG', 'np:G-xG', 'Matches'], axis = 1)
    df_squad.reset_index()
    #Creating squad variable(s) 
    squad1 = df_squad['Squad'][0]
    squad2 = df_squad['Squad'][1]
    #dropping columns
    df = df.drop(['index','Rk', 'Nation','Pos','Age', 'Squad', 'Born','90s','PK', 'FK', 'PKatt', 'Matches'], axis=1)
    #get parameters
    params = list(df.columns)
    
    params = params[1:]
    params
    # add ranges to list of tuple pairs
    ranges = []
    a_values = []
    b_values = []

    for x in params:
        a = min(df[params][x])
        a = a - (a * 0.25)
        b = max(df[params][x])
        b = b + (b * 0.25)

        ranges.append((a,b))

    for x in range(len(df['Player'])):
        if df['Player'][x] == player1:
            a_values = df.iloc[x].values.tolist()
        if df['Player'][x] == player2:
            b_values = df.iloc[x].values.tolist()
            

    a_values = a_values[1:]
    b_values = b_values[1:]

    values  = [a_values, b_values]
   #title [Labels]
    title = dict(
        title_name = player1,
        title_color = 'red',
        subtitle_name = squad1,
        subtitle_color = 'red',
        title_name_2 = player2,
        title_color_2 = 'blue',
        subtitle_name_2 = squad2,
        subtitle_color_2 = 'blue',
        title_fontsize = 18,
        subtitle_fontsize = 15
    )

    endnote = 'Deji Yekeen \ndata via FBREF /   Statsbomb'
    #Plot radar
    radar = Radar()

    fig, ax = radar.plot_radar(ranges=ranges, params=params,values=values,
                                radar_color=['red','blue'],
                                alphas=[.75, .6],
                                title=title,
                                endnote=endnote,
                                compare=True)
#player 1, player2 could be any premier league player
radarChart(player1='Harry Kane',player2='Mohamed Salah')
