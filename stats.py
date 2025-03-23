def get_num_count(text):
    count = 0
    for word in text.split():
        count += 1
    return count

def get_char_count(text):
    char_count = {}
    for char in text:
        if char.lower() not in char_count:
            char_count[char.lower()] = 1
        else:
            char_count[char.lower()] += 1
    return char_count

def sort_on(dict):
    return dict["count"]

def get_sorted_list(dict):
    list = []
    for letter in dict:
        new_dict = {"char": letter, "count": dict[letter]}
        list.append(new_dict)
    list.sort(reverse=True, key=sort_on)
    return list