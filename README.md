# Robo-Advisor Project

This program Automatic stock trading recommendations

instructions to help someone else install, setup, and run your program. This includes instructions for installing package dependencies, for example using Pip. It also includes instructions for setting an environment variable named ALPHAVANTAGE_API_KEY (see "Security Requirements" section below)


# Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

# Installation

Create a new repository on GitHub.com by the name of "shopping-cart-project" and clone or download the resulting repository onto your computer or to GitHub Desktop application. Then navigate there from the command line:

```sh
cd ~/Desktop/shopping-cart-project
```

> NOTE: subsequent usage and testing commands assume you are running them from the repository's root directory.

Use Anaconda to create and activate a new virtual environment, perhaps called "shopping_cart-env":

```sh
conda create -n shopping_cart-env python=3.7 # (first time only)
conda activate shopping_cart-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
pip install pytest
pip install python-dotenv
```

# Setup

1. Describe setup required for email receipts - SendGrid guidelines
2. Setup a .env file for the "secret" keys


## Usage

Run the recommendation script:

```py
python app/robo_advisor.py
```

Enter items from cart that you wish to buy or checkout when prompted to do so.

When finished enter "DONE" in the prompt. 

The program will display the total cost including tax and will prompt the user to "ACCEPT TRANSACTION" or "REJECT TRANSACTION." 

If the user enters "ACCEPT TRANSACTION", they will be prompted to "PRINT HARDCOPY RECEIPT" or "EMAIL RECEIPT."
    "PRINT HARD COPY RECEIPT" will display the receipt on the command line
    "EMAIL RECEIPT" will prompt the user to enter their email address and will send a soft copy to that email address and complete the transaction.

If the user enters "REJECT TRANSACTION", they will be prompted to check the list of items and make modifcations, either add or delete some items. Once complete the same original prompt will appear "ACCEPT TRANSACTION" or "REJECT TRANSACTION." 


## Testing

Install pytest (first time only):

```sh
pip install pytest
```

Run tests:

```sh
pytest

# or, skipping tests that issue network requests:
CI=true pytest
```

## [License](/LICENSE.md)






