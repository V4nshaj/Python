# currency converter using tkinter

from tkinter import *
from tkinter import ttk
currencyNameList = ["USD", "INR", "GBP", "CAD", "JPY", "CNY", "INR", "AUD", "NZD", "CHF", "SGD", "SEK", "DKK", "NOK", "KRW", "MXN", "ZAR", "BRL", "RUB", "TRY", "CZK", "PLN", "PHP", "RON", "HUF", "MYR", "IDR", "ILS", "BGN", "HRK", "THB", "ISK", "CLP", "PKR", "BHD", "VND", "LKR", "TWD", "SAR", "RSD", "KWD", "JOD", "OMR", "QAR", "KZT", "KGS", "UAH", "TMT", "COP", "KES", "LAK", "TJS", "UZS", "MNT", "MVR", "NPR", "PYG", "BND", "KHR", "VUV", "FJD", "BDT", "KZT", "LBP", "JMD", "LYD", "MAD", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CDF", "CHF", "CLP", "CNH", "CNY", "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "EUR"]
root = Tk()
root.title("Converter")
frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
welcomeLabel = ttk.Label(frame, text="Welcome to Currency Converter",background="blue",foreground="white")
welcomeLabel.grid(column=0, row=0, sticky=N,columnspan=3)
conversionRateLabel = ttk.Label(frame, text="1 USD = 74.93 INR")
conversionRateLabel.grid(column=1, row=1, sticky=N)
dateLabel = ttk.Label(frame, text="2020-07-22")
dateLabel.grid(column=1, row=2, sticky=N)
fromCurrencyDropDown = ttk.Combobox(frame, values=currencyNameList)
fromCurrencyDropDown.grid(column=0, row=3, sticky=(W, E))
fromCurrencyDropDown.current(0)
toCurrencyDropDown = ttk.Combobox(frame, values=currencyNameList)
toCurrencyDropDown.grid(column=2, row=3, sticky=(W, E))
toCurrencyDropDown.current(1)
fromAmount = ttk.Entry(frame)
fromAmount.grid(column=0, row=4, sticky=(W, E))
toAmount = ttk.Entry(frame)
toAmount.grid(column=2, row=4, sticky=(W, E))
convertButton = ttk.Button(frame, text="Convert")
convertButton.grid(column=1, row=5, sticky=(W, E))


root.mainloop()