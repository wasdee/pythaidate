# CsDate API Reference

## Class: CsDate

### Constructors

#### `CsDate(year: int, month: int, day: int, month_style: int = MONTH_SUK)`

Create a new CsDate object from year, month and day values.

Parameters:
- `year`: Chulasakarat year
- `month`: Month number (Sukothai format)
- `day`: Day of month
- `month_style`: Month numbering style (default: Sukothai)

#### Class Methods

- `fromyd(year: int, days: int)`: Create from year and days since new year
- `fromjulianday(jd: int)`: Create from Julian Day Number
- `today()`: Create for current date

### Properties

- `year`: The Chulasakarat year
- `month`: The month number
- `day`: The day of month
- `days`: Days since new year
- `horakhun`: Days since epoch
- `julianday`: Julian Day Number
- `kammacapon`: Excess of solar days
- `masaken`: Lunar months since epoch
- `uccapon`: Moon's apogee position
- `avoman`: Excess of lunar days
- `tithi`: Lunar day number
- `solar_leap_year`: Is solar leap year
- `leap_day`: Has intercalary day
- `leap_month`: Has intercalary month
- `days_in_year`: Total days in year

### Methods

- `csformat()`: Format date as Thai text
- `csformatymd()`: Format as YYYY-MM-DD
- `fromcsformat(s: str)`: Parse Thai text format
- `weekday()`: Get weekday (0-6)
- `isoweekday()`: Get ISO weekday (1-7)

### Comparison Operations

Supports standard comparison operators (`<`, `<=`, `==`, `>=`, `>`) with:
- Other CsDate objects
- datetime.date objects
- Objects with a julianday property

### Arithmetic Operations

- Addition with timedelta
- Subtraction of timedelta
- Subtraction of another CsDate/date returns timedelta 