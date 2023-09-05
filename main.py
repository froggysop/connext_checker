import requests


with open('wallets.txt', 'r') as wallets_file:
    wallets = [line.strip().lower() for line in wallets_file]


with open('wallet_transfers.txt', 'w') as output_file:
    for wallet in wallets:
        url = f'https://postgrest.mainnet.connext.ninja/transfers?xcall_caller=eq.{wallet}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if len(data) > 0:
                output_file.write(f"Results for wallet: {wallet}\n")
                for item in data:
                    transfer_id = item.get('transfer_id', 'N/A')
                    output_file.write(f"Transfer ID: {transfer_id}\n")
                output_file.write("\n")
            else:
                output_file.write(f"No data found for wallet: {wallet}\n\n")
        else:
            output_file.write(f"Error fetching data for wallet: {wallet}\n\n")

print("Results have been saved to 'wallet_transfers.txt'.")
