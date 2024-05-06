import pandas as pd

from kmp import kmp_search
from boyer_moore import boyer_moore_search
from rabin_karp import rabin_karp_search

import timeit


def load_text_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def test_algorithm(algorithm, text, pattern):
    return round(timeit.timeit(lambda: algorithm(text, pattern), number=1), 6)


def test_search_algorithms(file_name, patterns):
    text = load_text_from_file(file_name)
    algorithms = [kmp_search, boyer_moore_search, rabin_karp_search]
    results = []

    for pattern_type, pattern in patterns.items():
        for algorithm in algorithms:
            time_taken = test_algorithm(algorithm, text, pattern)
            results.append((file_name, pattern_type, algorithm.__name__, time_taken))

    return results


def main():
    patterns_article1 = {'existing': "хеш-таблиц", 'non-existing': "qwerty"}
    patterns_article2 = {'existing': "серії експериментів", 'non-existing': "qwerty"}

    results_article1 = test_search_algorithms('paper_1.txt', patterns_article1)
    results_article2 = test_search_algorithms('paper_2.txt', patterns_article2)

    all_results = results_article1 + results_article2

    data = {
        'File': [result[0] for result in all_results],
        'Pattern Type': [result[1] for result in all_results],
        'Algorithm': [result[2] for result in all_results],
        'Time (s)': [result[3] for result in all_results]
    }

    df = pd.DataFrame(data)

    print(f'{"-"*80}\nНайшвидший алгоритм\n{"-"*80}')
    fastest_approaches_per_file_pattern = df.groupby(['File', 'Pattern Type'], as_index=False).agg(
        {'Time (s)': 'min'}).merge(df, on=['File', 'Pattern Type', 'Time (s)'], how='left')
    print(fastest_approaches_per_file_pattern)

    print(f'{"-"*80}\nЗагальне порівняння алгоритмів\n{"-"*80}')
    pivot_table = df.pivot_table(values='Time (s)', index='Algorithm', columns='Pattern Type', aggfunc='mean')
    print(pivot_table)

    print(f'{"-" * 80}\nЗагальні результати\n{"-" * 80}')
    print(df)


if __name__ == '__main__':
    main()
