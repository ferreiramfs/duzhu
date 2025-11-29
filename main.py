import random as rd
import pandas as pd

teams_list = ['Aurora', 'NaVi', 'Team Liquid', '3DMax', 'Astralis', 'Tyloo', 'Mibr', 'Passion UA'
              , 'M80', 'FlyQuest', 'B8ers', 'Fnatic', 'NiP', 'Paravision', 'Imperial', 'Faze']

matchs = []

for i in range(len(teams_list)):
    for j in range(i + 1, len(teams_list)):
        matchs.append((teams_list[i], teams_list[j]))

odds = [0.55, 0.65, 0.55, 0.65, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.65 #Aurora x
        , 0.6, 0.5, 0.55, 0.65, 0.7, 0.7, 0.65, 0.65, 0.7, 0.7, 0.7, 0.65, 0.7, 0.6    #NaVi
        , 0.4, 0.5, 0.6, 0.7, 0.7, 0.65, 0.7, 0.7, 0.7, 0.7, 0.65, 0.7, 0.6            #Team Liquid
        , 0.55, 0.7, 0.7, 0.7, 0.65, 0.7, 0.7, 0.7, 0.7, 0.65, 0.7, 0.65               #3DMax
        , 0.7, 0.7, 0.7, 0.65, 0.65, 0.65, 0.7, 0.7, 0.6, 0.7, 0.6                     #Astralis
        , 0.45, 0.5, 0.45, 0.5, 0.5, 0.55, 0.5, 0.4, 0.5, 0.35                         #Tyloo
        , 0.55, 0.45, 0.55, 0.5, 0.55, 0.55, 0.35, 0.5, 0.35                           #Mibr
        , 0.45, 0.5, 0.5, 0.5, 0.5, 0.35, 0.5, 0.35                                    #Passion UA
        , 0.55, 0.55, 0.55, 0.55, 0.45, 0.55, 0.4                                      #M80
        , 0.5, 0.5, 0.5, 0.4, 0.5, 0.35                                                #FlyQuest
        , 0.5, 0.5, 0.4, 0.5, 0.35                                                     #B8ers
        , 0.5, 0.4, 0.5, 0.35                                                          #Fnatic
        , 0.4, 0.5, 0.35                                                               #NiP
        , 0.6, 0.55                                                                    #Paravision
        , 0.35]                                                                        #Imperial    

matchs_odds = dict(zip(matchs, odds))

round1 = [('Aurora', 'M80'), ('NaVi', 'FlyQuest'), ('Team Liquid', 'B8ers'), ('3DMax', 'Fnatic')
        , ('Astralis', 'NiP'), ('Tyloo', 'Paravision'), ('Mibr', 'Imperial'), ('Passion UA', 'Faze')]


final = {
      'Teams': teams_list,
      '0-3': [0] * len(teams_list),
      #'1-3': [0] * len(teams_list),
      #'2-3': [0] * len(teams_list),
      #'3-2': [0] * len(teams_list),
      #'3-1': [0] * len(teams_list),
      '3-0': [0] * len(teams_list),
}

final_result = pd.DataFrame(final)

num_ite = 10000

for times in range(num_ite):
      
        results = dict(zip(teams_list, '0'*len(teams_list)))

        for game in round1:

                rng = rd.random()

                if matchs_odds[game] > rng:
                        final_result.loc[final_result['Teams'] == game[0], '3-0'] += 1
                        final_result.loc[final_result['Teams'] == game[1], '0-3'] += 1
                else:
                        final_result.loc[final_result['Teams'] == game[1], '3-0'] += 1
                        final_result.loc[final_result['Teams'] == game[0], '0-3'] += 1

print(final_result)