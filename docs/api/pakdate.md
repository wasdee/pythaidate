# PakDate API Reference

## Class: PakDate

### Constructors

#### `PakDate(jd: int = None, pakcode: str = None, date: date = None)`

Create a new PakDate object. Must provide one of:
- `jd`: Julian Day Number
- `pakcode`: Pakkhakhananaa code string
- `date`: datetime.date object

#### Class Methods

- `fromjulianday(jd: int)`: Create from Julian Day Number
- `today()`: Create for current date

### Properties

- `julianday`: Julian Day Number
- `horakhun`: Days since Pakkhakhananaa epoch
- `pakkhagen`: Lunar weeks since epoch
- `pakcode`: Full Pakkhakhananaa code
- `pakabbr`: Abbreviated code
- `iswaxing`: Is moon waxing
- `iswaning`: Is moon waning
- `iswanphra`: Is Buddhist sabbath day
- `issabbath`: Alias for iswanphra

### Methods

- `pakboard(fh=None)`: Display Pakkhakhananaa board
- `weekday()`: Get weekday (0-6)
- `isoweekday()`: Get ISO weekday (1-7)

### Comparison Operations

Supports standard comparison operators (`<`, `<=`, `==`, `>=`, `>`) with:
- Other PakDate objects
- datetime.date objects
- Objects with a julianday property

### Arithmetic Operations

- Addition with timedelta
- Subtraction of timedelta
- Subtraction of another PakDate/date returns timedelta 