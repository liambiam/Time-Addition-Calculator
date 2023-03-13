def add_time(start, duration, day=None):
  
    # Define variables by splitting inputs

    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

   # Convert to 24hr clock

    if period == 'PM' and start_hour != 12:
        start_hour += 12

    # Calculate end time, hour, period

    end_minute = (start_minute + duration_minute) % 60
    end_hour = (start_hour + duration_hour + (start_minute + duration_minute) // 60) % 24
    end_period = 'AM' if end_hour < 12 else 'PM'

    # Re-convert to 12hr clock

    if end_hour > 12:
        end_hour -= 12
    if end_hour == 0:
        end_hour = 12

    # Format end time as string. 2d.p for minute
    new_time = f'{end_hour}:{end_minute:02} {end_period}'

    # Calculate number of days later
    days_later = (start_hour + duration_hour + ((start_minute + duration_minute) // 60)) // 24

    # Calculate day of the week if given
    if day is not None:
        day = day.capitalize()
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_index = days_of_week.index(day)
        end_day_index = (start_day_index + days_later) % 7
        end_day = days_of_week[end_day_index]
        new_time += f', {end_day}'

    # Format number of days later as string
    if days_later == 1:
        new_time += ' (next day)'
    elif days_later > 1:
        new_time += f' ({days_later} days later)'
    print(new_time)

    return new_time

add_time("11:58 PM", "20:05")