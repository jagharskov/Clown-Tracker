## A simple python script for fetching and outputting viewer numbers from a twitch page in real time. Created in order to make it easier to analyze viewer number inconsistencies, without relying on on websites like _Twitchtracker_ or _Streamscharts_ that only poll viewer numbers every 10 to 20 minutes.

<img width="2487" height="956" alt="image" src="https://github.com/user-attachments/assets/77062ccc-f292-44d1-8842-e8422ddae987" />

## Installating prerequisites:
```
pip install -r requirements.txt
```
This script uses a headless Firefox browser via Selenium. You will need to have Firefox installed on your system.

## How to use:
Change the __CHANNEL_NAME__ variable in _ClownTracker.py_ to the twitch channel of your choice. Only enter the channel name, not the full URL.
Finally run the script with:
```
python ClownTracker.py
```
The script will create and continously store all information inside a .csv file inside it's home directory.

