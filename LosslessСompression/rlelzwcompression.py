import collections
import math
import ast
# import string
# import random
import matplotlib.pyplot as plt


open("results_rle_lzw.txt", "w")
results = []


def main():
    n_seq = 100
    with open("sequence.txt", "r") as file:
        original_sequence = ast.literal_eval(file.read())
        original_sequence = [seq.strip("[]").strip("'") for seq in original_sequence]

    for sequence in original_sequence:
        counts = collections.Counter(sequence)
        probability = {symbol: count / n_seq for symbol, count in counts.items()}
        entropy = -sum(p * math.log2(p) for p in probability.values())
        original_sequence_len = 16 * len(sequence)

        encoded_sequence, encoded = encode_rle(sequence)
        decoded_sequence = decode_rle(encoded)
        compression_ratio_RLE = round((len(sequence) / len(encoded_sequence)), 2)
        if compression_ratio_RLE < 1:
            compression_ratio_RLE = '-'
        else:
            compression_ratio_RLE = compression_ratio_RLE


        with open("results_rle_lzw.txt", "a") as file:
            file.write("Оригінальна послідовність  " + str(sequence) + "\n")
            file.write("Розмір оригінальної послідовності " + str(original_sequence_len) + 'bits' + "\n")
            file.write("Ентропія " + str(entropy) + "\n")
            file.write("_______Кодування RLE_______" + "\n")
            file.write("Розмір закодованої RLE послідовності " + str(len(encoded_sequence)) + "\n")
            file.write("Коефіцієнт стисення RLE " + str(compression_ratio_RLE) + "\n")
            file.write("Декодована RLE послідовність " + str(decoded_sequence) + "\n")
            file.write("Розмір декодованої RLE послідовності " + str(len(decoded_sequence)) + "\n")
            file.write("_______Кодування LZW_______" + "\n")
            file.write("__________Словник__________" + "\n")
            # print(f"Декодована LZW послідовність:{decoded_sequence} \n"
            #       f"Розмір декодованої LZW послідовності: {len(decoded_sequence) * 16} bits \n", file=file)

        encoded_sequence_LZW, size, compression_ratio_LZW = encode_lzw(sequence)
        decoded_sequence_LZW = decode_lzw(encoded_sequence_LZW)

        if compression_ratio_LZW < 1:
            compression_ratio_LZW = '-'
        else:
            compression_ratio_LZW = compression_ratio_LZW

        results.append([round((entropy), 2), compression_ratio_RLE, compression_ratio_LZW])
    N = 8
    fig, ax = plt.subplots(figsize=(14 / 1.54, N / 1.54))
    headers = ['Ентропія', 'КС RLE', 'КС LZW']
    row = ['Послідовність 1', 'Послідовність 2', 'Послідовність 3', 'Послідовність 4', 'Послідовність 5',
           'Послідовність 6', 'Послідовність 7', 'Послідовність 8']
    ax.axis('off')
    table = ax.table(cellText=results, colLabels=headers, rowLabels=row,
                     loc='center', cellLoc='center')
    table.set_fontsize(14)
    table.scale(0.8, 2)
    title = 'Результати стиснення методами RLE та LZW'
    fig.savefig(title + '.png')


def encode_rle(sequence):
    result = []
    count = 1

    for i, item in enumerate(sequence):
        if i == 0:
            continue
        elif item == sequence[i-1]:
            count +=1
        else:
            result.append((sequence[i - 1], count))
            count = 1

    result.append((sequence[len(sequence) - 1], count))

    encoded = []
    for i, item in enumerate(result):
        encoded.append(f"{item[1]}{item[0]}")

    return "".join(encoded), result


def decode_rle(sequence):
    result = []
    for item in sequence:
        result.append(item[0] * item[1])
    return "".join(result)


def encode_lzw(sequence):

    result = []
    dictionary = {}
    size = 0
    # element_bits = []
    for i in range(65536):
        dictionary[chr(i)] = i
        # dictionary[i] = chr(i)
    current = ""
    for c in sequence:
        new_str = current + c

        if new_str in dictionary:
            current = new_str
        else:
            result.append(dictionary[current])
            dictionary[new_str] = len(dictionary)
            element_bits = 16 if dictionary[current] < 65536 else math.ceil(math.log2(len(dictionary)))

            with open("results_rle_lzw.txt", "a") as file:
                file.write(f"Code: {dictionary[current]}, Element: {current},bits: {element_bits}\n")
            size = size + element_bits
            current = c
    last = 16 if dictionary[current] < 65536 else math.ceil(math.log2(len(dictionary)))
    size = size + last
    compression_ratio_LZW = round((len(sequence) * 16 / size), 2)


    with open("results_rle_lzw.txt", "a") as file:
        file.write(f"Code: {dictionary[current]}, Element: {current}, Bits: {last}\n"
                   "-----------------------------" + '\n')
    result.append(dictionary[current])
    with open("results_rle_lzw.txt", "a") as file:
        file.write(f"Закодована LZW послідовність:{''.join(map(str, result))} \n")
        file.write(f"Розмір закодованої LZW послідовності: {size} bits \n")
        file.write("Коефіцієнт стисення RLE " + str(compression_ratio_LZW) + "\n")

    return result, size, compression_ratio_LZW


def decode_lzw(sequence):
    dictionary = {}
    for i in range(65536):
        dictionary[i] = chr(i)
    result = ""
    previous = None
    current = ""

    for code in sequence:
        if code in dictionary:
            current = dictionary[code]
            result += current
            if previous is not None:
                dictionary[len(dictionary)] = previous + current[0]
            previous = current
        else:
            current = previous + previous[0]
            result += current
            dictionary[len(dictionary)] = current
            previous = current
    return result


if __name__ == "__main__":
    main()
