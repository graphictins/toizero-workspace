

day   = int( input() )
month = int( input() )

# (Cutoff Day, "Sign" if <= Cutoff, "Sign" if > Cutoff)
zodiacs = [
    (0 , ""         , ""           ), # Placeholder for index 0
    (19, "capricorn", "aquarius"   ), # Jan
    (18, "aquarius" , "pisces"     ), # Feb
    (20, "pisces"   , "aries"      ), # Mar
    (19, "aries"    , "taurus"     ), # Apr
    (20, "taurus"   , "gemini"     ), # May
    (21, "gemini"   , "cancer"     ), # Jun
    (22, "cancer"   , "leo"        ), # Jul
    (22, "leo"      , "virgo"      ), # Aug
    (22, "virgo"    , "libra"      ), # Sep
    (23, "libra"    , "scorpio"    ), # Oct
    (21, "scorpio"  , "sagittarius"), # Nov
    (21, "sagittarius", "capricorn")  # Dec
]

# pick one row out to use based on month input
cutoff, sign_before, sign_after = zodiacs[month]

if day <= cutoff:
    print(sign_before)
else:
    print(sign_after)