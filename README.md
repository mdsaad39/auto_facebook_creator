# Auto Facebook  Creator

Create Facebook accounts with randomized profiles using Python and the Tor Browser for anonymity.

## Overview

This Python project automates Facebook account creation with unique profiles. It leverages Python scripts, web scraping, and browser automation for this purpose.

## Prerequisites

Before diving into this project, ensure the following prerequisites are in place:

1. **Folder Structure:** Your project folder should have the following structure:
   - `run_multiple_process.py`
   - `create_algerian_facebook_account.py`
   - `Tor Browser/` (Tor Browser installation)
   - `lastNames.csv`
   - `bb/` and `ww/` directories (with CSV files)

   **Note:** Please place your Tor Browser installation in the same directory as your project files.

2. **Dependencies:** Install required Python libraries using pip:

   ```bash
   pip install selenium beautifulsoup4 pyautogui names passwordgenerator

## Usage

To utilize this project, follow these steps:

Execute run_multiple_process.py to create multiple Facebook accounts with randomized profiles (or execute create_algerian_facebook_account.py if you need only to create one facebook account).

The create_algerian_facebook_account.py script generates random profile details, including email (from online fake email provider website (https://www.fakemailgenerator.com/), you need to change the code if the website is no longer in service), password, names, and gender, by automating the Facebook registration page.

Tor Browser is used for anonymity during the account creation process.
## Customization
You can customize the project by modifying create_algerian_facebook_account.py, allowing you to adjust profile information generation or use different email services.

## License
This project is open-source and available under the MIT License.


