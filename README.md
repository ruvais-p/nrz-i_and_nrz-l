# NRZ Encoding Visualizer

This Python script visualizes **Non-Return-to-Zero Level (NRZ-L)** and **Non-Return-to-Zero Inverted (NRZ-I)** encoding for a given binary input.

## Features
- Accepts a user-input binary string.
- Implements **NRZ-L encoding** (0 → Low, 1 → High).
- Implements **NRZ-I encoding** (0 → No change, 1 → Invert).
- Generates a graphical representation of the original data, NRZ-L signal, and NRZ-I signal using `matplotlib`.

## Prerequisites
Make sure you have Python installed along with the following dependencies:

```bash
pip install numpy matplotlib
```

## Usage
Run the script and enter a binary string when prompted:

```bash
python nrz_encoding.py
```

### Example Input
```
Enter a binary string (e.g., 10110): 1011
```

### Output
- A **matplotlib plot** displaying:
  - Original data.
  - NRZ-L encoding.
  - NRZ-I encoding.

## Code Breakdown
- `nrz_l_encoding(data)`: Implements NRZ-L encoding.
- `nrz_i_encoding(data)`: Implements NRZ-I encoding.
- `plot_encoding(data, nrz_l_signal, nrz_i_signal)`: Generates a plot.
- `main()`: Handles user input and function calls.

---

Happy coding! 🚀

