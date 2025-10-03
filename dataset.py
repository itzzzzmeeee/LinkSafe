import pandas as pd

urls = [
    ("http://secure-paypal.com@malicious.com", "phishing"),
    ("https://www.google.com", "legitimate"),
    ("http://login-facebook.com.fake.com", "phishing"),
    ("https://www.amazon.com", "legitimate"),
    ("http://verify-bank-account.com", "phishing"),
    ("https://www.microsoft.com", "legitimate")
]

df = pd.DataFrame(urls, columns=["url", "label"])
df.to_csv("urls_dataset.csv", index=False)
print("urls_dataset.csv created successfully!")
