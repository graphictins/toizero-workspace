
import math

def parse_time(s):
    # parse H.MM or HH.MM format
    parts = s.split('.')
    if len(parts) != 2:
        return None
    h = int(parts[0])
    m_str = parts[1]
    if len(m_str) != 2:
        return None
    m = int(m_str)
    if not (0 <= h <= 23) or not (0 <= m <= 59):
        return None
    return h * 60 + m

rates = [0, 25, 50, 80, 110, 145, 180, 250]

line1 = input().strip()
line2 = input().strip()

ti = parse_time(line1)
to = parse_time(line2)

if ti is None or to is None or ti >= to:
    print("ERROR")
else:
    duration_min = to - ti
    if duration_min < 15:
        print("FREE")
    else:
        hours = math.ceil(duration_min / 60)
        if hours >= 7:
            print(rates[7])
        else:
            print(rates[hours])
