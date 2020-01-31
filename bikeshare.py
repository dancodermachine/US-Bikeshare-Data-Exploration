import time
import pandas as pd
import numpy as np

cities = ['ch', 'ny', 'wh']
months_year = [1, 2, 3, 4, 5, 6]
day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday', 'Sunday']
options = ['day', 'month']
answers = ['yes', 'no']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (int) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    error_message = "Please, enter a correct value: "
    a = "Would you like to see the data for Chicago (CH), New York (NY), or Washington (WH)? "
    b = "Which month? Please enter an integer that represents the month. Only the first six months are available (e.g. January = 1): "
    c = "Please, enter the day of the week you want e.g. Monday): "
    d = "Would you like to filter by day or by month?: "

    city = input(a).lower()
    while city not in cities:
        city = input(error_message).lower()

    option = input(d).lower()
    while option not in options:
        option = input(error_message).lower()

    if option == "month":
        day = None
        month = 13
        while month not in months_year:
            try:
                month = int(input(b))
            except:
                pass

    else:
        month = None
        day = input(c).title()
        while day not in day_of_week:
            day = input(error_message).title()

    print('-'*40)
    return city, month, day, option


def load_data(city, month, day, option):
     """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (int) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    if city == 'ch':
        data_city = pd.read_csv('chicago.csv')
    elif city == 'ny':
        data_city = pd.read_csv('new_york_city.csv')
    else:
        data_city = pd.read_csv('washington.csv')

    data_city['Start Time'] = pd.to_datetime(data_city['Start Time'])
    data_city['End Time'] = pd.to_datetime(data_city['End Time'])

    if option == 'month':
        df = data_city[data_city['Start Time'].dt.month == month]
    else:
        df = data_city[data_city['Start Time'].dt.weekday_name == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['Start Time'].dt.month.value_counts().head(1).idxmax()
    print("The most common month is: " + str(most_common_month))

    # TO DO: display the most common day of week
    most_common_day_week = df['Start Time'].dt.weekday_name.value_counts().head(1).idxmax()
    print("The most common day of the week is: " + str(most_common_day_week))

    # TO DO: display the most common start hour
    most_common_start_hour = df['Start Time'].dt.hour.value_counts().head(1).idxmax()
    print("The most common start hour is: " + str(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is: ' +
          df['Start Station'].value_counts().head(1).idxmax())

    # TO DO: display most commonly used end station
    print('The most common end station is: ' +
          df['End Station'].value_counts().head(1).idxmax())

    # TO DO: display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    a = df['Trip Duration'].sum()
    print('The total travel time was ' + str(a))

    # TO DO: display mean travel time
    b = df['Trip Duration'].mean()
    print('The mean travel time was ' + str(b))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_per_user = df['User Type'].value_counts()
    print('Counts per user type:')
    print(count_per_user)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_per_gender = df['Gender'].value_counts()
        print('Counts per gender:')
        print(count_per_gender)
    else:
        print('No data about genders exist')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].value_counts().idxmax())
        print('The most common year is {}, the earliest year is {}, and the most recent year is {}.'.format(
            most_common, earliest, most_recent))
    else:
        print('No data about birth years exist')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Ask users whether they want to see the first 5 lines of the dataframe and
       keeps doing it until users says no."""

    raw = 'no'
    x = 0
    while raw in answers:
        raw = input('Would you like to see raw data? (yes/no): ').lower()
        if raw == 'yes':
            print(df.iloc[x:x+5])
            x += 5
        if raw == 'no':
            break
        if raw not in answers:
            print('I asked you to write YES or NO and you put something different. I will take it as a NO')


def main():
    while True:
        city, month, day, option = get_filters()
        df = load_data(city, month, day, option)

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
