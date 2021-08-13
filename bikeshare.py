import time
import pandas as pd
import numpy as np

CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'wa': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please select one of the following cities :\n- ch for Chicago\n- ny for New York City \n- wa for Washington \n ").lower()
    while city not in CITY_DATA.keys() :
        print("Sorry the city you selected is not in the data or wrong typing,\nPlease try again")
        city = input("Please select one of the following cities :\n- ch for Chicago\n- ny for New York City \n- wa for Washington\n ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please chose one month for filtering or 'all' for all months:\n- january \n- february \n- march \n- april \n- may \n- june \n- all\n ").lower()
    months = ['january','february','march','april','may','june','all']
    while month not in months :
        print("Sorry invalid month,Please try again")
        month = input("Please chose one month for filtering or 'all' for all months:\n- january \n- february \n- march \n- april \n- may \n- june \n- all\n ").lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please chose one day for filtering or 'all' for all days:\n- monday \n- tuesday \n- wednesday \n- thursday \n- friday \n- saturday \n- sunday \n- all \n").lower()
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while day not in days :
        print("Sorry invalid day, Please try again")
        day = input("Please chose one day for filtering or 'all' for all days:\n- monday \n- tuesday \n- wednesday \n- thursday \n- friday \n- saturday \n- sunday \n- all \n").lower()

    print('-'*40)
    return city,month,day

def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data file into a DataFrame according to City
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day Of Week'] = df['Start Time'].dt.day_name()
    # filter by month and day if applicable
    if month != 'all':
        df = df[df['Month'] == month.title()]
    if day != 'all' :
        df = df[df['Day Of Week'] == day.title()]


    return df

def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    while month == 'all':
        most_common_month = df['Month'].mode()[0]
        print("The most common Month: ",most_common_month)
        break

    # TO DO: display the most common day of week
    while day == 'all':
        most_common_day = df['Day Of Week'].mode()[0]
        print("The most common Day in month ({}): ".format(month).title(), most_common_day)
        break

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['Hour'].mode()[0]
    print("the most common start hour in month ({}) & on day ({}): ".format(month,day).title(),most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common Start Station: ',most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common End Station: ',most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' To ' + df["End Station"]
    most_common_trip = df['Trip'].mode()[0]
    print('The most common Trip is from ',most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_tarvel_time = sum(df['Trip Duration'])
    print('Total travel time: {} seconds'.format(total_tarvel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The averange travel time: {} seconds'.format(mean_travel_time) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nCount of each user type:\n',user_types)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\nCount of each Gender:\n',gender_count)
    except KeyError :
        print('\nSorry, no available Gender data for Washington')



    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = df['Birth Year'].min()
        print('\nThe earliest year of birth: ',earliest_birth)
        recent_birth = df['Birth Year'].max()
        print('The most recent year of birth: ',recent_birth)
        most_common_year_birth = df['Birth Year'].mode()[0]
        print('The most common year of birth: ',most_common_year_birth)
    except KeyError:
        print('\nSorry, no available BIRTH YEAR data for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_resource_data(df):
    """ Depend on user choice the function display 5 raw by 5 raw from the dataframe"""

    print('\nThe resource data is available to check... \n')
    start_look = 0
    while True:
        display_opt = input('To View the resource data, 5 rows by 5 rows type: Yes or No for Exiting \n').lower()
        if display_opt not in ['yes', 'no']:
            print('That\'s invalid choice, pleas type: yes or no')

        elif display_opt == 'yes':
            print(df.iloc[start_look:start_look+5])
            start_look+=5

        elif display_opt == 'no':
            print('\nThank You......\nExiting......')
            break

def main():
    while True:
        city,month,day = get_filters()
        print('The filter choices are: ',city,month,day)
        print('-'*40)

        df = load_data(city,month,day)
        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_resource_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
