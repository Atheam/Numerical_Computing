from main import *
from generate import *
from copy import deepcopy



def test_erdos():
    N = [n for n in range(20,201,20)]
    print("ERDOS GRAPH TEST")
    for n in N:
        G = generate_erdos(n,p=0.3)
        I_2 = solve_kirch(deepcopy(G))
        I_1 = solve_potential(deepcopy(G))
        
        
        test_tab = (abs(I_1 - I_2) < 0.001) | (abs(I_1 + I_2) < 0.001)

        if not np.all(test_tab):
            print("Number of currents mismatched:",np.size(test_tab) - np.count_nonzero(test_tab),"for",n,"nodes")
        else:
            print("Number of currents mismatched: 0 for",n,"nodes")

def test_cubic():
    print("CUBIC GRAPH TEST")
    N = [n for n in range(20,201,20)]
    for n in N:
        G = generate_cubic(n)
        I_1 = solve_potential(deepcopy(G))
        I_2 = solve_kirch(deepcopy(G))
        
        
        test_tab = (abs(I_1 - I_2) < 0.001) | (abs(I_1 + I_2) < 0.001)

        if not np.all(test_tab):
            print("Number of currents mismatched:",np.size(test_tab) - np.count_nonzero(test_tab),"for",n,"nodes")
        else:
            print("Number of currents mismatched: 0 for",n,"nodes")

def test_grid():
    print("2D GRID GRAPH TEST")
    N = [n for n in range(3,14,2)]
    for n in N:
        G = generate_grid(n,n)
        I_1 = solve_potential(deepcopy(G))
        I_2 = solve_kirch(deepcopy(G))
        
        
        test_tab = (abs(I_1 - I_2) < 0.001) | (abs(I_1 + I_2) < 0.001)

        if not np.all(test_tab):
            print("Number of currents mismatched:",np.size(test_tab) - np.count_nonzero(test_tab),"for",n*n,"nodes")
        else:
            print("Number of currents mismatched: 0 for",n,"nodes")

def test_small_world():
    print("SMALL WORLD GRAPH TEST")
    N = [n for n in range(20,201,20)]
    for n in N:
        G = generate_small_world(n)
        I_1 = solve_potential(deepcopy(G))
        I_2 = solve_kirch(deepcopy(G))
        
        
        test_tab = (abs(I_1 - I_2) < 0.001) | (abs(I_1 + I_2) < 0.001)

        if not np.all(test_tab):
            print("Number of currents mismatched:",np.size(test_tab) - np.count_nonzero(test_tab),"for",n,"nodes")
        else:
            print("Number of currents mismatched: 0 for",n,"nodes")

def draw_examples():
    G1 = generate_erdos(15,p=0.3)
    G2 = generate_cubic(16)
    G3 = generate_grid(4,4)
    G4 = generate_small_world(15,k=4)

    G1_copy = deepcopy(G1)
    G2_copy = deepcopy(G2)
    G3_copy = deepcopy(G3)
    G4_copy = deepcopy(G4)


    I = solve_kirch(G1_copy)
    draw_circuit(G1_copy,I)

    I = solve_potential(G1)
    draw_circuit(G1,I)
    

    I = solve_kirch(G2_copy)
    draw_circuit(G2_copy,I)

    I = solve_potential(G2)
    draw_circuit(G2,I)

    I = solve_kirch(G3_copy)
    draw_circuit(G3_copy,I)

    I = solve_potential(G3)
    draw_circuit(G3,I)

    I = solve_kirch(G4_copy)
    draw_circuit(G4_copy,I)

    I = solve_potential(G4)
    draw_circuit(G4,I)


        
test_erdos()
test_cubic()
test_grid()
test_small_world()
draw_examples()

        
    
    
