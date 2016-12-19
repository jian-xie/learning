# Implementation Details

## Data
### Download Data
#### Countires or regions:
GBP, EUR, JPY, AUD, CAD, US

#### What:
- ALL:
Currency Rate, Main Equity Index, Government Bond Yield of 2, 5 and 10 years,
CPI, GDP, Unemployment Rate

- US:
Non-farm payroll, Expected CPI in 1 year, Expected unemployment rate in 1 year

### Data Change
#### outright value to changes
Government Bond Yield of 2, 5 and 10 years,
CPI, GDP, Non-farm payroll, Expected CPI in 1 year, Expected unemployment rate in 1 year


#### outright value to percentage changes
Currency Rate, Main Equity Index,Unemployment Rate

### Normalize Data
Used Min-Max normaliztion to normalize all the data to the range from 0 to 1.

### Training Data
- X:
Get samples by rolling the data from start date to end date, in a given a rolling window.
For example, samples:

    **`1990-01-01:1991-01-01`**

 **`1990-02-01:1991-02-01`**

 **`...`**

 **`2010-11-01:2010-12-01`**

- Y:
We are trying to predict **US Goverment Bond Yield 10 Years**'s change in next data point.

    **`goes up  : [0, 0, 1]`**

    **`not move : [0, 1, 0]`**

    **`goes down: [1, 0, 0]`**

## Model

- Put inputs into groups by countries. Used 5 inputs groups, each of them learned by a LSTM layer

- Merge 5 inputs layers and connect to next lever layer

- Stack 2 layers of LSTM

- Add a drop out layer to regulization

- Add one layer of fully connected network

- Output layer

## Results

loss: 1.1371 - acc: 0.2900 - val_loss: 0.8221 - val_acc: 0.4757

loss: 0.8364 - acc: 0.5281 - val_loss: 0.7361 - val_acc: 0.5243

loss: 0.7860 - acc: 0.4675 - val_loss: 0.7261 - val_acc: 0.4757

loss: 0.7519 - acc: 0.4978 - val_loss: 0.7111 - val_acc: 0.4757

loss: 0.7466 - acc: 0.5281 - val_loss: 0.7057 - val_acc: 0.4757

loss: 0.7528 - acc: 0.5195 - val_loss: 0.7068 - val_acc: 0.4757

loss: 0.7528 - acc: 0.4632 - val_loss: 0.7027 - val_acc: 0.4757

loss: 0.7662 - acc: 0.4589 - val_loss: 0.7019 - val_acc: 0.4757

loss: 0.7532 - acc: 0.5065 - val_loss: 0.7053 - val_acc: 0.4757

loss: 0.7395 - acc: 0.5455 - val_loss: 0.6992 - val_acc: 0.4757

