
def progress_bar(curr, total, full_bar_value=100):
    frac = curr / total
    amount_filled = round(frac * full_bar_value)
    print('\r', '#' * amount_filled + '-' * (full_bar_value - amount_filled), '[{:>7.2%}]'.format(frac), end='')
