# Programmeer een simulatie lus waarin
# Een auto met massa 600 kilogram
# en netto voortstuwingskracht F = 800 N* optrekt
# over een afstand van 100 meter
# Print de eindtijd via de console
# *Motorvermogen, overbrengingsmoment ("grip") en luchtweerstand nemen we niet mee

# Ticking clock: while (running):
# t_new = t_old + dt
# 
# dt = delta tijd verstreken

# Accelereren
# dv = F/m * dt
# v_new = v_old + dv
# 
# dv = delta snelheid

# Verplaatsen:
# dx = v_new * dt
# x_new = x_old + dx
# 
# dx = delta afstand

# Define our car

F_motor = 800
mass = 600
a = F_motor / mass
v = 0
x = 0


# Defenition clock
dt = 0.01
t = 0
running = True

while (running):
    t = t + dt
    dv = a * dt
    v = v + dv
    dx = v * dt
    x = x + dx
#    print(x)
#    print(t)
    if x >= 100:
        

        print(f"Velocity: {v}")
        print(f"Translation: {x}")
        print(f"Tijd: {t}")

        running = False