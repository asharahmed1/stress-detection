# Stress Detection with Physiological Data and Machine Learning

This repository contains the code for a machine learning-based stress detection system using physiological data. The project leverages the WESAD dataset, which includes measurements such as electrodermal activity (EDA), electromyography (EMG), and electrocardiography (ECG) from individuals completing various tasks.

The system is implemented across three Jupyter Notebooks:

1. **Notebook1.ipynb**: This notebook loads data from the WESAD dataset, specifically from subject "S2.pkl". It extracts indices for baseline and stress measurements, and creates dictionaries for EDA, EMG, and ECG data. The notebook then plots the EDA measurements for both baseline and stress conditions using `matplotlib.pyplot`.

2. **Notebook2.ipynb**: This notebook loads data from subject number 3 using a custom `DataManager` module. It extracts temperature, EDA, and ACC data from the baseline and stress tests. The temperature data is further processed by splitting it into windows and calculating features such as maximum, minimum, and dynamic range. The EDA data is also processed, and the standard deviation of EDA and temperature measurements are plotted for both baseline and stress conditions.

3. **Notebook3.ipynb**: This notebook performs a binary classification task on accelerometer data collected from a wearable device. It loads and preprocesses the data using the `DataManager` module, splits the data into training and test sets, and trains a Long Short-Term Memory (LSTM) neural network model using Keras. The input data is normalized using `MinMaxScaler` from scikit-learn to improve the model's performance. The notebook evaluates the model's performance on the test set.

## Repository Structure

```
stress-detection/
├── Notebook1.ipynb
├── Notebook2.ipynb
├── Notebook3.ipynb
├── DataManager.py
├── Demo.py
└── README.md
```

## Getting Started

To run this project, you'll need to have Python 3.x and the following libraries installed:

- numpy
- pandas
- matplotlib
- scikit-learn
- keras
- tensorflow

You can install these dependencies using pip:

```
pip install numpy pandas matplotlib scikit-learn keras tensorflow
```

Once you have the dependencies set up, you can run the Jupyter Notebooks in this repository to explore the code and the stress detection system.

## Future Work

There are several areas for improvement and future research that can be explored to enhance the performance and practical applications of the developed system:

1. Expanding the types of physiological data used for stress detection, such as heart rate variability (HRV), respiratory rate, and skin temperature.
2. Testing the model's generalizability on larger and more diverse datasets.
3. Exploring real-world applications in areas such as mental health, workplace safety, and sports performance.
4. Experimenting with additional machine learning algorithms and ensemble methods to improve the model's accuracy and robustness.
5. Developing more granular models that can identify different types and levels of stress.

Feel free to contribute to this project or use it as a starting point for your own stress detection research and development.
