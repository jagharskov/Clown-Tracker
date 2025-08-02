## A simple python script for fetching and outputting viewer numbers from a twitch page in real time. Created in order to make it easier to analyze viewer number inconsistencies, without relying on on websites like _Twitchtracker_ or _Streamscharts_ that only poll viewer numbers every 10 to 20 minutes.

<img width="2487" height="956" alt="image" src="https://github.com/user-attachments/assets/77062ccc-f292-44d1-8842-e8422ddae987" />

## Installating prerequisits:
```
pip install -r requirements.txt
```
The script also uses a headless Firefox process, you will need Firefox on your computer.

## How to use:
Change the __CHANNEL_NAME__ variable in _ClownTracker.py_ to the twitch channel of your choice. Only enter the channel name, not the full URL.
Finally run the script with:
```
python ClownTracker.py
```


