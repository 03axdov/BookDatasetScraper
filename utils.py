def process_num_ratings(rating):
    if rating[-1].lower() == "k":
        return float(rating[0: len(rating) - 1]) * 1000
    if rating[-1].upper() == "M":
        return float(rating[0: len(rating) - 1]) * 1000000
    else:
        return float(rating)


def create_ds(file_path = "db.txt"):
    labels = []
    text = []
    titles = []
    years = []
    lengths = []

    with open(file_path) as file:
        for line in file:
            line_list = line.split(" <SEP> ")

            labels.append(line_list[0])
            text.append(line_list[1])
            titles.append(line_list[2])
            years.append(line_list[3])
            lengths.append(line_list[4].replace("\n", ""))

        file.close()

    return labels, text, titles, years, lengths


def write_to_file(rating, text, title, year, length, file_path = "db.txt"):
    with open(file_path, 'a') as file:
        file.write(str(rating) + " <SEP> " + str(text) + " <SEP> " + str(title) + " <SEP> " + str(year) + " <SEP> " + str(handle_length(length)) + "\n")

        file.close()


def handle_length(length):  # Minutes
    length = length.replace(" ", "")

    time = 0
    current = ''
    for i in length:
        if i.lower() != "h" and i.lower() != "m":
            current += i
        elif i.lower() == "h":
            time += int(current) * 60
            current = ''
        else:
            time += int(current)

    return time
