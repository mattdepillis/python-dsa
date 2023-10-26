"""

"""
def underscorify_substring(string, substring):
    underscorified = ""
    last_found_index = 0

    while last_found_index < len(string):
        # print(f"last_found_index: {last_found_index}")
        # print(f"string to search: {string[last_found_index:]}")
        substr_index = string[last_found_index:].find(substring)
        print(f"substr_index: {substr_index}")

        if substr_index < 0:
            print(f"could not find substring in the current string")
            break

        underscorified += string[last_found_index : last_found_index + substr_index]
        matched, last_found_index = f"{substring}", last_found_index + substr_index

        while True:
            overlap_index, next_start_index = len(substring - 1), len(substring)

            if (last_found_index + next_start_index < len(string)
            ) and (string[last_found_index + next_start_index] == substring[0]
            ) and string[last_found_index + next_start_index:].find(substring) == 0:
                matched += substring
                last_found_index += next_start_index

            elif (last_found_index + overlap_index < len(string)
            ) and (string[last_found_index + overlap_index] == substring[0]
            ) and string[last_found_index + overlap_index:].find(substring) == 0:
                matched += substring[1:]
                last_found_index += overlap_index

            else: break

        last_found_index += len(substring)

    underscorified += string[last_found_index:]
    return underscorified


if __name__ == "__main__":
    print(underscorify_substring(
        "testthis is a testtest to see if testestest it works",
        "test"
    ))