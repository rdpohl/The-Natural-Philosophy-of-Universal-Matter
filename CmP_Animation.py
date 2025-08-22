'''
    RDPohl, May 3, 2025
    This seems to show a 2-axis rotation works as needed to describe
    the EM wave
'''

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def animate(i):
    """Updates the plot for each frame of the animation."""
    angle_x = i  # Rotate around x-axis
    angle_y = i  # Rotate around y-axis

    rotated_data = rotate_around_axis(cross_data, -angle_x, 'y')
    rotated2_data = rotate_around_axis(cross_data, angle_y, 'z')

    lines[0].set_data(rotated_data[:2, 0], rotated_data[:2, 1])
    lines[0].set_3d_properties(rotated_data[:2, 2])
    lines[0].set_color('red')
        
    lines[1].set_data(rotated2_data[2:, 0], rotated2_data[2:, 1])
    lines[1].set_3d_properties(rotated2_data[2:, 2])
    lines[1].set_color('blue')
    
    return lines

def rotate_around_axis(data, angle, axis='x'):
    """Rotates a set of points around a specified axis."""
    rad = np.radians(angle)
    if axis == 'x':
        rotation_matrix = np.array([[1, 0, 0],
                                    [0, np.cos(rad), np.sin(rad)],
                                    [0, np.sin(rad), np.cos(rad)]])
    elif axis == 'y':  
        rotation_matrix = np.array([[np.cos(rad), 0, np.sin(rad)],
                                    [0, 1, 0],
                                    [np.sin(rad), 0, np.cos(rad)]])
    elif axis == 'z':
        rotation_matrix = np.array([[np.cos(rad), np.sin(rad), 0],
                                    [np.sin(rad), np.cos(rad), 0],
                                    [0, 0, 1]])
    else:
        raise ValueError("Axis must be 'x', 'y', or 'z'")
    return np.dot(data, rotation_matrix)

# Define the initial 2D cross shape
cross_data = np.array([[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0]])

# Create the figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Initialize the plot
lines = [ax.plot([], [], [])[0] for _ in range(2)]

ax.set(xlim3d=(-2, 2), xlabel='X')
ax.set(ylim3d=(-2, 2), ylabel='Y')
ax.set(zlim3d=(-2, 2), zlabel='Z')

ax.set_xticks(np.arange(-2, 2, 1))
ax.set_yticks(np.arange(-2, 2, 1))
ax.set_zticks(np.arange(-2, 2, 1))
ax.grid(True)

# Define the range for the axes
axes_range = np.array([-3, 3])

ax.plot(axes_range, [0, 0], [0, 0], color='black', label='x-axis')
ax.plot([0, 0], axes_range, [0, 0], color='black', label='y-axis')
ax.plot([0, 0], [0, 0], axes_range, color='black', label='z-axis')

# Animation function
# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=180, interval=20, blit=True)

plt.show()
