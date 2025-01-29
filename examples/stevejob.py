from pythaidate import CsDate, PakDate
from datetime import date
from pythaidate.julianday import date_to_julianday, julianday_to_date

def print_date_details(title, date_input):
    """
    Print Thai calendar details for a given date
    Args:
        title: String title for the output
        date_input: Can be either a datetime.date object or Julian day number
    """
    print(f"\n=== {title} ===")
    
    # Convert input to both Gregorian and Julian day formats
    if isinstance(date_input, (int, float)):
        # Input is Julian day
        julianday = date_input
    else:
        # Input is Gregorian date
        gregorian_date = date_input
        julianday = date_to_julianday(gregorian_date)
    
    # Convert to Thai lunar calendar formats
    date_in_cs = CsDate.fromjulianday(julianday)
    date_in_pak = PakDate.fromjulianday(julianday)
    
    print("Gregorian date:", gregorian_date)
    # print("Julian day:", julianday)
    print("Full Thai lunar date:", date_in_cs.csformat())
    print(f"Horakhun (หรคุฌ): {date_in_cs.horakhun}")  # Days since epoch
    print(f"Kammacapon (กัมมัขผล): {date_in_cs.kammacapon}")  # Solar day excess
    print(f"Masaken (มาสเกฌฑ์): {date_in_cs.masaken}")  # Lunar months since epoch
    print(f"Uccapon (อุจจพล): {date_in_cs.uccapon}")  # Moon's apogee position
    print(f"Avoman (อวมาน): {date_in_cs.avoman}")  # Lunar/solar day excess
    print(f"Tithi (ดิถี): {date_in_cs.tithi}")  # Lunar day (1/30 synodic month)
    
    print("Pakkhanipatai format:", date_in_pak.pakboard())


    print("\nMoon Phase Information:")
    print(f"Moon is waxing (ข้างขึ้น): {date_in_pak.iswaxing}")
    print(f"Moon is waning (ข้างแรม): {date_in_pak.iswaning}")
    print(f"Is Buddhist holy day (วันพระ): {date_in_pak.iswanphra}")

# Steve Jobs' passing date
steve_jobs_date = date(2011, 10, 5)
# Matched with www.myhora.com
print_date_details("Steve Jobs' Passing Date", steve_jobs_date)

# Example with Julian day input (around Buddha's time)
# Note: This is an approximation as dates this far back are not reliable
try:
    # Buddha's birth date if he was dead in the same date as Steve Jobs
    # buddha_ancient_julianday = 1516065  
    buddha_death_gregorian = date(-563, 5, 15)
    buddha_death_julianday = date_to_julianday(buddha_death_gregorian)
    print_date_details("Ancient Date via Julian Day", buddha_death_julianday)
except ValueError as e:
    print("\n=== Buddha's Birth Date ===")
    print("Note: Unable to process dates before 1 CE directly.")
    print("Historical records indicate Buddha was born around 563 BCE,")
    print("traditionally celebrated on the full moon day of Vesak (May).")
    print("This corresponds to the 15th day of the 6th lunar month in the Buddhist calendar.")

