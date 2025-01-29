# Pakkhakhananaa Calendar (ปฏิทินปักขคณนา)

The Pakkhakhananaa calendar is a traditional Thai lunar calendar system used for religious purposes. It operates on a complex cycle of 289,577 days.

## Basic Usage

Create a `PakDate` object using one of several methods:

```python
from pythaidate import PakDate

# From pakcode string
p = PakDate(pakcode="1-6:11:5:2:2:10")
print(p.horakhun)    # 96398
print(p.julianday)   # 2451545
print(p.iswanphra)   # False

# From datetime.date
from datetime import date
p = PakDate(date=date(2000, 1, 1))

# From Julian Day Number
p = PakDate(jd=2451545)
```

## Pakkhakhananaa Code

Get the Pakkhakhananaa code and abbreviations:

```python
p = PakDate(pakcode="1-6:11:5:2:2:10")
print(p.pakcode)   # '1-6:11:5:2:2:10'
print(p.pakabbr)   # ๖๑๕ข๒
                   #  ๑
```

## Display Board

Display an ASCII Pakkhakhananaa board (กระดานปักขคณนา):

```python
p = PakDate(pakcode="1-6:11:5:2:2:10")
p.pakboard()
```

This will output something like:

```
           ๑  ๒  ๓  ๔  ๕  ๖  ๗  ๘  ๙ ๑๐ ๑๑ ๑๒ ๑๓ ๑๔ ๑๕ ๑๖ ๑๗ ๑๘
ปักขคณนา    ม  ม  ม  ม  ม  ม  ม  ม  ม  ม  ม  ม  ม  ม  ม  ม  ม  จ
มหาสัมพยุหะ  จ  จ  จ  จ  จ  จ  จ  จ  จ  จ  ม
จุลสัมพยุหะ   จ  จ  จ  จ  จ  จ  จ  จ  จ  ม
มหาพยุหะ    ม  ม  ม  ม  ม  ม  จ
จุลพยุหะ     ม  ม  ม  ม  ม  จ
มหาสมุหะ    จ  จ  จ  ม
จุลสมุหะ     จ  จ  ม
มหาวรรค    ม  ม  ม  ม  จ
จุลวรรค     ม  ม  ม  จ
มหาปักข์     ๑  ๒  ๓  ๔  ๕  ๖  ๗  ๘  ๙ ๑๐ ๑๑ ๑๒ ๑๓ ๑๔ ๑๕
จุลปักข์      ๑  ๒  ๓  ๔  ๕  ๖  ๗  ๘  ๙ ๑๐ ๑๑ ๑๒ ๑๓ ๑๔
```

## Properties

Various properties are available:

```python
p = PakDate(pakcode="1-6:11:5:2:2:10")
print(p.iswaxing)    # Is moon waxing
print(p.iswaning)    # Is moon waning
print(p.iswanphra)   # Is Buddhist sabbath day
print(p.issabbath)   # Alias for iswanphra
``` 