import matplotlib.pyplot as plt

data1 = [
    {
        "ship": "Småland",
        "battles": 3925,
        "winRate": 64.4
    },
    {
        "ship": "Vampire II",
        "battles": 1855,
        "winRate": 63.3
    },
    {
        "ship": "La Pampa",
        "battles": 953,
        "winRate": 63.1
    },
    {
        "ship": "Druid",
        "battles": 1209,
        "winRate": 62.5
    },
    {
        "ship": "Cassard",
        "battles": 2945,
        "winRate": 62.3
    },
    {
        "ship": "Hull",
        "battles": 3357,
        "winRate": 62.1
    },
    {
        "ship": "Daring",
        "battles": 6375,
        "winRate": 61.8
    },
    {
        "ship": "Lüshun",
        "battles": 2129,
        "winRate": 61.2
    },
    {
        "ship": "Khabarovsk",
        "battles": 1709,
        "winRate": 60.8
    },
    {
        "ship": "Z-42",
        "battles": 2327,
        "winRate": 60.7
    },
    {
        "ship": "Yueyang",
        "battles": 3341,
        "winRate": 60.4
    },
    {
        "ship": "Ragnar",
        "battles": 1504,
        "winRate": 59.8
    },
    {
        "ship": "Hayate",
        "battles": 1687,
        "winRate": 59.8
    },
    {
        "ship": "Marceau",
        "battles": 3292,
        "winRate": 59.7
    },
    {
        "ship": "Gdańsk",
        "battles": 3112,
        "winRate": 59.6
    },
    {
        "ship": "Georg Hoffmann",
        "battles": 3711,
        "winRate": 59.6
    },
    {
        "ship": "Shimakaze",
        "battles": 11939,
        "winRate": 59.3
    },
    {
        "ship": "Álvaro de Bazán",
        "battles": 2024,
        "winRate": 59.2
    },
    {
        "ship": "Somers",
        "battles": 1710,
        "winRate": 59.2
    },
    {
        "ship": "Tromp",
        "battles": 9882,
        "winRate": 59
    },
    {
        "ship": "Delny",
        "battles": 643,
        "winRate": 58.9
    },
    {
        "ship": "Grozovoi",
        "battles": 1328,
        "winRate": 58.7
    },
    {
        "ship": "Gearing",
        "battles": 4081,
        "winRate": 58.6
    },
    {
        "ship": "Kléber",
        "battles": 2242,
        "winRate": 58.5
    },
    {
        "ship": "Z-52",
        "battles": 2556,
        "winRate": 58.1
    },
    {
        "ship": "Halland",
        "battles": 6735,
        "winRate": 58
    },
    {
        "ship": "Attilio Regolo",
        "battles": 1916,
        "winRate": 57.4
    },
    {
        "ship": "Elbing",
        "battles": 2258,
        "winRate": 57
    },
    {
        "ship": "Forrest Sherman",
        "battles": 3002,
        "winRate": 56.4
    },
    {
        "ship": "Harugumo",
        "battles": 1742,
        "winRate": 54.2
    }
]

data2 = [
    {
        "ship": "Småland",
        "battles": 2366,
        "winRate": 63.7
    },
    {
        "ship": "Z-42",
        "battles": 1630,
        "winRate": 62.7
    },
    {
        "ship": "Marceau",
        "battles": 2405,
        "winRate": 62.7
    },
    {
        "ship": "Attilio Regolo",
        "battles": 1425,
        "winRate": 62.7
    },
    {
        "ship": "Vampire II",
        "battles": 1661,
        "winRate": 62.4
    },
    {
        "ship": "Gdańsk",
        "battles": 1972,
        "winRate": 62.3
    },
    {
        "ship": "Hull",
        "battles": 2539,
        "winRate": 61.8
    },
    {
        "ship": "Daring",
        "battles": 2981,
        "winRate": 61.8
    },
    {
        "ship": "Lüshun",
        "battles": 1365,
        "winRate": 61.7
    },
    {
        "ship": "Grozovoi",
        "battles": 661,
        "winRate": 61.6
    },
    {
        "ship": "Álvaro de Bazán",
        "battles": 1548,
        "winRate": 61.4
    },
    {
        "ship": "Cassard",
        "battles": 1519,
        "winRate": 61.2
    },
    {
        "ship": "Georg Hoffmann",
        "battles": 1861,
        "winRate": 60.9
    },
    {
        "ship": "Ragnar",
        "battles": 1059,
        "winRate": 60.8
    },
    {
        "ship": "Delny",
        "battles": 258,
        "winRate": 60.5
    },
    {
        "ship": "Kléber",
        "battles": 1410,
        "winRate": 60.4
    },
    {
        "ship": "Yueyang",
        "battles": 1937,
        "winRate": 60.1
    },
    {
        "ship": "Hayate",
        "battles": 1099,
        "winRate": 59.5
    },
    {
        "ship": "Khabarovsk",
        "battles": 1323,
        "winRate": 59.3
    },
    {
        "ship": "Forrest Sherman",
        "battles": 1849,
        "winRate": 59.3
    },
    {
        "ship": "Shimakaze",
        "battles": 7266,
        "winRate": 59.1
    },
    {
        "ship": "Z-52",
        "battles": 1266,
        "winRate": 59
    },
    {
        "ship": "Gearing",
        "battles": 2903,
        "winRate": 58.6
    },
    {
        "ship": "Somers",
        "battles": 1190,
        "winRate": 58.2
    },
    {
        "ship": "Tromp",
        "battles": 5310,
        "winRate": 57.5
    },
    {
        "ship": "Druid",
        "battles": 1291,
        "winRate": 57.4
    },
    {
        "ship": "Elbing",
        "battles": 1412,
        "winRate": 56.5
    },
    {
        "ship": "La Pampa",
        "battles": 713,
        "winRate": 56.1
    },
    {
        "ship": "Halland",
        "battles": 3296,
        "winRate": 55.6
    },
    {
        "ship": "Harugumo",
        "battles": 857,
        "winRate": 54
    }
]

data3 = [
    {
        "ship": "Vampire II",
        "battles": 776,
        "winRate": 65.7
    },
    {
        "ship": "Småland",
        "battles": 3244,
        "winRate": 65.6
    },
    {
        "ship": "Daring",
        "battles": 4580,
        "winRate": 65.6
    },
    {
        "ship": "Álvaro de Bazán",
        "battles": 1425,
        "winRate": 65.2
    },
    {
        "ship": "Grozovoi",
        "battles": 554,
        "winRate": 63.9
    },
    {
        "ship": "Cassard",
        "battles": 2203,
        "winRate": 63.7
    },
    {
        "ship": "Lüshun",
        "battles": 1228,
        "winRate": 63.4
    },
    {
        "ship": "Georg Hoffmann",
        "battles": 1459,
        "winRate": 62.2
    },
    {
        "ship": "Somers",
        "battles": 406,
        "winRate": 61.8
    },
    {
        "ship": "Yueyang",
        "battles": 2098,
        "winRate": 60.7
    },
    {
        "ship": "La Pampa",
        "battles": 447,
        "winRate": 60.4
    },
    {
        "ship": "Gearing",
        "battles": 2207,
        "winRate": 60.1
    },
    {
        "ship": "Z-42",
        "battles": 1435,
        "winRate": 60
    },
    {
        "ship": "Ragnar",
        "battles": 1045,
        "winRate": 60
    },
    {
        "ship": "Attilio Regolo",
        "battles": 1297,
        "winRate": 59.6
    },
    {
        "ship": "Z-52",
        "battles": 895,
        "winRate": 59.3
    },
    {
        "ship": "Marceau",
        "battles": 2545,
        "winRate": 59.1
    },
    {
        "ship": "Hull",
        "battles": 3558,
        "winRate": 59.1
    },
    {
        "ship": "Gdańsk",
        "battles": 1615,
        "winRate": 58.6
    },
    {
        "ship": "Delny",
        "battles": 601,
        "winRate": 58.6
    },
    {
        "ship": "Shimakaze",
        "battles": 7999,
        "winRate": 58.6
    },
    {
        "ship": "Druid",
        "battles": 755,
        "winRate": 58.3
    },
    {
        "ship": "Tromp",
        "battles": 6118,
        "winRate": 57.6
    },
    {
        "ship": "Halland",
        "battles": 4421,
        "winRate": 57.3
    },
    {
        "ship": "Kléber",
        "battles": 1051,
        "winRate": 57
    },
    {
        "ship": "Hayate",
        "battles": 1093,
        "winRate": 56.7
    },
    {
        "ship": "Khabarovsk",
        "battles": 1296,
        "winRate": 56.5
    },
    {
        "ship": "Elbing",
        "battles": 919,
        "winRate": 53.8
    },
    {
        "ship": "Harugumo",
        "battles": 925,
        "winRate": 53.6
    },
    {
        "ship": "Forrest Sherman",
        "battles": 724,
        "winRate": 52.9
    }
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
