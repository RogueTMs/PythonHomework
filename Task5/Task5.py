def format_table(benchmarks, algos, results):

    benchmarks.insert(0, "Benchmark")
    b_len = len(max(benchmarks, key=len)) + 1
    a_len = len(max(algos, key=len)) + 1
    r_len = 0
    for i in range(len(benchmarks) - 1):
        r_len = max(r_len, len(max(list(map(str, results[i])), key=len)))

    flag = b_len + 1 + len(algos) + (max(r_len, a_len) + 1) * len(algos)
    results.insert(0, algos)
    for i in range(len(benchmarks)):
        print(f"| {benchmarks[i]:<{b_len}}", end='')
        for j in range(len(algos)):
            print(f"| {results[i][j]:<{max(a_len, r_len)}}", end='')
        print("|\n", end='')
        if flag:
            print("|" + "-" * flag + "|")
            flag = False


format_table(["baaaaaaaaaaaaaaaaaaaaaaaa", "w"],
             ["quick sort", "merge sort", "bubble sort"],
             [[1111.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
