import os
import matplotlib.pyplot as plt
import numpy as np

# Determine the current script directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Optionally, change the current working directory to the script directory
os.chdir(script_directory)

# Data
cores = np.array([128, 196, 256, 512])
aimd_walltime = np.array([12.62, 8.11, 6.37, 5.66])  # Hours
mlff_walltime = np.array([2.3585, 1.438, 1.1643, 1.0440])  # Hours

# Calculate speedup relative to the first element (128 cores, reference AIMD)
aimd_speedup = aimd_walltime[0] / aimd_walltime
mlff_speedup = aimd_walltime[0] / mlff_walltime

# Plotting
x = np.arange(len(cores))  # the label locations
width = 0.35  # the width of the bars

title_font_size = 14
axis_label_font_size = 12
tick_label_font_size = 10
legend_font_size = 10
bar_label_font_size = 10

fig, ax = plt.subplots()
# Bars with adjusted alpha
rects1 = ax.bar(x - width/2, aimd_speedup, width, label='AIMD', color='tab:blue', alpha=0.6)
rects2 = ax.bar(x + width/2, mlff_speedup, width, label='MLFF-AIMD', color='tab:red', alpha=0.6)

# Lines with points
ax.plot(x - width/2, aimd_speedup, marker='o', color='tab:blue', linewidth=3)
ax.plot(x + width/2, mlff_speedup, marker='o', color='tab:red', linewidth=3)

# Add some text for labels, title, and custom x-axis tick labels, with adjustable font sizes
ax.set_xlabel('Number of Cores (n)', fontsize=axis_label_font_size)
ax.set_ylabel('Speedup ( t(n = 128, AIMD) / t (n) )', fontsize=axis_label_font_size)
ax.set_title(r'1000 AIMD steps, CH$_3$NH$_3$PbI$_3$', fontsize=title_font_size)
ax.set_xticks(x)
ax.set_xticklabels(cores, fontsize=tick_label_font_size)

# Adjust legend to accommodate both bars and lines
handles, labels = ax.get_legend_handles_labels()
# Combine handles and labels for bars and lines and set the legend
ax.legend(handles, labels, fontsize=legend_font_size, loc='best')

# Format the speedup numbers to two decimal places for the bar labels and adjust font size
ax.bar_label(rects1, padding=3, fmt='%.2f', fontsize=bar_label_font_size)
ax.bar_label(rects2, padding=3, fmt='%.2f', fontsize=bar_label_font_size)

# Hide the grid
ax.grid(False)

fig.tight_layout()
plt.savefig('speedup.png', dpi = 800)
plt.show()