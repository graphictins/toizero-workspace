

import matplotlib.pyplot as plt

def generate_beam_plot(red_pts=[2, 7, 8, 15, 20], blue_pts=[3, 4, 5, 7, 10, 16, 21]):
    
    # Red starts at (0, 1), flips at each hit
    red_x = [0] + red_pts
    red_y = []
    curr_y = 1
    for _ in red_x:
        red_y.append(curr_y)
        curr_y = 1 - curr_y
        
    # Blue starts at (0, 0), flips at each hit
    blue_x = [0] + blue_pts
    blue_y = []
    curr_y = 1
    for _ in blue_x:
        blue_y.append(curr_y)
        curr_y = 1 - curr_y

    plt.figure(figsize=(10, 4))
    
    # Vertical grid lines at every event point
    all_events = sorted(list(set(red_pts + blue_pts)))
    for xi in all_events:
        plt.axvline(x=xi, color='gray', linestyle='--', alpha=0.3)
    plt.axvline(x=0, color='gray', linestyle='--', alpha=0.3)

    # Plot paths
    plt.plot(red_x, red_y, color='red', marker='o', label='Red Beam (Start Top)', linewidth=2)
    plt.plot(blue_x, blue_y, color='blue', marker='x', label='Blue Beam (Start Bottom)', linewidth=2)

    # Formatting
    plt.ylim(-0.2, 1.2)
    plt.yticks([0, 1], ['Bottom (0)', 'Top (1)'])
    plt.xlabel("Distance X")
    plt.xticks(range(0, max(max(red_pts), max(blue_pts)) + 1))
    plt.ylabel("Rail Position")
    plt.title("Beam Reflection Visualization")
    plt.legend()
    plt.grid(True, axis='y', linestyle=':')
    
    # plt.savefig('beam_visualization2.png')
    # plt.close()
    plt.show()

if __name__ == "__main__":
    generate_beam_plot()