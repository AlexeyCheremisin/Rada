import random


def get_password(first_num):
    pairs = list()
    for i in range(1, 21):
        for j in range(1, 21):
            if i == j:
                continue
            if first_num % (i + j) == 0:
                if len(pairs) > 0:
                    if (j, i) not in pairs:
                        pairs.append((i, j))
                else:
                    pairs.append((i, j))
    return pairs


if __name__ == "__main__":
    first_number = random.choice(range(3, 21))
    result = f"{first_number} - "
    for pair in get_password(first_number):
        result += f"{pair[0]}{pair[1]}"
    print(result)
