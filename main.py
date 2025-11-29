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

print(matchs_odds)