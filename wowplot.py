import matplotlib.pyplot as plt
# paste the output of the js web console funciton into the "data" lists for each server
data1 = [
    
]

data2 = [
    
]

data3 = [
    
]

ship_stats = {}
for d in data1 + data2 + data3:
    s = d["ship"]
    if s not in ship_stats:
        ship_stats[s] = {"b": 0, "w": 0.0}
    ship_stats[s]["b"] += d["battles"]
    ship_stats[s]["w"] += d["winRate"] * d["battles"]

data = [{"ship": s, "battles": v["b"], "winRate": v["w"] / v["b"]} for s, v in ship_stats.items()]

ships = [i["ship"] for i in data]
battles = [i["battles"] for i in data]
win_rates = [i["winRate"] for i in data]

plt.figure(figsize=(10, 6))
plt.scatter(battles, win_rates, c=win_rates, cmap='viridis', s=100, edgecolor='k', alpha=0.9)
plt.xlabel("Battles")
plt.ylabel("Win Rate (%)")
plt.grid(True)

for i, ship in enumerate(ships):
    plt.annotate(ship, (battles[i], win_rates[i]), fontsize=9, alpha=0.7)

plt.show()
