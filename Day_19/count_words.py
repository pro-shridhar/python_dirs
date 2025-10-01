def count_words():
    with open("new.txt", "r") as file:
        content = file.read()
        count = 0
        for word in content:
            if word != " ":
                count += 1

    return count


print(count_words())
