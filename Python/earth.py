import matplotlib.pyplot as plt

# Constants (in arbitrary units for simplicity)
G = 1  # Gravitational constant
EARTH_MASS = 1000
MOON1_MASS = 1
MOON2_MASS = 0.5

# Initial positions and velocities (in arbitrary units)
earth_pos = [0, 0]
earth_vel = [0, 0]
moon1_pos = [5, 0]
moon1_vel = [0, 2]
moon2_pos = [8, 0]
moon2_vel = [0, -1]

# Time step and total time for simulation
dt = 0.01
total_time = 10

# Lists to store the positions of Earth and moons at each time step
earth_positions = [earth_pos]
moon1_positions = [moon1_pos]
moon2_positions = [moon2_pos]

# Simulation loop
num_steps = int(total_time / dt)
for _ in range(num_steps):
    # Calculate the distance and direction between Earth and each moon
    dist_moon1 = [(moon1_pos[i] - earth_pos[i]) for i in range(2)]
    dist_moon2 = [(moon2_pos[i] - earth_pos[i]) for i in range(2)]
    
    # Calculate the accelerations due to gravitational forces
    moon1_acc = [(G * EARTH_MASS / dist_moon1[i]**3) for i in range(2)]
    moon2_acc = [(G * EARTH_MASS / dist_moon2[i]**3) for i in range(2)]
    
    # Update velocities using the Euler method
    for i in range(2):
        moon1_vel[i] -= moon1_acc[i] * dt
        moon2_vel[i] -= moon2_acc[i] * dt

    # Update positions using the Euler method
    for i in range(2):
        moon1_pos[i] += moon1_vel[i] * dt
        moon2_pos[i] += moon2_vel[i] * dt

    # Append positions to the lists
    earth_positions.append(earth_pos.copy())
    moon1_positions.append(moon1_pos.copy())
    moon2_positions.append(moon2_pos.copy())

# Plotting the orbits
earth_positions = list(zip(*earth_positions))
moon1_positions = list(zip(*moon1_positions))
moon2_positions = list(zip(*moon2_positions))

plt.plot(earth_positions[0], earth_positions[1], label="Earth")
plt.plot(moon1_positions[0], moon1_positions[1], label="Moon 1")
plt.plot(moon2_positions[0], moon2_positions[1], label="Moon 2")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Orbits of Two Moons around Earth")
plt.legend()
plt.grid()
plt.axis("equal")
plt.show()
