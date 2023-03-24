import random
import string
import collections
import math
import matplotlib.pyplot as plt


# seq1
n_1 = 97
list1_s1 = [1] * 3
list0_s1 = [0] * n_1

original_sequence_1 = list0_s1 + list1_s1
random.shuffle(original_sequence_1)

original_sequence_1_str = ''.join(map(str, original_sequence_1))

unique_chars = set(original_sequence_1)
unique_chars_len = len(unique_chars)

original_sequence_size_byte = len(original_sequence_1)
original_sequence_size_bit = len(original_sequence_1) * 8


# seq2
n_2 = 92
list1_s2 = ['b','o','r','b','o','t','k','o']
list0_s2 = [0] * n_2
original_sequence_2 = list1_s2 + list0_s2

original_sequence_2_str = ''.join(map(str, original_sequence_2))

unique_chars_s2 = set(original_sequence_2)
unique_chars_s2_len = len(unique_chars_s2)

original_sequence_2_size_byte = len(original_sequence_2)
original_sequence_2_size_bit = len(original_sequence_2) * 8


# seq3
n_3 = 92
list1_s3 = ['b', 'o', 'r', 'b', 'o', 't', 'k', 'o']
list0_s3 = [0] * n_3

original_sequence_3 = list1_s3 + list0_s3

random.shuffle(original_sequence_3)
original_sequence_3_str = ''.join(map(str, original_sequence_3))

unique_chars_s3 = set(original_sequence_3)
unique_chars_s3_len = len(unique_chars_s3)

original_sequence_3_size_byte = len(original_sequence_3)
original_sequence_3_size_bit = len(original_sequence_3) * 8


# seq4
n_seq = 100
letters = ['b', 'o', 'r', 'b', 'o', 't', 'k', 'o', 5, 2, 9]
n_letters = len(letters)
n_repeats = n_seq // n_letters
n_remainder = (n_seq % n_letters)

list = letters * n_repeats
list += letters[:n_remainder]

original_sequence_4_str = ''.join(map(str, list))

unique_chars_s4 = set(original_sequence_4_str)
unique_chars_s4_len = len(unique_chars_s4)

original_sequence_4_size_byte = len(original_sequence_4_str)
original_sequence_4_size_bit = len(original_sequence_4_str) * 8


# seq5
n_seq2 = 100
list2 = ['b', 'o', 5, 2, 9]
pi = [0.2, 0.2, 0.2, 0.2, 0.2]

original_sequence_5 = list2 * 20
random.shuffle(original_sequence_5)

original_sequence_5_str = ''.join(map(str, original_sequence_5))

unique_chars_s5 = set(original_sequence_5_str)
unique_chars_s5_len = len(unique_chars_s5)

original_sequence_5_str_size_byte = len(original_sequence_5_str)
original_sequence_5_str_size_bit = len(original_sequence_5_str) * 8


# seq6
n_seq3 = 100

p_letters = int(0.7 * n_seq3)
p_digits = int(0.3 * n_seq3)

letters2 = ['b', 'o']
digits = [5, 2, 9]
n_letters2 = letters2 * 70
n_digits = digits * 30

list_100 = []
for i in range(p_letters):
    list_100.append(random.choice(letters2))
for i in range(p_digits):
    list_100.append(random.choice(digits))
random.shuffle(list_100)

original_sequence_6_str = ''.join(map(str, list_100))

unique_chars_s6 = set(original_sequence_6_str)
unique_chars_s6_len = len(unique_chars_s6)

original_sequence_6_str_size_byte = len(original_sequence_6_str)
original_sequence_6_str_size_bit = len(original_sequence_6_str) * 8


# seq7
n_seq4 = 100
elements = string.ascii_lowercase + string.digits
list_100_seq7 = [random.choice(elements) for i in range(n_seq4)]

original_sequence_7_str = ''.join(map(str, list_100_seq7))

unique_chars_s7 = set(original_sequence_7_str)
unique_chars_s7_len = len(unique_chars_s7)

original_sequence_7_str_size_byte = len(original_sequence_7_str)
original_sequence_7_str_size_bit = len(original_sequence_7_str) * 8


# seq8
n_seq4 = 100
list3 = [1] * n_seq4
original_sequence_8_str = ''.join(map(str, list3))

unique_chars_s8 = set(original_sequence_8_str)
unique_chars_s8_len = len(unique_chars_s8)

original_sequence_8_str_size_byte = len(original_sequence_8_str)
original_sequence_8_str_size_bit = len(original_sequence_8_str) * 8


# seq_final

original_sequences = [original_sequence_1_str, original_sequence_2_str, original_sequence_3_str,
                     original_sequence_4_str, original_sequence_5_str, original_sequence_6_str,
                     original_sequence_7_str, original_sequence_8_str]


save_sequence_str = ''.join(map(str, original_sequences))
save_sequence = open('sequence.txt', 'w')
save_sequence.write(str(original_sequences))
save_sequence.close()

results = []
for sequence in original_sequences:
    counts = collections.Counter(sequence)
    probability = {symbol: count / n_seq4 for symbol, count in counts.items()}
    mean_probability = sum(probability.values()) / len(probability)
    equal = all(abs(prob - mean_probability) < 0.05 * mean_probability for prob in probability.values())
    if equal:
        uniformity = "рівна"
    else:
        uniformity = "нерівна"

    sequence_alphabet_size = len(set(sequence))
    entropy = -sum(p * math.log2(p) for p in probability.values())
    if sequence_alphabet_size > 1:
        source_excess = 1 - entropy / math.log2(sequence_alphabet_size)
    else:
        source_excess = 1

    sequence_size_byte = len(original_sequence_8_str)
    sequence_size_bit = len(original_sequence_8_str) * 8
    probability_str = ', '.join([f"{symbol}={prob:.4f}" for symbol, prob in probability.items()])
    with open("results_sequence.txt", "a") as file:
        file.write("Послідовність  " + str(sequence) + "\n")
        file.write("Розмір послідовності " + str(sequence_size_byte) + 'bytes' + "\n")
        file.write("Розмір алфавіту " + str(sequence_alphabet_size) + "\n")

        file.write("Ймовірності появи символів  " + str(probability_str) + "\n")
        file.write("Середнє арифметичне ймовірностей  " + str(mean_probability) + "\n")
        file.write("Ймовірність розподілу символів  " + str(equal) + "\n")
        file.write("Ентропія  " + str(entropy) + "\n")
        file.write("Надмірність джерела  " + str(source_excess) + "\n")
        file.write("-------------------------------------- " + "\n")

    results.append([sequence_alphabet_size, round((entropy), 2), round((source_excess), 2), uniformity])
fig, ax = plt.subplots(figsize=(14 / 1.54, 8 / 1.54))
headers = ['Розмір алфавіту', 'Ентропія', 'Надмірність', 'Ймовірність']
row = ['Послідовність 1', 'Послідовність 2', 'Послідовність 3', 'Послідовність 4', 'Послідовність 5',
       'Послідовність 6', 'Послідовність 7', 'Послідовність 8']
ax.axis('off')
table = ax.table(cellText=results, colLabels=headers, rowLabels=row, loc='center', cellLoc='center')
table.set_fontsize(14)
table.scale(0.8, 2)
title = 'Характеристики сформованих послідовностей'
fig.savefig(title + '.png')
