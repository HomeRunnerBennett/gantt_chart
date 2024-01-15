This Python code generates a Gantt chart using the matplotlib library to visualize the schedule of a project with different phases, durations, and start dates. Here's an explanation of the code:
<img width="939" alt="image" src="https://github.com/HomeRunnerBennett/gantt_chart/assets/31154071/58bc7ca5-9fc1-4610-b962-9ef84657c0aa">

1. Import the required libraries:

import matplotlib.pyplot as plt
import numpy as np

2. Define project information, such as phases, durations (in weeks), and start dates (in weeks):

phases = ["Phase 1: Inception", "Phase 2: Iterative Design and Prototyping", "Phase 3: Time-Boxed Development Iterations", "Phase 4: Continuous Testing and Feedback", "Phase 5: Evolution of Requirements", "Phase 6: Finalization and Deployment", "Phase 7: Reflection and User Training", "Phase 8: Monitoring and Continuous Improvement"]
durations = [2, 4, 10, 6, 4, 4, 3, 4]  # in weeks
start_dates = [0, 2, 6, 16, 22, 26, 30, 33]  # in weeks

3. Define colors for each phase:

colors = ["#000000", "#C8102E", "#007A33", "#FFC107", "#2196F3", "#9C27B0", "#4CAF50", "#FF9800"]

4. Create a figure and an axis for the Gantt chart:


fig, ax = plt.subplots(figsize=(12, 8))

5. Plot the Gantt chart using ax.broken_barh to create horizontal bars for each phase:

for i in range(len(phases)):
    ax.broken_barh([(start_dates[i], durations[i])], (i-0.4, 0.8), facecolors=colors[i], label=phases[i])

6. Set axis labels, title, and limits:

ax.set_xlabel("Weeks")
ax.set_ylabel("Phases")
ax.set_title("Gantt Chart for Localized Agricultural Management System (AMS)")
ax.set_xlim(0, 37)
ax.set_ylim(-0.5, 7.5)

8. Add legend and grid:

ax.legend(loc="lower right")
ax.grid(True)

9. Display the Gantt chart:

plt.show()

<img width="766" alt="image" src="https://github.com/HomeRunnerBennett/gantt_chart/assets/31154071/667ddc52-0463-4058-bb6e-3c89abfec3cd">

This code creates a Gantt chart that visually represents the project phases, their durations, and the timeline of the project. The chart is displayed using matplotlib with different colors for each phase, and it includes labels, legends, and a grid for better readability. The output will be a graphical representation of the project schedule with labeled phases and corresponding time durations.






