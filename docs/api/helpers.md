# Helper Functions

## Julian Day Number Helpers

### `to_julianday(year: int, month: int, day: int) -> int`
Convert year, month, day to Julian Day Number.

### `from_julianday(jd: int) -> tuple`
Convert Julian Day Number to (year, month, day) tuple.

### `today() -> int`
Get Julian Day Number for current date.

### `date_to_julianday(d: date) -> int`
Convert datetime.date or object with julianday property to Julian Day Number.

### `julianday_to_date(jd: int) -> date`
Convert Julian Day Number to datetime.date object.

## Thai Number Conversion

### `digit_thai_to_arabic(s: str) -> str`
Convert Thai numerals to Arabic numerals in string.

### `digit_arabic_to_thai(s: str) -> str`
Convert Arabic numerals to Thai numerals in string.

### `thai_string_width(s: str) -> int`
Calculate display width of Thai string. 