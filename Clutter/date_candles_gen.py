from datetime import datetime

#starting date is 2017 - 09 - 21 00.00

def calc_candles(y1, mo1, d1, h1, min1, y2, mo2, d2, h2, min2, min_interval):

    no_candles = datetime(2017, 9, 21, 00, 00)
    starting_candles = datetime(y1, mo1, h1, min1)
    end_candles = datetime(y2, mo2, d2, h2, min2)

    start_diff = start_candles - no_candles
    end_diff = end_candles - no_candles

    start_diff_seconds = start_diff.total_seconds()

    end_diff_seconds = end_diff.total_seconds

    start_diff_candle = start_diff_seconds/(min_interval*60)

    end_diff_candle = end_diff_seconds/(min_interval*60)

    return start_diff_candle, end_diff_candle


x, y = calc_candles(2018, 1, 8, 0, 0, 2018, 1, 11, 3, 0)



