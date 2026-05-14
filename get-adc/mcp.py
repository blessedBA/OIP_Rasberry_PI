import mcp3021_driver as mcp
import adc_plot as plt
import time

if __name__ == "__main__":
        try:
            adc = mcp.MCP3021(5.2, False)
            voltage_values = []
            time_values = []
            duration = 3.0
            start_time = time.time()
            while ((time.time() - start_time) < duration):
                voltage = adc.get_sc_voltage()
                time_values.append(time.time() - start_time)
                voltage_values.append(voltage)
            plt.plot_voltage_vs_time(time_values, voltage_values, 3.3)
            plt.plot_sampling_period_hist(time_values)

        finally:
            adc.deinit()