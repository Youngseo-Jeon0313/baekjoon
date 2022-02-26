name=input()
L,O,V,E=0,0,0,0
for i in name:
    if i=='L':
        L+=1
    elif i=='O':
        O+=1
    elif i=='V':
        V+=1
    elif i=='E':
        E+=1
team=int(input())
MAX=0
second_teams=[]
for i in range(team):
    cal_L=L; cal_O=O; cal_V=V; cal_E=E;
    TeamName=input()
    for j in TeamName:
        if j=='L': cal_L+=1
        elif j=='O': cal_O+=1
        elif j=='V': cal_V+=1
        elif j=='E': cal_E+=1
    score=((cal_L+cal_O)*(cal_L+cal_V)*(cal_L+cal_E)*(cal_O+cal_V)*(cal_O+cal_E)*(cal_V+cal_E))%100
    if score>MAX:second_teams=[TeamName]; MAX=score
    elif score==MAX: second_teams.append(TeamName)

second_teams.sort()
print(second_teams[0])
    
    
