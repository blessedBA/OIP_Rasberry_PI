from r2r_adc import R2R_ADC
import time
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

adc = R2R_ADC(3.3, 0.0001, False)

voltage_values = []
time_values = []
duration = 10.0
dynamic_range = 3.3

try:
    start_time = time.time()
    while time.time() - start_time < duration:
        voltage_values.append(adc.get_sc_voltage())
        time_values.append(time.time() - start_time)

    plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
    plot_sampling_period_hist(time_values)

finally:
    if adc is not None:
        adc.deinit()