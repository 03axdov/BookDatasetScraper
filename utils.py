def process_num_ratings(rating):
    if rating[-1].lower() == "k":
        return float(rating[0: len(rating) - 1]) * 1000
    if rating[-1].upper() == "M":
        return float(rating[0: len(rating) - 1]) * 1000000
    else:
        return float(rating)