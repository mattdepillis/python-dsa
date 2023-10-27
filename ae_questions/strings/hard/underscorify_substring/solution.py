"""

"""
def underscorify_substring(string, substring):
    underscorified = ""
    start_indices = []
    start_index = 0

    while start_index < len(string):
        substr_start_index = string[start_index:].find(substring)
        if substr_start_index < 0: break
        start_indices.append(start_index + substr_start_index)
        start_index = start_index + substr_start_index + len(substring) - 1

    for i, start_index in enumerate(start_indices):

        if i == 0 or start_index - start_indices[i - 1] > len(substring):
            underscorified += "_"

        end_index = len(string) if i == len(start_indices) - 1 else start_indices[i + 1]
        end_substr_to_add_index = start_index + min(end_index - start_index, len(substring))

        underscorified += string[start_index : end_substr_to_add_index]

        if i == len(start_indices) - 1 or end_substr_to_add_index < start_indices[i + 1]:
            underscorified += "_"

        underscorified += string[end_substr_to_add_index : end_index]

    return underscorified


if __name__ == "__main__":
    print(underscorify_substring(
        "testthis is a testtest to see if testestest it works",
        "test"
    ))