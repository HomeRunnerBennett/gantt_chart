# Import matplotlib and numpy libraries
import matplotlib.pyplot as plt
import numpy as np

# Define the project phases, durations, and start dates
phases = ["Phase 1: Inception", "Phase 2: Iterative Design and Prototyping", "Phase 3: Time-Boxed Development Iterations", "Phase 4: Continuous Testing and Feedback", "Phase 5: Evolution of Requirements", "Phase 6: Finalization and Deployment", "Phase 7: Reflection and User Training", "Phase 8: Monitoring and Continuous Improvement"]
durations = [2, 4, 10, 6, 4, 4, 3, 4] # in weeks
start_dates = [0, 2, 6, 16, 22, 26, 30, 33] # in weeks

# Define the colors for the phases
colors = ["#000000", "#C8102E", "#007A33", "#FFC107", "#2196F3", "#9C27B0", "#4CAF50", "#FF9800"]

# Create a figure and an axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the gantt chart as horizontal bars
for i in range(len(phases)):
    ax.broken_barh([(start_dates[i], durations[i])], (i-0.4, 0.8), facecolors=colors[i], label=phases[i])

# Set the axis labels, title, and limits
ax.set_xlabel("Weeks")
ax.set_ylabel("Phases")
ax.set_title("Gantt Chart for Localized Agricultural Management System (AMS)")
ax.set_xlim(0, 37)
ax.set_ylim(-0.5, 7.5)

# Add a legend and a grid
ax.legend(loc="lower right")
ax.grid(True)

# Show the gantt chart
plt.show()
