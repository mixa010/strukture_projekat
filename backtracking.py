import time

def validan_potez(x, y, tabla):
    return 0 <= x < len(tabla) and 0 <= y < len(tabla) and tabla[x][y] == -1

def rijesi_turu_skakaca(tabla, trenutni_x, trenutni_y, potezi_x, potezi_y, pozicija):
    if pozicija == len(tabla) * len(tabla):
        return True
    
    for i in range(8):
        novi_x = trenutni_x + potezi_x[i]
        novi_y = trenutni_y + potezi_y[i]
        if validan_potez(novi_x, novi_y, tabla):
            tabla[novi_x][novi_y] = pozicija
            if rijesi_turu_skakaca(tabla, novi_x, novi_y, potezi_x, potezi_y, pozicija + 1):
                return True
            tabla[novi_x][novi_y] = -1  # Povratak unazad
    return False

def tura_skakaca(velicina):
    tabla = [[-1 for _ in range(velicina)] for _ in range(velicina)]
    potezi_x = [2, 1, -1, -2, -2, -1, 1, 2]
    potezi_y = [1, 2, 2, 1, -1, -2, -2, -1]
    tabla[0][0] = 0

    if not rijesi_turu_skakaca(tabla, 0, 0, potezi_x, potezi_y, 1):
        return "Rješenje ne postoji"
    else:
        return tabla

# Mjerenje vremena izvršavanja
velicina_table = 8  
start_time = time.time()
tura = tura_skakaca(velicina_table)
end_time = time.time()

if isinstance(tura, str):
    print(tura)
else:
    for red in tura:
        print(red)

print(f"Vrijeme izvršavanja: {end_time - start_time:.6f} sekundi")
