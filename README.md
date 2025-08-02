## A simple python script for fetching and outputting viewer numbers from a twitch page in real time. Created in order to make it easier to analyze viewer number inconsistencies, without relying on on websites like _Twitchtracker_ or _Streamscharts_ that only poll viewer numbers every 10 to 20 minutes.

<img width="2487" height="956" alt="image" src="https://github.com/user-attachments/assets/77062ccc-f292-44d1-8842-e8422ddae987" />

## Installating prerequisites:
```
pip install -r requirements.txt
```
This script uses a headless Firefox process via Selenium. You will need to have Firefox installed on your system.

## How to use:
Run ClownTracker.py with the channel name as an argument. Do not use the full URL. Example:
```
python ClownTracker.py quin69
```
A _viewer_data_ folder will be created inside the script's directory, where viewer data will be saved continuously to a .csv file.
