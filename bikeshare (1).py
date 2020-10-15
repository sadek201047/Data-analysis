import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter city: chicago, new york city, washington: ')
    while city.lower() not in ['chicago', 'new york city', 'washington']:
        city = input('Enter correct city: chicago, new york city, washington: ')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter month: All, January, Febraury, ....., June:  ')
    while month.lower() not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('''Enter correct month january, february, march, april, may, june: ''')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('day of week (All, Monday, Tuesday,... Sunday): ')
    while day.lower() not in ['all', 'monday', 'tuesday', 'Wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('Enter correct day All, Monday, Tuesday,... sunday): ')
        
        
    if month == 'all':
         month = ''
    if day == 'all':
         day = ''
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    ' use dictionary call from city_data dictionary'
    df = pd.read_csv(CITY_DATA.get(city))
    
    '''convert Start Time column in data frame from string format to date&time format to change the date formate from numbers to letters
     for easier filtering by month or day'''
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    'change the date formate from standard 10-06-2020 12:00 to string format like Monday-May-2020-23:00'
    df['Start Time'] = df['Start Time'][0:].map(lambda ts: ts.strftime("%A-%B-%Y-%H"))
    
    'apply filters by month and day on Start time column on data frame df'
    df = df[(df['Start Time'].str.contains(month, case=False)) & (df['Start Time'].str.contains(day, case=False))]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    'Splitted Start Time column with the its new format by splitter - to four columns named as below to perform calculations on every column'
    df[['day', 'month', 'year', 'hour']] = df['Start Time'].str.split("-",expand=True,)
    # TO DO: display the most common month
    print('most common month', df['month'].mode())

    # TO DO: display the most common day of week
    print('most common day', df['day'].mode())

    # TO DO: display the most common start hour
    print("most common start hour.", df['hour'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most commonly used start station', df['Start Station'].mode())

    # TO DO: display most commonly used end station
    print('most commonly used start station', df['End Station'].mode())

    # TO DO: display most frequent combination of start station and end station trip
    stations = df['Start Station'] + df['End Station']
    print('most frequent combination of start station and end station trip', stations.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('mean travel time', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types', df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if 'Gender' in df:
         print('Display counts of gender', df['Gender'].value_counts())
         
               
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
         print('young Birth Year', df['Birth Year'].max())
         print('oldest Birth Year', df['Birth Year'].min())
         print('common birth year', df['Birth Year'].mode()) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
def view_raw_data(df):
    view_data = input('would you like to see raw data yes or no: ')
    counter = 0
    while view_data.lower() == 'yes':
            print(df.iloc[counter:counter + 5])
            counter =  counter + 5
            view_data = input('would you like to see raw data yes or no: ')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_raw_data(df)
        
        
            
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
