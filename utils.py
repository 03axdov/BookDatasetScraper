def process_ratings_count(ratings_count):
    current = ""
    for i in ratings_count:
        if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ","]:
            break
        current += i
    ratings_count = current.replace(",", "")
    return ratings_count


def create_ds(file_path = "db.txt"):
    ratings = []
    ratings_counts = []
    descriptions = []
    titles = []

    with open(file_path) as file:
        for line in file:
            line_list = line.split(" <SEP> ")

            ratings.append(line_list[0])
            ratings_counts.append(line_list[1])
            descriptions.append(line_list[2])
            titles.append(line_list[3].replace("\n", ""))

        file.close()

    return ratings, ratings_counts, titles, titles


def write_to_file(rating, ratings_count, description, title, file_path = "db.txt"):
    with open(file_path, 'a') as file:
        file.write(str(rating) + " <SEP> " + str(process_ratings_count(ratings_count)) + " <SEP> " + str(description) + " <SEP> " + str(title) + "\n")

        file.close()