from pylab import *
from Functions import *
from matplotlib.widgets import *

g = 9.81

def main():
    # Initial conditions
    r = 0.75
    d = 2*r
    V = 4/3*pi*r**3
    m_balloon = 0.35  # mass of the balloon material
    velocity_wind = 5  # wind speed in m/s
    time_interval = 0.1  # time step in seconds
    
    rho_air = 1.225  # in kg/m^3 (air density at sea level)
    rho_helium = 0.1786  # in kg/m^3 (helium density)

    # Initialize
    time_array = linspace(0, 100, int(100 / time_interval) + 1)
    position_x_array = zeros_like(time_array)
    position_y_array = zeros_like(time_array)
    
    position_x_array[0] = 0
    position_y_array[0] = 0
    
    # Main simulation loop
    for i in range(1, len(time_array)):
        t = time_array[i]
        mass_helium = m_helium(rho_helium, V)  # Using density directly
    
        F_b = F_oppdrift(rho_air, rho_helium, V, g)
        F_g = F_gravitasjon(m_balloon, mass_helium, g)
        F_w = F_vind(mass_helium, velocity_wind, time_interval)
    
        Scalar_OV = Skalar_Oppdrift_Vindkraft(F_b, F_w)
        theta_ov = Theta_OV(F_b, Scalar_OV)
        theta_d = Theta_Drakraft(theta_ov)
    
        F_d = F_drakraft(rho_air, velocity_wind, A(d))
        F_dx = F_drakraft_x(F_d, theta_d)
        F_dy = F_drakraft_y(F_d, theta_d)
    
        F_net_x = F_w - F_dx
        F_net_y = F_b - F_g - F_dy
    
        # Update position using Euler's method
        position_x_array[i] = position_x_array[i-1] + F_net_x * time_interval
        position_y_array[i] = position_y_array[i-1] + F_net_y * time_interval
        t += time_interval
    
    # Plotting
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)
    plt.grid()
    plt.plot(time_array, position_x_array, label='X Position')
    plt.xlabel('Time (s)')
    plt.ylabel('Position X [m]')
    
    plt.plot(time_array, position_y_array, label='Y Position')
    plt.xlabel('Time (s)')
    plt.ylabel('Position Y [m]')
    plt.legend()
    

    # Slider for adjusting balloon mass:
    axcolor = 'lightgoldenrodyellow'
    axmass = plt.axes([0.25, 0, 0.65, 0.03], facecolor=axcolor)
    b_mass = Slider(axmass, 'Mass of Balloon', 0, 1, valinit=m_balloon)

    # Slider for adjusting the wind velocity:
    ax_w_velocity = plt.axes([0.25, 0.025, 0.65, 0.03], facecolor=axcolor)
    w_velocity = Slider(ax_w_velocity, 'Wind Velocity', -10, 10, valinit=velocity_wind)

    # Slider for helium density:
    ax_rho_he = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
    density_he = Slider(ax_rho_he, 'Helium Density', 0, 1, valinit=rho_helium)

    # Slider for diameter:
    ax_diameter= plt.axes([0.25, 0.075, 0.65, 0.03], facecolor=axcolor)
    diameter_balloon = Slider(ax_diameter, 'Balloon Diameter', 0.1, 5, valinit=d)
    
    # Update function to update the graph whenever a value slider is changed:
    def update(val):
        m_balloon = b_mass.val
        velocity_wind = w_velocity.val
        rho_helium = density_he.val
        d = diameter_balloon.val

        time_array = linspace(0, 100, int(100 / time_interval) + 1)
        position_x_array = zeros_like(time_array)
        position_y_array = zeros_like(time_array)
        
        position_x_array[0] = 0
        position_y_array[0] = 0
        
        # Main simulation loop
        for i in range(1, len(time_array)):
            t = time_array[i]
            mass_helium = m_helium(rho_helium, V)  # Using density directly
        
            F_b = F_oppdrift(rho_air, rho_helium, V, g)
            F_g = F_gravitasjon(m_balloon, mass_helium, g)
            F_w = F_vind(mass_helium, velocity_wind, time_interval)
        
            Scalar_OV = Skalar_Oppdrift_Vindkraft(F_b, F_w)
            theta_ov = Theta_OV(F_b, Scalar_OV)
            theta_d = Theta_Drakraft(theta_ov)
        
            F_d = F_drakraft(rho_air, velocity_wind, A(d))
            F_dx = F_drakraft_x(F_d, theta_d)
            F_dy = F_drakraft_y(F_d, theta_d)
        
            F_net_x = F_w - F_dx
            F_net_y = F_b - F_g - F_dy
        
            # Update position using Euler's method
            position_x_array[i] = position_x_array[i-1] + F_net_x * time_interval
            position_y_array[i] = position_y_array[i-1] + F_net_y * time_interval
            t += time_interval

        ax.clear()
        ax.grid()
        ax.plot(time_array, position_x_array, label='X Position')
        ax.plot(time_array, position_y_array, label='Y Position')
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Position [m]')
        ax.legend()

        plt.draw()

    b_mass.on_changed(update)
    w_velocity.on_changed(update)
    density_he.on_changed(update)
    diameter_balloon.on_changed(update)
    
    plt.show()

if __name__ == "__main__":
    main()