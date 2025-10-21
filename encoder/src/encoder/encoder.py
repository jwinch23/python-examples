def run_length_encode(s):
    if not s:
        return ""

    encoded = []
    count = 1

    for i in range(1, len(s)):
        print(f"Comparing {s[i]} with {s[i - 1]}")
        if s[i] == s[i - 1]:
            count += 1
            print(f"Count incremented to {count}")
        else:
            encoded.append(s[i - 1] + str(count))
            print(f"Appending {s[i - 1]}{count}")
            count = 1

    encoded.append(s[-1] + str(count))
    print(f"Appending final {s[-1]}{count}")
    return ''.join(encoded)