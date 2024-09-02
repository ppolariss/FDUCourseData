prefixes = [
    "AIB11",
    "AIB21",
    "AIB31",
    "AIE21",
    "AIE31",
    "AIE41",
    "AIE53",
    "AIE83",
    "AIS21",
    "AIS31",
    "AIS41",
    "AIS53",
    "AIS63",
    "AIS73",
    "AIT31",
    "AIT41",
    "AIT53",
    "ATMO11",
    "ATMO13",
    "BIOL11",
    "BIOL12",
    "BIOL13",
    "CHEM11",
    "CHEM12",
    "CHEM13",
    "CHIN11",
    "CHIN12",
    "CHIN13",
    "CHIN17",
    "COMP11",
    "COMP12",
    "COMP13",
    "DATA11",
    "DATA13",
    "ECON11",
    "ECON12",
    "ECON13",
    "ECON16",
    "ECON17",
    "ENGL01",
    "ENGL11",
    "ENVI11",
    "ENVI13",
    "ENVI17",
    "FINE11",
    "FISF13",
    "FORE11",
    "FORE12",
    "FORE13",
    "GNUR11",
    "GNUR13",
    "HIST11",
    "HIST12",
    "HIST13",
    "HIST17",
    "ICES11",
    "ICES12",
    "ICES13",
    "ICES17",
    "INFO11",
    "INFO12",
    "INFO13",
    "INNO11",
    "JOUR11",
    "JOUR12",
    "JOUR13",
    "JOUR16",
    "JOUR17",
    "JWCH11",
    "KQSY11",
    "LAWS11",
    "LAWS12",
    "LAWS13",
    "LAWS16",
    "LAWS17",
    "MACR11",
    "MACR13",
    "MANA11",
    "MANA12",
    "MANA13",
    "MANA17",
    "MATE11",
    "MATE13",
    "MATE17",
    "MATH01",
    "MATH11",
    "MATH12",
    "MATH13",
    "MATH17",
    "MECH11",
    "MECH13",
    "MED11",
    "MED110",
    "MED115",
    "MED116",
    "MED119",
    "MED13",
    "MED130",
    "MED170",
    "MICR11",
    "MICR12",
    "MICR13",
    "MUSE11",
    "MUSE12",
    "MUSE13",
    "NDEC11",
    "NURS11",
    "NURS13",
    "PEDU11",
    "PEDU13",
    "PEDU17",
    "PHAR11",
    "PHAR13",
    "PHIL11",
    "PHIL12",
    "PHIL13",
    "PHPM11",
    "PHPM13",
    "PHYS11",
    "PHYS12",
    "PHYS13",
    "POLI11",
    "POLI13",
    "POLI16",
    "POLI17",
    "PTSS01",
    "PTSS11",
    "PTSS13",
    "PTSS17",
    "RZSY11",
    "SOCI11",
    "SOCI12",
    "SOCI13",
    "SOCI17",
    "SOFT11",
    "SOFT12",
    "SOFT13",
    "SOSC12",
    "STOM13",
    "STUO11",
    "TCPH11",
    "TCPH13",
    "TFSY11",
    "TOUR11",
    "TOUR13",
    "XDSY11",
    "XHXT12",
    "ZDSY11",
]
unique_prefixes = sorted(set(prefixes))

# 输出前缀
print("export const CODE_PREFIXES = [")
for prefix in unique_prefixes:
    print(f"  '{prefix}',")
print("];")
