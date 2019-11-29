intervals = [(1990, 2008), (1990, 2008), (1994, 2004), (1998, 2010)]

def getLivingPeople(intervals):
    borders = []
    for birth, death in intervals:
        borders.append((birth, +1))
        borders.append((death, -1))
    borders = sorted(borders)
    c = 0
    maxi = -float("inf")
    year = None
    for couple in borders:
        c += couple[1]
        if c > maxi:
            maxi = c
            year = couple[0]
    return year, maxi

if __name__ == "__main__":
    print(getLivingPeople(intervals))