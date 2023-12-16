import json
import numpy as np
from scipy.signal import butter, lfilter

def load_json_data(file_path):
    try:
        with open(file_path) as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON data from '{file_path}'. Check if the file contains valid JSON.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def calculate_sample_period(x):
    try:
        n = 20  # calculate from first 20 samples
        return sum([x[i + 1] - x[i] for i in range(n)])
    except Exception as e:
        print(f"Error in calculate_sample_period: {e}")
        return None
    
def stepTime(x):
    try:
        n=len(x)
        s = sum([x[i + 1] - x[i] for i in range(n - 1)])
        return (s/(n-1))
    except Exception as e:
        print(f"Error in calculate_steptime: {e}")
        return None

def butterworth_filter(data, sample_period, n):
    try:
        sample_rate = 1 / sample_period
        cutoff = 10 / (0.5 * sample_rate)
        nyq = 0.5 * sample_rate
        order = n
        b, a = butter(order, 0.9, btype='lowpass')
        y = lfilter(b, a, data)
        return y
    except Exception as e:
        print(f"Error in butterworth_filter: {e}")
        return None

def local_maxima_minima(x):
    try:
        maxima = []
        minima = []
        for i in range(1, len(x) - 1):
            if x[i] > x[i - 1] and x[i] > x[i + 1]:
                maxima.append(i)
            elif x[i] < x[i - 1] and x[i] < x[i + 1]:
                minima.append(i)
        return maxima, minima
    except Exception as e:
        print(f"Error in local_maxima_minima: {e}")
        return None, None

# Main code
def runCalc(_path, _tLength):
    
    file_path = _path #'30sec_sampleData.json'
    data = load_json_data(file_path)
    totalLength = _tLength #  30  #in meters

    if data is not None:
        try:
            #samples = 50 * np.array([np.sin(2 * np.pi * i / 20) for i in range(98)])  #for testing maxima minima function
            timestamps = [sample['timestamp'] for sample in data.get('GaitScribe_123', [])]

        #@knee
            # ax_x = [sample['sensor_012']['ax_x'] for sample in data.get('GaitScribe_123', [])]
            # ax_y = [sample['sensor_012']['ax_y'] for sample in data.get('GaitScribe_123', [])]
            # ax_z = [sample['sensor_012']['ax_z'] for sample in data.get('GaitScribe_123', [])]
        #@ankle
            # ax_x2 = [sample['sensor_013']['ax_x'] for sample in data.get('GaitScribe_123', [])]
            ax_y2 = [sample['sensor_013']['ax_y'] for sample in data.get('GaitScribe_123', [])]
            # ax_z2 = [sample['sensor_013']['ax_z'] for sample in data.get('GaitScribe_123', [])]

            x=ax_y2 #ankle sensor axis selection

            sp = calculate_sample_period(timestamps)
            if sp is not None:
                b_samples = butterworth_filter(x, sp, 4)
                if b_samples is not None:
                    maxima, minima = local_maxima_minima(b_samples)
                    if maxima is not None and minima is not None:
                        peak_timestamps = [timestamps[i] for i in maxima]
                        st = stepTime(peak_timestamps) / 1000  # conversion from ms to seconds

                        cadence=60/st    #cadence
                        sl = totalLength/len(maxima)
                        print("stepTime in seconds", st)
                        print("cadence",cadence)
                        print("step length in meters",sl)


        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def plotGraph(_path):

    file_path = _path #'30sec_sampleData.json'
    data = load_json_data(file_path)

    if data is not None:
        try:
            #samples = 50 * np.array([np.sin(2 * np.pi * i / 20) for i in range(98)])  #for testing maxima minima function
            timestamps = [sample['timestamp'] for sample in data.get('GaitScribe_123', [])]

        #@knee
            # ax_x = [sample['sensor_012']['ax_x'] for sample in data.get('GaitScribe_123', [])]
            # ax_y = [sample['sensor_012']['ax_y'] for sample in data.get('GaitScribe_123', [])]
            # ax_z = [sample['sensor_012']['ax_z'] for sample in data.get('GaitScribe_123', [])]
        #@ankle
            # ax_x2 = [sample['sensor_013']['ax_x'] for sample in data.get('GaitScribe_123', [])]
            ax_y2 = [sample['sensor_013']['ax_y'] for sample in data.get('GaitScribe_123', [])]
            # ax_z2 = [sample['sensor_013']['ax_z'] for sample in data.get('GaitScribe_123', [])]
            return timestamps, ax_y2
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# runCalc('sampleData/30sec_sampleData.json', 30)