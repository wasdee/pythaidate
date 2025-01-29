# Chulasakarat Calendar (จุลศักราช)

The Chulasakarat calendar is a lunisolar calendar system that was historically used in Thailand. This calendar combines aspects of both lunar and solar calendars.

## Basic Usage

`CsDate` objects can be created from a year, month, day triple, like a `datetime.date` object. They represent the Thai lunisolar calendar with the epoch of 22nd March 638 AD. Months should be specified in Sukothai number format (eg. 5 is the first month).

```python
from pythaidate import CsDate

# Create a date
cs = CsDate(1361, 1, 24)
print(cs.year, cs.month, cs.day)  # 1361, 1, 24

# Get days since new year
print(cs.days)  # 260

# Get days since epoch (horakhun)
print(cs.horakhun)  # 497378

# Get Julian Day Number
print(cs.julianday)  # 2451545
```

## Calendar Properties

The calendar provides several properties for understanding the internal calculations:

```python
# Get internal calculation values
print(cs.kammacapon)  # Excess of solar days over whole solar days
print(cs.masaken)     # Number of lunar months since epoch
print(cs.uccapon)     # Position of Moon's apogee
print(cs.avoman)      # Excess of lunar days over solar days
print(cs.tithi)       # Lunar day (1/30th of synodic month)
```

## Alternative Constructors

You can create `CsDate` objects in several ways:

```python
# From year and days since new year
cs = CsDate.fromyd(1361, 260)

# From Julian Day Number
cs = CsDate.fromjulianday(2451545)

# Get today's date
cs = CsDate.today()
```

## Formatting

Convert a `CsDate` to Thai text representation:

```python
cs = CsDate(1361, 1, 24)
print(cs.csformat())  # 'วันเสาร์ เดือน ๑ แรม ๙ ค่ำ ปีเถาะ จ.ศ.๑๓๖๑'
print(str(cs))        # Same as csformat()
```

## Intercalations

The calendar has three types of intercalations:

```python
cs = CsDate(1361, 1, 24)
print(cs.solar_leap_year)  # Solar leap year (อธิกสุรทิน)
print(cs.leap_day)         # Lunar intercalary day (อธิกวาร)
print(cs.leap_month)       # Lunar intercalary month (อธิกมาส)
print(cs.days_in_year)     # Total days in year (354, 355, or 384)
```

!!! note
    A year can only have either zero or one intercalations. There can't be both an intercalary day (อธิกวาร) and month (อธิกมาส) in the same year. 