with open("sample.txt") as file:
    data = file.read()
top = input("Please enter how many top common words to display: ")
if top.isdigit():
    top = int(top)
    words = []
    splits = [" ", ",", ".", "\n"]
    text = ""
    for i in data:
        if i in splits:
            if text:
                words.append(text)
                text = ""
        else:
            text += i.lower()
    words_count = {}
    for i in words:
        if i not in words_count:
            words_count[i] = 1
        else:
            words_count[i] += 1
    list1 = sorted((v, k) for k, v in words_count.items())[::-1]
    # print(list1)
    if len(list1) >= top:
        n = top
        common_words = list1[:top]
    else:
        print(f"Number of words is less then your input.")
        n = len(list1)
        common_words = list1
    # print(words)
    total_words = len(words)
    print("Total words:", total_words)
    print(f"Top {n} most common words:")
    text = ""
    for i in common_words:
        text += f"{i[1]} - {i[0]} times\n"
    print(text)

    with open("word_count_report.txt", "w") as file:
        file.write(f"Word Count Report\n"
                   f"Total words: {total_words}\n"
                   f"Top {n} most common words:\n"
                   f"{text}")
else:
    print("Please enter only numbers")