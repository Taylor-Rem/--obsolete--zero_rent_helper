from datetime import datetime
import os

now = datetime.now()
day = now.day
month = now.month
year = now.year
username = "taylorremund"

months_of_the_year = {
    "1": "Jan",
    "2": "Feb",
    "3": "Mar",
    "4": "Apr",
    "5": "May",
    "6": "Jun",
    "7": "Jul",
    "8": "Aug",
    "9": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec",
}

path = f"/Users/{username}/Desktop/zero_rent_helper/{year}/{month}/{day}"
altpath = f"/Users/{username}/Desktop/zero_rent_helper/{year}/{month}"

if not os.path.exists(path):
    os.makedirs(path)

if not os.path.exists(altpath):
    os.makedirs(altpath)


file_name = os.listdir(path)[-1]
file_path = os.path.join(path, file_name)
