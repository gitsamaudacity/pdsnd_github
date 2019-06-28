
#make sure to import right python modules
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

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
    while True:
        city = input("\nPlease type in Chicaco,New York City or Washington\n").lower().title()
        if city not in ('Chicago','New York City','Washington'):
            print("Sorry,you wrote something wrong")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nPlease filter by January, February, March, April, May, June.Alternatively,type all if you cant choose one.\n").lower().title()
        if month not in('January', 'February', 'March', 'April', 'May', 'June', 'all'):
            print(" Sorry,wrong input")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nPlease choose a day:Monday,Tuesday, Wednesday, Thursday, Friday, Saturday,Sunday. Type all if there is no preference.\n").lower().title()
        if day not in ('Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday','all'):
            print('Sorry, you imput a wrong value')
            continue
        else:
            break

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
    #Use code from Practice Solution 3
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
         df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common Day of the Week:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip in seconds
    Combination_Station =     df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/3600, " Hours")

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types: \n',user_types)

    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types: \n',gender_types)
    except KeyError:
        print("\nGender Types:\nSorry,No data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nSorry,No data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nSorry,No data available for this month.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_separation(df):
    row_count = 0
    raw_data = input("\n Would you like to see the raw data used? Please write 'yes' or 'no' \n").lower()
    while True:
        if raw_data == 'no':
            return

        if raw_data == 'yes':
            print(df[row_count: row_count + 5])
            row_count += 5

        raw_data = input("\n Would you like to see five more rows of the data used to compute the stats? Please write 'yes' or 'no' \n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_separation(df)

#Allows code to be executed again

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
