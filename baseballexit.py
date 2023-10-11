import math

# Constants
mass = 0.145     # Mass of baseball in kilograms
COR = 0.5        # Coefficient of restitution (typical value for a baseball)
grav = 32.174    # acceleration of gravity in feet per second squared

# Variables
pitch_speed = float(input("Pitch Speed in MPH: "))
angle = float(input("Launch Angle: "))
wind_speed = float(input("Wind Speed in MPH: "))
wind_direction = float(input("Wind Direction (in degrees, 0 to 360): "))

# Convert angle and wind direction to radians
angle_rad = math.radians(angle)
wind_direction_rad = math.radians(wind_direction)

# Convert pitch speed from mph to feet per second
pitch_speed_fps = pitch_speed * 1.46667

# Calculate initial velocity components including wind effect
vx0 = (pitch_speed_fps + wind_speed * math.cos(wind_direction_rad)) * math.cos(angle_rad)
vy0 = (pitch_speed_fps + wind_speed * math.cos(wind_direction_rad)) * math.sin(angle_rad)

# Calculate time to apex
t_apex = vy0 / grav

# Calculate maximum height
h = vy0 ** 2 / (2 * grav)

# Calculate time to ground
t_ground = math.sqrt(2 * h / grav)

# Calculate horizontal distance
x = vx0 * (t_apex + t_ground)

# Calculate final velocity magnitude
v_f = math.sqrt(vx0 ** 2 + (vy0 - 2 * grav * t_apex) ** 2) * COR

# Convert final velocity from feet per second to mph
v_f_mph = v_f / 1.46667

# Print result
print("Exit speed:", round(v_f_mph, 2), "mph")