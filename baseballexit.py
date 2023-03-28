import math

# Constants
mass = 0.145     # Mass of baseball in kilograms
COR = 0.5        # Coefficient of restitution (typical value for a baseball)
grav = 78972.650505968 # acceleration of gravity in mph^2

# Variables
pitch_speed = input("Pitch Speed in MPH:")
angle = input("Launch Angle:")

# Convert angle to radians
theta = math.radians(angle)

# Calculate initial velocity components
vx0 = pitch_speed * math.cos(theta)
vy0 = pitch_speed * math.sin(theta)

# Calculate time to apex
t_apex = vy0 / grav

# Calculate maximum height
h = vy0**2 / (2 * grav)

# Calculate time to ground
t_ground = math.sqrt(2 * h / grav)

# Calculate horizontal distance
x = vx0 * (t_apex + t_ground)

# Calculate final velocity magnitude
v_f = math.sqrt(vx0**2 + (vy0 - 2 * grav * t_apex)**2) * COR

# Print result
print("Exit speed:", round(v_f, 2), "mph")
