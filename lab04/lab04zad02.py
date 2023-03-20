import time
import matplotlib.pyplot as plt
import random

from aco import AntColony


plt.style.use("dark_background")


COORDS = (
    (20, 52),
    (43, 50),
    (20, 84),
    (70, 65),
    (29, 90),
    (87, 83),
    (73, 23),
    # (55, 50),
    # (55, 20),
    # (20, 50),
    # (50, 87),
    # (80, 90),

)


def random_coord():
    r = random.randint(0, len(COORDS))
    return r


def plot_nodes(w=12, h=8):
    for x, y in COORDS:
        plt.plot(x, y, "g.", markersize=15)
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])


def plot_all_edges():
    paths = ((a, b) for a in COORDS for b in COORDS)

    for a, b in paths:
        plt.plot((a[0], b[0]), (a[1], b[1]))

start=time.time()
plot_nodes()

colony = AntColony(COORDS, ant_count=300, alpha=0.5, beta=1.2, 
                    pheromone_evaporation_rate=0.10, pheromone_constant=1000.0,
                    iterations=200)

optimal_nodes = colony.get_path()

end=time.time()

for i in range(len(optimal_nodes) - 1):
    plt.plot(
        (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
        (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
    )

print('der Zeit: ',end-start)
plt.show()

#czas dla początkowych wartości: 26.881932258605957
#czas dla 12 wierzchołków: 39.48424220085144
#czas dla 10 wierzchołków: 33.2459762096405

#coords takie jak początkowe:
#COORDS, ant_count=400, alpha=0.5, beta=1.2, pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,iterations=300:
#34.057249546051025
#COORDS, ant_count=100, alpha=0.5, beta=1.2, pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,iterations=300:
#9.790606498718262
#COORDS, ant_count=300, alpha=0.9, beta=1.2, pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,iterations=300:
#27.617783546447754
#COORDS, ant_count=300, alpha=0.1, beta=1.2, pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,iterations=300:
#27.648799419403076
#COORDS, ant_count=300, alpha=0.5, beta=1.7, pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,iterations=300:
#27.995697736740112
#COORDS, ant_count=300, alpha=0.5, beta=0.6, pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,iterations=300:
#26.672244787216187
#COORDS, ant_count=300, alpha=0.5, beta=1.2, pheromone_evaporation_rate=0.70, pheromone_constant=1000.0,iterations=300:
#26.886788368225098
#COORDS, ant_count=300, alpha=0.5, beta=1.2, pheromone_evaporation_rate=0.10, pheromone_constant=1000.0,iterations=300:
#26.340469121932983
#COORDS, ant_count=300, alpha=0.5, beta=1.2, pheromone_evaporation_rate=0.40, pheromone_constant=1900.0,iterations=300:
#27.171123504638672
#COORDS, ant_count=300, alpha=0.5, beta=1.2, pheromone_evaporation_rate=0.40, pheromone_constant=500.0,iterations=300:
#26.672858715057373
#COORDS, ant_count=300, alpha=0.5, beta=1.2, pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,iterations=400:
#36.08818793296814
#COORDS, ant_count=300, alpha=0.5, beta=1.2, pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,iterations=200:
#17.86691451072693

# Im większa liczba wierzchołków, tym dłuższy czas wykonania.
# Najlepszy czas wykonania (9.79 s) osiągnięto dla 100 mrówek.
# Wysoka wartość parametru alpha (0.9) spowodowała zwiększenie czasu wykonania.
# Niska wartość parametru alpha (0.1) również wpłynęła niekorzystnie na czas wykonania.
# Zmiana parametru beta z 1.2 na 1.7 wpłynęła nieznacznie na długość czasu wykonania.
# Zmiana parametru beta z 1.2 na 0.6 również wpłynęła nieznacznie na czas wykonania.
# Zmniejszenie współczynnika parowania feromonów z 0.4 na 0.1 nieznacznie zmniejszyło czas wykonania.
# Zwiększenie współczynnika parowania feromonów z 0.4 na 0.7 nieznacznie zwiększyło czas wykonania.
# Zmiana wartości stałej feromonowej z 1000.0 na 1900.0 spowodowała nieznaczne zwiększenie czasu wykonania.
# Zmniejszenie wartości stałej feromonowej z 1000.0 na 500.0 również spowodowało nieznaczne zmniejszenie czasu wykonania.
# Zwiększenie liczby iteracji z 300 na 400 spowodowało znaczne wydłużenie czasu wykonania.
# Zmniejszenie liczby iteracji z 300 na 200 znacznie skróciło czas wykonania.