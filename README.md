[![PyPI version](https://badge.fury.io/py/lnpay-py.svg)](https://badge.fury.io/py/lnpay-py)


# lnpay-py

LNPay Python SDK - at the moment a basic wrapper for the [LNPay API](https://docs.lnpay.co)

## Install
Get it on [pip](https://pypi.org)

```
pip install lnpay-py 
```

## Setup
First import into your python module

```python
import lnpay_py
```

Now, you need to instantiate it with a Public API Key from [LNPay.co](https://lnpay.co)

```python
# Set your public key
lnpay_api_key = 'pak_XXX'

# init lnpay
lnpay_py.initialize(lnpay_api_key)
```

## Usage - [Documentation](https://docs.lnpay.co)

The first alpha version of this SDK is mainly a wrapper for the [LNPay API](https://docs.lnpay.co)

Everyhing revolves around the _wallet_ and Wallet Access Keys (WAK) which grant various levels of permission.



### Instantiate a Wallet / Check Balance

When interacting with the wallet, import the wallet module and then initialize the wallet.

```python
from lnpay_py.wallet import LNPayWallet

my_wallet = LNPayWallet(lnpay_wallet_key)
```

Then you can proceed to check balance, etc.

```python
info = my_wallet.get_info()
print(info)
```

### Create a wallet

You can create a _wallet_ from the UI or via the API. When you create a wallet via the API, Wallet Access Keys (WAK) are returned. You need to save these.

```python
wallet_params = {
    'user_label': 'My wallet'
}
new_wallet = lnpay_py.create_wallet(wallet_params)
print(new_wallet)
```

### Generate Invoice

```python
my_wallet = LNPayWallet(lnpay_wallet_key)
invoice_params = {
    'num_satoshis': 2,
    'memo': 'Tester'
}
invoice = my_wallet.create_invoice(invoice_params)
print(invoice)
```

### Pay Invoice

```python
my_wallet = LNPayWallet(lnpay_wallet_key)
invoice_params = {
    'payment_request': 'lnbc....'
}
pay_result = my_wallet.pay_invoice(invoice_params)
print(pay_result)
```

### Transfers between wallets

```python
my_wallet = LNPayWallet(lnpay_wallet_key)
transfer_params = {
    'dest_wallet_id': 'w_XXX',
    'num_satoshis': 1,
    'memo': 'Transfer Memo'
}
transfer_result = my_wallet.internal_transfer(transfer_params)
print(transfer_result)
```

### Get Wallet Transactions

```python
my_wallet = LNPayWallet(lnpay_wallet_key)
transactions = my_wallet.get_transactions()
print(transactions)
```

### Get LNURL

```python
my_wallet = LNPayWallet(lnpay_wallet_key)
lnurl_params = {
    'num_satoshis': 1,
    'memo': 'SatsBack!'
}
lnurl_link = my_wallet.get_lnurl(lnurl_params)
print(lnurl_link)
```

### Get Invoice / Check if Settled

```python
lntx_id = 'lntx_XXX'
ln_tx = LNPayLnTx(lntx_id)
invoice_result = ln_tx.get_info()
print(invoice_result)
```

See [this example file](example/run.py)

Development
===========================

### 1. Installation
You will need to have [python](https://www.python.org/downloads/) installed as well as [pip](https://pip.pypa.io/en/stable/installing/)

Clone the repository

### 2. Getting started

* open the command line and switch into the project folder
* ```pip install -rrequirements.txt```
* ```python setup.py install```
* Edit & run the example file `python example/run.py`

### 3. Run Tests
```
./run_tests.sh
```

### 4. Publishing To Pypi
- Create an account for [pypi](https://pypi.org) & [pypi test](https://test.pypi.org)
- Install [twine](github.com/pypa/twine) - `pip install twine`
- Increment version in `__init__.py`
- Remove current items in dist - `rm -rf dist/*`
- Build package - `python setup.py install`
- Build sdist - `python setup.py sdist`
- Run pypi test upload - `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
- Upload to pypi - `twine upload --repository-url https://upload.pypi.org/legacy/ dist/*`
