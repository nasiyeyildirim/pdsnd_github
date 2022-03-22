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
    city = input("Write the City Name:").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("You can only choose chicago, new york city or washington:").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month= input("Write the Month:").lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month =input("You can only choose all, january, february, march, april, may or june:").lower()
      

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Write day:").lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day =input("You can only choose all, monday, tuesday, ... sunday:").lower()
    


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
       

    #axtract day of week from the Start Time column to create a day of week column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df
        


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is:" ,df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("The most common day of week is:" ,df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print("The most common start hour is:", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is:", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most commonly used end station is:", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    sses = df['Start Station'] + '-' + df['End Station']
    print("The most commonly used frequent combination of start station and end station trip is:", sses.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time in hour is:", df['Trip Duration'].sum()/3600)

    # TO DO: display mean travel time
    print("The mean travel time in hour is:", df['Trip Duration'].sum()/3600)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender
    
    
    if "Gender" in df.columns:
        user_gender = df['Gender'].value_counts()
        print(user_gender)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        ey = int(df['Birth Year'].min())
        mr = int(df['Birth Year'].max())
        cy = int(df['Birth Year'].mode()[0])
        print("Earliest year of birtht is {}, most recent year of birth is {} and most common year of birth is {}".format('ey', 'mr','cy'))
    else:
        print('Birth year does not defined for Washington!')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data (df):
    #TO DO: ask to the user they woud like to view 5 rows of individual trip data
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    start_loc = 0
    while view_data == 'yes' and start_loc+5<df.shape[0]:
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        display_data = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
