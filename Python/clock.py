def add_time(start_time, duration, start_day=None):
    # Parse start time
    time_part, period = start_time.split()
    hours, minutes = map(int, time_part.split(':'))
    
    # Convert to 24-hour format
    if period == 'PM' and hours != 12:
        hours += 12
    elif period == 'AM' and hours == 12:
        hours = 0
    
    # Parse duration
    parse_hours, parse_minutes = map(int, duration.split(':'))
    
    # Add minutes first
    total_minutes = minutes + parse_minutes
    carry_hours = total_minutes // 60
    remaining_minutes = total_minutes % 60
    
    # Add hours with carry from minutes
    total_hours = hours + parse_hours + carry_hours
    days_passed = total_hours // 24
    remaining_hours = total_hours % 24
    
    # Convert back to 12-hour format
    if remaining_hours == 0:
        new_period = 'AM'
        display_hours = 12
    elif remaining_hours < 12:
        new_period = 'AM'
        display_hours = remaining_hours
    elif remaining_hours == 12:
        new_period = 'PM'
        display_hours = 12
    else:
        new_period = 'PM'
        display_hours = remaining_hours - 12
    
    # Format the time string
    formatted_time = f"{display_hours}:{remaining_minutes:02d} {new_period}"
    
    # Handle day of week if provided
    if start_day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_lower = start_day.lower()
        day_index = next((i for i, day in enumerate(days_of_week) if day.lower() == start_day_lower), 0)
        new_day_index = (day_index + days_passed) % 7
        new_day = days_of_week[new_day_index]
        formatted_time += f", {new_day}"
    
    # Add day information
    if days_passed == 1:
        formatted_time += " (next day)"
    elif days_passed > 1:
        formatted_time += f" ({days_passed} days later)"
    
    return formatted_time

# Test case that was failing
print(add_time('3:12 PM', '964:45'))