import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def first_gen(x,y, start_pop):
    X = (np.random.rand(x,y)>start_pop).astype(int) #Erstellt eine {x}x{y} Matrix mit Zufallszahlen zwischen 0 und 1, die dann in eine Binärmatrix umgewandelt wird, wobei Werte größer als start_pop auf 1 gesetzt werden und alle anderen auf 0.
    return X

def next_gen(X):
    count = X[:-2,:-2] + X[:-2,1:-1] + X[:-2,2::] + X[1:-1,:-2] + X[1:-1,2:] + X[2:,:-2] + X[2:,1:-1] + X[2:,2:] #Zählt die Anzahl der lebenden Nachbarn für jedes Element in der Matrix X, indem es die Werte der umliegenden Zellen summiert.

    newX = ((count==3) & (X[1:-1,1:-1]==0)) | (((count==3)|(count==2)) & (X[1:-1,1:-1]==1)) #Erstellt eine neue Matrix newX, die die nächste Generation der Zellen basierend auf den Regeln des Spiels des Lebens berechnet. Eine tote Zelle wird lebendig, wenn sie genau 3 lebende Nachbarn hat, und eine lebende Zelle bleibt lebendig, wenn sie 2 oder 3 lebende Nachbarn hat.
    X[:]=0
    X[1:-1,1:-1] = newX
    return X

def endless_game(x,y):
    X = first_gen(x,y)
    while True:
        print(X)
        X = next_gen(X)
def defined_game(x,y, start_pop, rounds):
    X = first_gen(x,y, start_pop)
    for i in range(rounds):
        print(X)
        X = next_gen(X)

def animate_game(x, y, start_pop=0.3, interval=200):
    grid = first_gen(x, y, start_pop)
    
    fig, ax = plt.subplots()
    
    img = ax.imshow(grid, cmap='binary', interpolation='nearest')
    ax.axis('off')

    def update(*args):
        nonlocal grid
        grid = next_gen(grid)
        img.set_array(grid)
        return [img]


    ani = animation.FuncAnimation(fig, update, interval=interval, blit=True, cache_frame_data=False)
    plt.show()

# Starte das Spiel mit einer 50x50 Matrix und 30% Startpopulation
animate_game(100, 100, start_pop=0.9, interval=100)