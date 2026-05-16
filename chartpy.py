from pyscript import document, display
import numpy as np

# Suppress matplotlib font logs
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

# Preload to avoid font cache message
plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

# Store data globally
days = []
kills = []


def displaying(e):
    day = document.getElementById('dayOfTheWeek').value
    kill_count = int(document.getElementById('kills').value)

    # Save data
    days.append(day)
    kills.append(kill_count)

    # Convert to NumPy array
    converted_kills = np.array(kills)

    # Clear previous plot
    plt.clf()

    # Create graph
    plt.plot(days, converted_kills, marker='o')
    plt.title("Weekly Body Count (Kills)")
    plt.xlabel("Day")
    plt.ylabel("Number of Kills")
    plt.grid()

    # Display plot
    plt.show()
