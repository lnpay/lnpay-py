import lnpay_py
from lnpay_py.wallet import LNPayWallet
from lnpay_py.lntx import LNPayLnTx

# Set your public key & wallet key
lnpay_api_key = 'pak_ZA7N6YoXEXwreG3ibKzaTWQQYuEmJL'
lnpay_wallet_key = 'wa_gJvYs6TIjsL2t9iRoNm8oQpm'

# init lnpay
lnpay = lnpay_py.initialize(lnpay_api_key)

# Create a wallet
print('Creating a new wallet....')
wallet_params = {
    'user_label': 'My wallet'
}
new_wallet = lnpay_py.create_wallet(wallet_params)
print(new_wallet)

# Instantiate a Wallet
my_wallet = LNPayWallet(lnpay_wallet_key)

# Check balance
print('Checking balance...')
my_wallet = LNPayWallet(lnpay_wallet_key)
info = my_wallet.get_info()
print(info)

# get transactions
print('Getting transactions...')
my_wallet = LNPayWallet(lnpay_wallet_key)
transactions = my_wallet.get_transactions()
print(transactions)

# create invoice
print('Creating invoice...')
my_wallet = LNPayWallet(lnpay_wallet_key)
invoice_params = {
    'num_satoshis': 2,
    'memo': 'Tester'
}
invoice = my_wallet.create_invoice(invoice_params)
print(invoice)

# pay invoice
"""
print('Paying invoice...')
my_wallet = LNPayWallet(lnpay_wallet_key)
invoice_params = {
    'payment_request': 'lnbc....'
}
pay_result = my_wallet.pay_invoice(invoice_params)
print(pay_result)
"""

# transfer to internal wallet
"""
print('Transfering to internal wallet...')
my_wallet = LNPayWallet(lnpay_wallet_key)
transfer_params = {
    'dest_wallet_id': 'w_XXX',
    'num_satoshis': 1,
    'memo': 'Transfer Memo'
}
transfer_result = my_wallet.internal_transfer(transfer_params)
print(transfer_result)
"""

# Get lnurl link
print('Getting lnurl link...')
my_wallet = LNPayWallet(lnpay_wallet_key)
lnurl_params = {
    'num_satoshis': 1,
    'memo': 'SatsBack!'
}
lnurl_link = my_wallet.get_lnurl(lnurl_params)
print(lnurl_link)

# Check if ln invoice is settled
"""
print('Checking ln invoice...')
lntx_id = 'lntx_XXX'
ln_tx = LNPayLnTx(lntx_id)
invoice_result = ln_tx.get_info()
print(invoice_result)
"""
