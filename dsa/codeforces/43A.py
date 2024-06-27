n = int(input())
scores = {}
for i in range(n):
    s = input()
    if s not in scores:
        scores[s] = 1
    else:
        scores[s] += 1

win_team, win_score = next(iter(scores.items()))


for team, score in scores.items():
    if score > win_score:
        win_score = score
        win_team = team

print(win_team)
