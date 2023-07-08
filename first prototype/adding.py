import numpy as np
from scipy.io.wavfile import read, write

# read the wav file
count = 0
for index in range(9876,9877):
    path = "C:\\Users\\om\\Desktop\\anti piracy\\first prototype\\use.wav"
    rate, data = read(path)

    # Make sure it's mono by taking the first channel onliy
    if len(data.shape) > 1:
        data = data[:, 0]
        
    ones = index % 10
    tens = (index // 10) % 10
    hundreds = (index // 100) % 10
    thousands = (index // 1000) % 10

    if ones == 0 or tens == 0 or hundreds == 0 or thousands == 0:
        continue
    if ones == tens or ones == hundreds or ones == thousands or tens == hundreds or tens == thousands or hundreds == thousands:
        continue
    # print(index)
    count += 1
# print(count)
    # Specify the frequencies
    # frequencies = [20000, 20500, 21000, 21500, 22000]  # in Hz
    frequencies = [20000, 20250, 20500, 20750, 21000]  # in Hz
    sine_duration = 0.005  # duration of sine wave in seconds

    # Calculate the length of the audio clip in seconds
    clip_length = len(data) / rate

    # Loop through every two minutes interval in the audio clip
    for start_min in np.arange(0, clip_length, 120):
        # Set the times at which the frequencies should be inserted
        times = [start_min + 10, start_min + ones*10 + 10, start_min + tens*10 + 10, start_min + hundreds*10 + 10, start_min + thousands*10 + 10]  # in seconds

        for frequency, start_time in zip(frequencies, times):
            # Generate the time array for the sine wave
            end_time = start_time + sine_duration  # end time in seconds
            time = np.arange(start_time, end_time, 1/rate)

            # Generate the sine wave
            sine_wave = np.sin(2 * np.pi * (frequency) * time)

            # Apply a window function to the sine wave
            window = np.hanning(len(sine_wave))
            sine_wave = sine_wave * window

            # Normalize sine wave to match original data amplitude
            sine_wave = sine_wave * np.max(np.abs(data))
            print(index, start_time, end_time)

            # Calculate the start and end indices in the data array
            start_index = int(start_time * rate)
            end_index = int(end_time * rate)

            # Make sure the end_index does not exceed the data
            if end_index > len(data):
                end_index = len(data)

            # Mix the original data with the sine wave
            data[start_index:end_index] += sine_wave[:end_index - start_index].astype(data.dtype)

    # Write the result to a new wav file
    out = "C:\\Users\\om\\Desktop\\anti piracy\\first prototype\\sample" + str(index) + ".wav"
    write(out, rate, data)




# import numpy as np
# from scipy.io.wavfile import read, write

# # read the wav file
# for index in range(468,469):
#     path = "C:\\Users\\om\\Desktop\\anti piracy\\first prototype\\main.wav"   
#     rate, data = read(path)

#     # Make sure it's mono by taking the first channel only
#     if len(data.shape) > 1:
#         data = data[:, 0]
#     ones = index%10
#     tens = (index//10)%10
#     hundreds = (index//100)%10
#     thousands = 11
    
#     if ones == 0 or tens == 0 or hundreds == 0 or thousands == 0:
#         continue
#     if ones == tens or ones == hundreds or ones == thousands or tens == hundreds or tens == thousands or hundreds == thousands:
#         continue
#     # Specify the frequencies and times at which they should be inserted
#     frequencies = [20000, 20500, 21000, 21500, 22000]  # in Hz
#     times = [10, ones*10 + 10, tens*10 + 10, hundreds*10 + 10, thousands*10 + 10]  # in seconds
#     sine_duration = 0.005  # duration of sine wave in seconds

#     for frequency, start_time in zip(frequencies, times):
#         # Generate the time array for the sine wave
#         end_time = start_time + sine_duration  # end time in seconds
#         time = np.arange(start_time, end_time, 1/rate)

#         # Generate the sine wave
#         sine_wave = np.sin(2 * np.pi * frequency * time)

#         # Apply a window function to the sine wave
#         window = np.hanning(len(sine_wave))
#         sine_wave = sine_wave * window

#         # Normalize sine wave to match original data amplitude
#         sine_wave = sine_wave * np.max(np.abs(data))
#         print(index, start_time, end_time)
#         # Calculate the start and end indices in the data array
#         start_index = int(start_time * rate)
#         end_index = int(end_time * rate)

#         # Make sure the end_index does not exceed the data length
#         if end_index > len(data):
#             end_index = len(data)

#         # Mix the original data with the sine wave
#         data[start_index:end_index] += sine_wave[:end_index - start_index].astype(data.dtype)

#     # Write the result to a new wav file
#     out = "C:\\Users\\om\\Desktop\\anti piracy\\first prototype\\sample" + str(index) + ".wav"
#     write(out, rate, data)
