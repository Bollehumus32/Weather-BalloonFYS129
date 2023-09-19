from pylab import *

# Constants:
    
C_d = 0.47              # Dragcoefficient for a circle
y_hat = 1               # y_hat, unit vector in y direction


# Lambad functions:
    
A = lambda d: pi * (d/2)**2         # d being diameter

m_helium = lambda rho, V: rho * V

F_oppdrift = lambda P_L, P_He, V, g: (P_L - P_He) * V * g

F_gravitasjon = lambda m_b, m_he, g: (m_b + m_he) * g * y_hat

F_vind = lambda m, v_w, t: m * v_w/t

F_drakraft = lambda P_L, v_w, A: 1/2 * C_d * P_L * A * v_w

Skalar_Oppdrift_Vindkraft = lambda F_oppdrift, F_vind: sqrt(abs(F_oppdrift)**2 + abs(F_vind)**2)

Theta_OV = lambda F_oppdrift, Skalar_Oppdrift_Vindkraft: arcsin((abs(F_oppdrift)/abs(Skalar_Oppdrift_Vindkraft)))

Theta_Drakraft = lambda Theta_OV: Theta_OV + pi

F_drakraft_x = lambda F_drakraft, Theta_Drakraft: F_drakraft * cos(Theta_Drakraft)

F_drakraft_y = lambda F_drakraft, Theta_Drakraft: F_drakraft * sin(Theta_Drakraft)

Volume = lambda r : 4/3*pi*r**3





