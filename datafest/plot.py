import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(27, 27))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.margins(x=-0.001, y=-0.001)

gps = pd.read_csv('gps_filtered.csv').sort_values(by='PlayerID')
# gps = gps[gps.Half == 1]

scat = ax.scatter(gps[gps.FrameID == 1]['Longitude'], gps[gps.FrameID == 1]['Latitude'], s=150, color='red', alpha=0.5)


def update(frame_number):
    # print(frame_number)
    # Update the scatter collection, with the new positions
    scat.set_offsets(gps[gps.FrameID == frame_number][['Longitude', 'Latitude']])


# Construct the animation, using the update function as the animation director.
ani = animation = FuncAnimation(fig, update, interval=50, save_count=5000)  # 0.1s
ani.save('game_viz.mp4', bitrate=1000)
# plt.show()
