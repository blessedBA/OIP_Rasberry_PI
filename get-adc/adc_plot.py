import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    
    plt.title("voltage versus time")
    plt.xlabel("Time, s")
    plt.ylabel("Voltage, V")

    if time:
        plt.xlim(0, max(time))
    plt.ylim (0, max_voltage)

    plt.grid(True)
    plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = [
        time[i] - time[i - 1]
        for i in range(1, len(time))
    ]

    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods)

    plt.title("Sampling period histogram")
    plt.xlabel("Sampling period, s")
    plt.ylabel("Number of measurements")
    plt.xlim(0, 0.06)

    plt.grid(True)
    plt.show()