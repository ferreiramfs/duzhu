import random as rd
import pandas as pd
import time

def run_games(games, results):

        for game in games:

                rng = rd.random()

                if matchs_odds[game] > rng:

                        results[game[0]] += 1
                else:
                        results[game[1]] += 1
        
        return(results)

teams_list = ['Aurora', 'NaVi', 'Team Liquid', '3DMax', 'Astralis', 'Tyloo', 'Mibr', 'Passion UA'
              , 'M80', 'FlyQuest', 'B8ers', 'Fnatic', 'NiP', 'Paravision', 'Imperial', 'Faze']

matchs = []

#Filling the possible matchs
for i in range(len(teams_list)):
    for j in range(i + 1, len(teams_list)):
        matchs.append((teams_list[i], teams_list[j]))

#Filling the expected odds of each possible match
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

round2 = []

final = {
      'Teams': teams_list,
      '0-3': [0] * len(teams_list),
      '1-3': [0] * len(teams_list),
      '2-3': [0] * len(teams_list),
      '3-2': [0] * len(teams_list),
      '3-1': [0] * len(teams_list),
      '3-0': [0] * len(teams_list),
}

final_result = pd.DataFrame(final)

num_ite, iter = 100000, 1

inicio = time.time()

for times in range(num_ite):
        
        results = dict(zip(teams_list, [0]*len(teams_list)))

        if iter % (num_ite/20) == 0:
                print(f'{round((iter/num_ite) * 100, 2)}%')
                print(f'Tempo decorrido: {time.time() - inicio:.4f}s')
                inicio = time.time()

        results = run_games(round1, results)

        win_r1 = sorted([chave for chave, valor in results.items() if valor == 1], key=teams_list.index)
        los_r1 = sorted([chave for chave, valor in results.items() if valor == 0], key=teams_list.index)

        round2 = [(win_r1[i], win_r1[-i-1]) for i in range(len(win_r1) // 2 )] + [(los_r1[i], los_r1[-i-1]) for i in range(len(los_r1) // 2 )]

        results = run_games(round2, results)

        win_r2 = sorted([chave for chave, valor in results.items() if valor == 2], key=teams_list.index)
        tie_r2 = sorted([chave for chave, valor in results.items() if valor == 1], key=teams_list.index)
        los_r2 = sorted([chave for chave, valor in results.items() if valor == 0], key=teams_list.index)

        round3 = [(win_r2[i], win_r2[-i-1]) for i in range(len(win_r2) // 2 )] + [(tie_r2[i], tie_r2[-i-1]) for i in range(len(tie_r2) // 2 )] + [(los_r2[i], los_r2[-i-1]) for i in range(len(los_r2) // 2 )]

        results = run_games(round3, results)

        teams_3x0 = [chave for chave, valor in results.items() if valor == 3]
        teams_0x3 = [chave for chave, valor in results.items() if valor == 0]

        win_r3 = sorted([chave for chave, valor in results.items() if valor == 2], key=teams_list.index)
        los_r3 = sorted([chave for chave, valor in results.items() if valor == 1], key=teams_list.index)
        
        round4 = [(win_r3[i], win_r3[-i-1]) for i in range(len(win_r3) // 2 )] + [(los_r3[i], los_r3[-i-1]) for i in range(len(los_r3) // 2 )]

        results = run_games(round4, results)

        teams_3x1 = [item for item in [chave for chave, valor in results.items() if valor == 3] if item not in teams_3x0]
        teams_1x3 = [chave for chave, valor in results.items() if valor == 1]

        tie_r4 = sorted([chave for chave, valor in results.items() if valor == 2], key=teams_list.index)

        round5 = [(tie_r4[i], tie_r4[-i-1]) for i in range(len(tie_r4) // 2 )]

        results = run_games(round5, results)

        teams_3x2 = [item for item in [chave for chave, valor in results.items() if valor == 3] if item not in teams_3x0 + teams_3x1]
        teams_2x3 = [chave for chave, valor in results.items() if valor == 2]

        for team in results:
                if team in teams_3x0:
                        final_result.loc[final_result['Teams'] == team, '3-0'] += 1

                elif team in teams_3x1:
                        final_result.loc[final_result['Teams'] == team, '3-1'] += 1
                
                elif team in teams_3x2:
                        final_result.loc[final_result['Teams'] == team, '3-2'] += 1
                
                elif team in teams_2x3:
                        final_result.loc[final_result['Teams'] == team, '2-3'] += 1
                
                elif team in teams_1x3:
                        final_result.loc[final_result['Teams'] == team, '1-3'] += 1
        
                else:
                        final_result.loc[final_result['Teams'] == team, '0-3'] += 1

        iter += 1

final_result[['0-3', '1-3', '2-3', '3-2', '3-1', '3-0']] = final_result[['0-3', '1-3', '2-3', '3-2', '3-1', '3-0']] / num_ite

print('---------------------------------------------------')
print(final_result)
print('---------------------------------------------------')

top2_3x0 = final_result.nlargest(2, '3-0')
top3_3x1 = final_result.nlargest(3, '3-1')
top3_3x2 = final_result.nlargest(3, '3-2')
top2_0x3 = final_result.nlargest(2, '0-3')

print(top2_3x0[['Teams', '3-0']])
print('--------------------')

print(top3_3x1[['Teams', '3-1']])
print('--------------------')

print(top3_3x2[['Teams', '3-2']])
print('--------------------')

print(top2_0x3[['Teams', '0-3']])
print('--------------------')