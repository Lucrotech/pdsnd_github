import time
import pandas as pd
import numpy as np
import sys
import os

CITY_DATA = {'chicago':'chicago.csv',
             'new york':'new_york_city.csv',
             'washington':'washington.csv'}
    """
    The above data to be pulled via API in the future.
    """

def get_user_input():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter
        (str) day - name of the day of week to filter
    """
    print('Hello! Let\'s explore some US Bikeshare data!')
  
    #get user input for city (chicago, new york, washington)
    city = input('For which city would you like to see data? Pick Chicago, New York, or Washington? Note that it must all be typed in lower case.').lower()
    
    #get user input for month (all, january, february, ... , june)
    month = input('For which month would you like to see data? Pick a month - January, February, March, April, May, or June? Note that it must all be typed in lower case.').lower()
    
    #get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day of the weeks data would you like to see? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday? Note that it must all be typed in lower case.').lower()
    
    return city, month, day

def display_data(city, month, day):
    """
    The data displayed according to city name and filtered by month and day.

    """
    try:
        df = pd.read_csv(CITY_DATA[city])

        df['Start Time'] = pd.to_datetime(df['Start Time'])
    
        df['month'] = df['Start Time'].dt.month
    
        df['day_of_week'] = df['Start Time'].dt.weekday_name
    
        if month != 'all':
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month)+1
    
        df = df[df['month'] == month]
    
        if day != all:
            df = df[df['day_of_week'] == day.title()]
            
        return df

    except:
        print('\n Please type in valid city name, month, and day! Note that it must all be typed in lower case.\n')
            
def pop_times_to_rent(df, month):
    """
    Show the most popular rental periods .

    """    
    print('We are getting your data ready!')
        
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['hour'] = df['Start Time'].dt.hour
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    #display the most common month
    print('What is the most common month for users to use the bicycles?')
    print(month)
    
    #display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('What is the most common day for bicycles to be used?')
    print(popular_day_of_week)
           
    #display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('What is the most popular hour of the day to use a rental bicycle?')
    print(popular_hour)
         
def pop_stations_tp(df):
    """
    Displays the most popular bicycle pickup destination.

    """
    print('We are getting your data ready!')    
    #display the most common start station
    pop_start_stations = df['Start Station'].mode()[0]
    print('What was the most popular bicycle pickup destination?')
    print(pop_start_stations)
    
    #display the most common end station
    pop_end_stations = df['End Station'].mode()[0]
    print('What was the most popular bicycle dropoff destination?')
    print(pop_end_stations)
       
    #display the most common trip from start to end station
    tp_start_end_value = df['Start Station']+"_"+df['End Station']
    pop_trip_start_end = tp_start_end_value.mode()[0]
    print('What was the most popular trip based on pickup and dropoff destinations?')
    print(pop_trip_start_end)
     

def tp_duration(df):
    """
    Display duration of rentals in seconds.

    """
    print('We are fetching and compiling all your data. . .')
    tp_duration = df['Trip Duration']
    
    #display the Total travel time
    print('What was the total time per rental (in seconds)?')
    print(tp_duration.sum())
    
    #display the Average travel time
    print('What was the average time that a rental client spends on each trip (in seconds)?')
    print(tp_duration.mean())
      
def info_user(df, city):
    """
    Displays rental client statistics.
     
    """
    print('We are fetching and compiling all your data. . .')  
    #display the count of each user type
    usr_types_count = df['User Type'].value_counts()
    print('What is the breakdown of rental clients?')
    print(usr_types_count)
    
    if city != 'washington':
        #display the count of each gender
        gen_count = df['Gender'].value_counts()
        print('What is the gender breakdown by sex?')
        print(gen_count)
    else:
        print('Unfortunately we dont have any gender related data to share.')
        
    if city != 'washington':
        #display the earliest year of birth
        bd_youngest = df['Birth Year'].max()
        print('In what year was the youngest rental client born?')
        print(int(bd_youngest))
    
        #display the recent year of birth
        bd_oldest = df['Birth Year'].min()
        print('In what year was the oldest rental client born?')
        print(int(bd_oldest))
    
        #display the most common year of birth
        pop_year = df['Birth Year'].mode()[0]
        print('In which year was the majority of rental clients born?')
        print(int(pop_year))
    else:
        print('Unfortunately we dont have any date of birth related data to share')
        print('-'*50)
 
def main(df_user_input,month,city):
    pop_times_to_rent(df_user_input, month)
    pop_stations_tp(df_user_input)
    tp_duration(df_user_input)
    info_user(df_user_input, city)
    print('-'*50)
            
def restart_program():
    """
    Application user promted request to restart the application. 
    
    """
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
if __name__ == "__main__":
    city_option, month_option, day_input = get_user_input()
    df_user_input = display_data(city_option, month_option, day_input)
    
    if df_user_input is None:
        print('Exception applies if Data Frame can not be compiled with the arguments acquired through the users imput.')
        print('-'*50)
    else:    
        main(df_user_input,month_option,city_option)
        
        raw_data_input = input('Would you like to see some of the raw data? The data will be displayed in batches of 10 lines. Enter yes or no.').lower()
        index_start = 0
        index_end = 10
        while raw_data_input == 'yes':
            print(df_user_input.iloc[index_start:index_end])
            print('\n')
            raw_data_input = input('Would you like to see the following 10 lines of raw data? Enter yes or no.').lower()
            index_start=index_end
            index_end += 10
        
        print('\n')
        restart_input = input('Would you like to restart this application? Enter yes or no.').lower()
        if restart_input == 'yes':
            restart_program()
            print('\n')
        elif restart_input != 'no':
            print('Please enter yes or no! Note that you should be typing in lower case.')