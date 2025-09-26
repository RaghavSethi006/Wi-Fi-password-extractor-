Wi-Fi Password Extractor

This Python script extracts all saved Wi-Fi SSIDs and their passwords from a Windows machine and stores them in a .csv file with a timestamp.

⚡ Features

Retrieves all Wi-Fi profiles stored on your Windows PC.

Extracts SSID (Wi-Fi name) and password (if available).

Saves results into a passwords/ folder as a CSV file.

Filenames are timestamped (YYYY-MM-DD-HH-MM-SS.csv).

🛠 Requirements

Python 3.7+

Windows OS (uses netsh command, not compatible with macOS/Linux).

After execution:

Extracted Wi-Fi credentials are printed in the terminal.

A .csv file is saved inside the passwords/ folder with format:

SSID	Password
MyHomeWiFi	mypassword123
CoffeeShop	coffee@123
OfficeWiFi	None (if empty)
