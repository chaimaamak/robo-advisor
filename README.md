# Robo-Advisor Project

This program is aimed at helping the user access current stock data by entering a ticker symbol. The ticker symbol must be valid. The information displayed is for recent highs and lows and close stock prices. There is also a recommendation portion to either buy or sell based on comparison with the recent average prices.


# Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

# Installation

Create a new repository on GitHub.com by the name of "Robo-Advisor Project" and clone or download the resulting repository onto your computer or to GitHub Desktop application. Or fork this repository under your own control. Then navigate there from the command line:

```sh
cd ~/Desktop/robo-advisor project  # or use the file path where you have saved the python file
```

> NOTE: subsequent usage and testing commands assume you are running them from the repository's root directory.

Use Anaconda to create and activate a new virtual environment, perhaps called "roboadvisor-env":

```sh
conda create -n roboadvisor-env python=3.7 # (first time only)
conda activate roboadvisor-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

# Setup

Before using or developing this application, take a moment to [obtain an AlphaVantage API Key](https://www.alphavantage.co/support/#api-key) (e.g. "abc123").

After obtaining the key, update the .env file with your secret key and ensure this .env file is ignored under the .gitignore file


## Usage

Run the recommendation script:

```py
python app/robo_advisor.py
```


## Testing

Install pytest (first time only):

```sh
pip install pytest
```

Run tests:

```sh
pytest  # no automated test configured in this code

# or, skipping tests that issue network requests:
CI=true pytest
```

## [License](/LICENSE.md)






