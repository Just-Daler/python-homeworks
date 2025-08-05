import threading

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    primes = [n for n in range(start, end) if is_prime(n)]
    result.extend(primes)

def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    results = []
    chunk_size = (end - start) // num_threads

    for i in range(num_threads):
        chunk_start = start + i * chunk_size
        chunk_end = start + (i + 1) * chunk_size if i < num_threads - 1 else end
        thread = threading.Thread(target=check_primes, args=(chunk_start, chunk_end, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    results.sort()
    print("Primes found:", results)

# Example usage
threaded_prime_checker(1, 100, num_threads=4)


import threading
from collections import Counter

def count_words(lines, result_list):
    counter = Counter()
    for line in lines:
        words = line.strip().lower().split()
        counter.update(words)
    result_list.append(counter)

def threaded_word_counter(filename, num_threads=4):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    threads = []
    results = []
    chunk_size = len(lines) // num_threads

    for i in range(num_threads):
        chunk_start = i * chunk_size
        chunk_end = (i + 1) * chunk_size if i < num_threads - 1 else len(lines)
        thread = threading.Thread(
            target=count_words,
            args=(lines[chunk_start:chunk_end], results)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Combine all counters
    final_counter = Counter()
    for result in results:
        final_counter.update(result)

    print("Word frequencies:")
    for word, count in final_counter.most_common(10):  # Top 10
        print(f"{word}: {count}")

# Example usage
# threaded_word_counter("large_text_file.txt", num_threads=4)
