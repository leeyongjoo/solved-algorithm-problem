def solution(table, languages, preference):
    total_scores = []  # score, job
    for s in table:
        job, *langs = s.split(' ')
        langs_dict = {lang: i for i, lang in enumerate(langs[::-1], start=1)}
        score = 0
        for lang, pref in zip(languages, preference):
            score += langs_dict.get(lang, 0) * pref
        total_scores.append((score, job))
    return sorted(total_scores, key=lambda a: (-a[0], a[1]))[0][1]


if __name__ == "__main__":
    t, l, p = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
               "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
               "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]
    # "HARDWARE"
    # print(solution(t, l, p))

    t, l, p = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
               "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
               "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]
    # "PORTAL"
    print(solution(t, l, p))
