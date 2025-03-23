def get_num_count(text):
    count = 0
    for word in text.split():
        count += 1
    return count