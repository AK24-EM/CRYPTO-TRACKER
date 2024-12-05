import tkinter as tk
import requests

class cryptocurrency_tracker:
    def __init__(self , root , api_keys):
        self.root = root
        self.api_keys = api_keys
        self.root.title("Crypto Tracker")
        self.create_widgets()

    def create_widgets(self):
        self.clear()
        tk.Label(self.root , text ="enter the currency your are looking for").pack(pady=5)
        self.crypto_entry = tk.Entry(self.root)
        self.crypto_entry.pack(pady=5)
        tk.Button(self.root , text = "check result" , command=self.crypto_market).pack(pady=5)
        self.panel_entry = tk.Label(self.root , text="")
        self.panel_entry.pack(pady=5)
        tk.Button(self.root , text="back" , command =self.create_widgets).pack(pady=5)

    def crypto_market(self):
        symbol = self.crypto_entry.get().upper()
        url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={symbol}"
        headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": self.api_keys,
        }

        try:
            responses = requests.get(url , headers=headers)
            responses.raise_for_status()
            data = responses.json()
            if symbol in data["data"]:
                price = data["data"][symbol]["quote"]["USD"]["price"]
                market_cap = data["data"][symbol]["quote"]["USD"]["market_cap"]
                result = f"Price: ${price:.2f}\nMarket Cap: ${market_cap:.2f}"
            else:
                result = "Cryptocurrency not found!"
        except Exception as e:
            result = f"Error: {e}"

        self.panel_entry.config(text=result)

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    api_keys = "6581ada7-a389-4435-8e4c-283977fe8240"
    app = cryptocurrency_tracker(root , api_keys)
    root.mainloop()






