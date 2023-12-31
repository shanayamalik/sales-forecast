# Sales Forecast Models

The `sales-forecast` repository contains machine learning models designed to predict sales based on historical data. The primary models used in this repository are AdaBoost and LSTM.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [AdaBoost Model](#adaboost-model)
  - [Training](#training)
  - [Inference](#inference)
- [LSTM Model](#lstm-model)
  - [Training](#training-1)
  - [Inference](#inference-1)
- [Support](#support)

## Overview

Sales forecasting is crucial for businesses to make informed decisions. This repository provides two distinct models to tackle the problem:

1. **AdaBoost**: A boosting algorithm that fits a sequence of weak learners on different weighted training data.
2. **LSTM (Long Short-Term Memory)**: A type of recurrent neural network (RNN) that can remember long-term dependencies.

## Prerequisites

1. Ensure you have Python installed on your machine. If not, download and install it from [Python's official website](https://www.python.org/downloads/).
2. Git, for cloning the repository.

## Setup

1. Clone the repository
   ```bash
   git clone https://github.com/shanayamalik/sales-forecast.git
   cd sales-forecast

## AdaBoost Model

**Training**
1. Navigate to the AdaBoost directory
      ```bash
      cd AdaBoost
3. Install the required packages
     ```bash
   pip install -r requirements.txt
6. Run the training script
      ```bash
      python Training.py
   
**Inference**
1. Ensure you are in the AdaBoost directory.
2. Run the inference script
      ```bash
      python Inference.py

## LSTM Model

**Training**
1. Navigate to the LSTM directory
      ```bash
      cd ../LSTM
3. Install the required packages
      ```bash
      pip install -r requirements.txt
5. Run the training script
      ```bash
      python Training.py
   
**Inference**
1. Ensure you are in the LSTM directory.
2. Run the inference script
      ```bash
      python Inference.py

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Support
For further details or any issues, refer to the repository's README or open an issue on GitHub.
