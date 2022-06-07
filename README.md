# Scrap My LinkedIn

This project is meant for data obtention.
Using this tools, you can easly get the information you need with enough patience ^^'

## Summary
- [Requirements](#Requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Problems?](#problems)
- [Credits](#credits)

## Requirements

Many technologies are required. However, you will be able to install them easly following the [installation process](#installation).

| Technology |
|------------|
|Python 3.9 |
|Selenium |
|BeautifulSoup|
|Request|
|time|
|Chrome/Chromium|
|Chrome Selenium Driver|

Supported OS are:

|OS| Supported ? |
|--|------------|
|Fedora|   ✅ |
|Debian based|✅|
|Windows |⚠️ (WSL Advised)|

## Installation

In order to use the project, you will need the [Chrome](https://support.google.com/chrome/answer/95346?hl=fr&co=GENIE.Platform%3DDesktop)/[Chromium](https://www.chromium.org/getting-involved/download-chromium/) Browser.

Once the browse is installed, open a terminal and find the version of your browser.
For Chrome it will be:
```bash
google-chrome --version
```
And For Chromium:
```bash
chromium-browser --version
```

With that information you can now download the good version of the chrome driver need for selenium on this [link](https://chromedriver.chromium.org/downloads).

Put the file *chromedriver* that you just downloaded at the root of the repository, replacing the other file named the same way.
After that, you can launch the *installDriver* file using the following command:
```bash
./installDriver
```

Now, you need [**Python**](https://www.python.org/downloads/).
Once you are done installing python, you can launch the following command at the root of the repository:
```bash
./DownloadDependencies
```

## Usage

Before launching the project, you can enter your credentials of your linkedin account into the *credentials.json* file. Don't worry, if the credentials are invalid, the program will ask you again your credentials.

If everything is installed correctly, you can then use the following command to launch the project :
```bash
python3 main.py
```

Once the program is launched, the browser will ask you to *verify your indentity*.
You just need to resolve the puzzle and next, you will be asked informations in the terminal. Once you have given the informations, the script will begin to scrap.
**Don't close of minimize the window** if you don't want the scrapping to stop.
You can do something else meanwhile.

## Problems

It is possible for you to encounter some problems.
It can be caused by a **bad connection** or the fact that the window has been **minimized** or **closed**.

Also, it'll happen if you are not **premium** on linkedIn.The program will crash because the account reached the maximum profil search per month.

## Credits

#### Programation : Justin Duc
[![linkeding bage](https://img.shields.io/badge/-linkedin-0A66C2?logo=linkedin&style=for-the-badge)](https://www.linkedin.com/in/justin-duc-51b09b225/)
[![git hub bage](https://img.shields.io/badge/-GitHub-181717?logo=GitHub&style=for-the-badge)](https://github.com/Just1truc)
[![mail](https://img.shields.io/badge/-Mail-0078D4?logo=Microsoft-Outlook&style=for-the-badge)](mailto:justin.duc@epitech.eu)
