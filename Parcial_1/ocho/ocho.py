import random






while True:
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)

    print("Dado 1:", dado_1)
    print("Dado 2:", dado_2)
    
    try:
        if dado_1 + dado_2 == 8:
            print("\nUsted ha ganado! :3")
            break
        elif dado_1 + dado_2 == 7:
            print("\nUsted ha perdido :(")
            break
        else:
            print("Sigue lanzando")

    except: #En caso de error:
        break
