from dateutil import parser
import pandas as pd
import read

df = read.load_data()

def extract_hour(datetime):
    return parser.parse(datetime).hour

def extract_day(datetime):
    return parser.parse(datetime).weekday() + 1

def top_hours():
    hours = df['submission_time'].apply(func=extract_hour)
    return hours.value_counts()

def top_days():
    days = df['submission_time'].apply(func=extract_day)
    return days.value_counts()
    
if __name__ == '__main__':
    print(top_days())