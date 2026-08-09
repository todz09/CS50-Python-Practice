def total(galleons, sickles, knuts):
    return (galleons * 493 * 29 + sickles) * 29 + knuts


# coins = [100, 50, 25]
coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "knuts")
