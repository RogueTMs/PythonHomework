def format_table(benchmarks, algos, results):
    benchmarks.insert(0, "Benchmark")
    b_len = len(max(benchmarks, key=len)) + 2
    a_len = len(max(algos, key=len)) + 2

    flag = a_len + b_len * len(algos) - 1
    results.insert(0, algos)
    for i in range(len(benchmarks)):
        print(f"| {benchmarks[i]:<{b_len}}", end='')
        for j in range(len(algos)):
            print(f"| {results[i][j]:<{a_len}}", end='')
        print("|\n", end='')
        if flag:
            print("|" + "-" * flag + "|")
            flag = 0


format_table(["best case", "worst ever case"],
             ["quick sort", "merge sort", "bubble sort"],
             [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
