import numpy as np
import matplotlib.pyplot as plt

def nrz_l_encoding(data):
    """NRZ-L encoding: 0 → 0, 1 → 1"""
    encoded_signal = []
    for bit in data:
        encoded_signal.extend([int(bit), int(bit)])
    return encoded_signal

def nrz_i_encoding(data):
    """NRZ-I encoding: 0 → No change, 1 → Invert"""
    encoded_signal = []
    current_level = 0
    for bit in data:
        if bit == '1':
            current_level = 1 if current_level == 0 else 0
        encoded_signal.extend([current_level, current_level])
    return encoded_signal

def plot_encoding(data, nrz_l_signal, nrz_i_signal):
    plt.figure(figsize=(12, 8))
    
    time = np.arange(0, len(nrz_l_signal))
    
    # Original Data
    plt.subplot(3, 1, 1)
    plt.title('Original Data')
    plt.ylim(-0.5, 1.5)
    plt.yticks([0, 1], ['0', '1'])
    plt.xticks(range(len(data)), data, fontsize=10)
    plt.xlabel('Bit Position')
    plt.ylabel('Bit Value')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.step(range(len(data)), [int(bit) for bit in data], where='post', linewidth=2, color='black')
    for i, bit in enumerate(data):
        plt.text(i+0.5, -0.3, bit, horizontalalignment='center', fontsize=10)
    
    # NRZ-L
    plt.subplot(3, 1, 2)
    plt.title('NRZ-L Encoding')
    plt.ylim(-0.5, 1.5)
    plt.yticks([0, 1], ['Low', 'High'])
    plt.xticks(range(0, len(nrz_l_signal), 2), data, fontsize=10)
    plt.xlabel('Time')
    plt.ylabel('Signal Level')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.step(time, nrz_l_signal, where='post', linewidth=2, color='blue')
    for i, bit in enumerate(data):
        plt.text((i * 2)+1, -0.3, bit, horizontalalignment='center', fontsize=10)
    
    # NRZ-I
    plt.subplot(3, 1, 3)
    plt.title('NRZ-I Encoding')
    plt.ylim(-0.5, 1.5)
    plt.yticks([0, 1], ['Low', 'High'])
    plt.xticks(range(0, len(nrz_i_signal), 2), data, fontsize=10)
    plt.xlabel('Time')
    plt.ylabel('Signal Level')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.step(time, nrz_i_signal, where='post', linewidth=2, color='red')
    for i, bit in enumerate(data):
        plt.text((i * 2)+1, -0.3, bit, horizontalalignment='center', fontsize=10)
    
    plt.tight_layout()
    plt.show()

def main():
    while True:
        data = input("Enter a binary string (e.g., 10110): ")
        data += "0"
        if all(bit in '01' for bit in data):
            break
        print("Invalid input. Please enter only 0s and 1s.")
    
    nrz_l_signal = nrz_l_encoding(data)
    nrz_i_signal = nrz_i_encoding(data)
    plot_encoding(data, nrz_l_signal, nrz_i_signal)

if __name__ == "__main__":
    main()
