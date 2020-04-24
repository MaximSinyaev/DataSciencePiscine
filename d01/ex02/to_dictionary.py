list_of_tuples = [
    ("Russia", "25"),
    ("France", "132"),
    ("Germany", "132"),
    ("Spain", "178"),
    ("Italy", "162"),
    ("Portugal", "17"),
    ("Finland", "3"),
    ("Hungary", "2"),
    ("The Netherlands", "28"),
    ("The USA", "610"),
    ("The United Kingdom", "95"),
    ("China", "83"),
    ("Iran", "76"),
    ("Turkey", "65"),
    ("Belgium", "34"),
    ("Canada", "28"),
    ("Switzerland", "26"),
    ("Brazil", "25"),
    ("Austria", "14"),
    ("Israel", "12")
]


def tuples_to_dict():
    result = dict()
    for pair in list_of_tuples:
        if pair[1] not in result:
            result[pair[1]] = list()
        # for i in result[pair[1]]:
        result[pair[1]].append(pair[0])

    for key in result:
        for country in result[key]:
            print(f'"{key}" : "{country}"')
    # print(result)


if __name__ == "__main__":
    tuples_to_dict()
