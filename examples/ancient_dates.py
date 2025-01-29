import ephem
from datetime import datetime, timedelta
import math

def get_full_moon_date(year, month):
    """Calculate the full moon date for a given year and month."""
    # Create a date object for the start of the month
    date = ephem.Date(datetime(year if year > 0 else year + 1, month, 1))
    
    # Get next full moon after this date
    next_full = ephem.next_full_moon(date)
    
    # Convert ephem Date to Python datetime
    return ephem.Date(next_full).datetime()

def print_moon_phase_info(title, year, month, day):
    """Print detailed moon phase information for a given date."""
    print(f"\n=== {title} ===")
    
    # Create Moon object
    moon = ephem.Moon()
    
    # Create Observer on Earth
    observer = ephem.Observer()
    observer.lat = '13.7563'  # Bangkok latitude
    observer.lon = '100.5018'  # Bangkok longitude
    
    # Set the date
    date = ephem.Date(datetime(year if year > 0 else year + 1, month, day))
    observer.date = date
    
    # Calculate moon's phase
    moon.compute(observer)
    
    # Moon phase is returned as a number between 0 and 1
    phase = moon.phase
    
    # Calculate days since new moon
    previous_new = ephem.previous_new_moon(date)
    days_since_new = (date - previous_new) * 24 * 60 * 60 / (24 * 60 * 60)  # Convert to days
    
    print(f"Date: {year}-{month:02d}-{day:02d}")
    print(f"Moon Phase: {phase:.1f}%")
    print(f"Days since new moon: {days_since_new:.1f}")
    
    # Determine if it's waxing or waning
    next_full = ephem.next_full_moon(date)
    previous_full = ephem.previous_full_moon(date)
    
    if abs(date - next_full) < abs(date - previous_full):
        print("Moon is waxing (ข้างขึ้น)")
    else:
        print("Moon is waning (ข้างแรม)")

def main():
    # Steve Jobs' passing date
    print_moon_phase_info("Steve Jobs' Passing Date", 2011, 10, 5)
    
    # Calculate full moon in Vesak month (May) of 563 BCE
    try:
        buddha_full_moon = get_full_moon_date(-563, 5)
        print_moon_phase_info(
            "Buddha's Traditional Birth Date (563 BCE)", 
            -563, 
            buddha_full_moon.month, 
            buddha_full_moon.day
        )
    except Exception as e:
        print("\n=== Buddha's Birth Date Calculation ===")
        print("Note: Astronomical calculations for dates this far in the past")
        print("may not be completely accurate due to changes in Earth's rotation")
        print("and other astronomical factors.")
        print("\nTraditional date: Full moon of Vesak month (May), 563 BCE")
    
    print("\n=== Additional Information ===")
    print("Note: Astronomical calculations for ancient dates should be")
    print("treated as approximations due to:")
    print("1. Changes in Earth's rotation over millennia")
    print("2. Calendar system differences")
    print("3. Historical recording variations")

if __name__ == "__main__":
    main() 