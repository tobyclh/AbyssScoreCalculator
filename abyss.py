import streamlit as st
with open('data.txt') as f:
    lines = f.readlines()
rates = {}
names = []
for i in range(len(lines)//2):
    name, rate = lines[i*2].rstrip(), lines[i*2+1].rstrip()
    rate = rate.replace('%', '')
    names.append(name)
    rates[name] = float(rate)

five_star_char = ['Kazuha', 'Kokomi', 'Ayaka', 'Venti', 'Ayato', 'Ganyu', 'Shenhe', 'Shougun', 'Bennett', 'Zhongli', 'Mona', 'Yae', 'Tartaglia', 'Hutao', 'Jean', 'Eula', 'Xiao', 'Albedo', 'Itto', 'Yoimiya', 'Klee', 'Qiqi', 'Keqing', 'Diluc']
# rates['X'] = 0
# print(rates)
cons_factor = 1.2
total_cost = 0
st.markdown('## Team 1')
cols = st.columns(4)
team_1_cost = 0
for i, col in enumerate(cols):
    name = col.selectbox(f'Team 1 Character {i+1}', names)
    cons = col.number_input(f'Team 1 Constellation {i+1}', 0, 6, 0)
    five_star_weapon = int(col.checkbox(f'Team 1 5* Weapon {i+1}')) * 0.5 + 1
    cost = rates[name] * five_star_weapon
    if name in five_star_char:
        cost *= (cons_factor**cons)
    col.write(f'Cost: {cost}')
    total_cost += cost
    team_1_cost += cost
st.markdown(f'### Team 1 cost: {team_1_cost}')

st.markdown('## Team 2')
cols = st.columns(4)
team_2_cost = 0
for i, col in enumerate(cols):
    name = col.selectbox(f'Team 2 Character {i+1}', names)
    cons = col.number_input(f'Team 2 Constellation {i+1}', 0, 6, 0)
    five_star_weapon = int(col.checkbox(f'Team 2 5* Weapon {i+1}')) * 0.5 + 1
    cost = rates[name] * five_star_weapon
    if name in five_star_char:
        cost *= (cons_factor**cons)
    col.write(f'Cost: {cost}')
    total_cost += cost
    team_2_cost += cost
st.markdown(f'### Team 2 cost: {team_2_cost}')
st.markdown(f'## Total cost: {total_cost}')