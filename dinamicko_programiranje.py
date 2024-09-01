import time

def broj_nacina_do_pozicije(n, m, velicina):
    # Inicijalizacija kvadratne matrice
    dp = [[0] * velicina for _ in range(velicina)]
    dp[0][0] = 1  # Početna pozicija skakača

    potezi = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    for x in range(velicina):
        for y in range(velicina):
            for dx, dy in potezi:
                nx, ny = x + dx, y + dy
                if 0 <= nx < velicina and 0 <= ny < velicina:
                    dp[nx][ny] += dp[x][y]

    return dp[n][m]

# Mjerenje vremena izvršavanja
velicina_table = 32  # Veličina table
n, m = 31, 31  # Ciljana pozicija
start_time = time.time()
broj_puteva = broj_nacina_do_pozicije(n, m, velicina_table)
end_time = time.time()

print(f"Broj načina za dolazak do pozicije ({n}, {m}) na tabli veličine {velicina_table}x{velicina_table} je: {broj_puteva}")
print(f"Vrijeme izvršavanja: {end_time - start_time:.6f} sekundi")
