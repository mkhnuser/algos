import os


def find_file(path: str, file_name: str) -> str | None:
    for listing in os.listdir(path):
        path_to_consider = os.path.join(path, listing)

        if os.path.isdir(path_to_consider):
            found_path = find_file(path_to_consider, file_name)
            if found_path is not None:
                return found_path
        else:
            if os.path.basename(path_to_consider) == file_name:
                return path_to_consider


def play_with_dolls(n):
    if n == 0:
        return

    print(f"DOLL'S NUMBER {n} HEAD HAS BEEN DETACHED!")
    play_with_dolls(n - 1)
    print(f"DOLL'S NUMBER {n} HEAD HAS BEEN ATTACHED BACK!")


def build_stairs(n):
    if n == 0:
        return
    print(n)
    build_stairs(n - 1)


def list_files(parent_directory, current_filepath=""):
    output_list = []

    for key, value in parent_directory.items():
        if value is None:
            output_list.append(current_filepath + "/" + key)
        else:
            output_list.extend(
                list_files(
                    value,
                    current_filepath=current_filepath + "/" + key,
                )
            )

    return output_list


if __name__ == "__main__":
    example = {
        "Documents": {
            "Proposal.docx": None,
            "Receipts": {
                "January": {"receipt1.txt": None, "receipt2.txt": None},
                "February": {"receipt3.txt": None},
            },
        },
    }

    assert list_files(example) == [
        "/Documents/Proposal.docx",
        "/Documents/Receipts/January/receipt1.txt",
        "/Documents/Receipts/January/receipt2.txt",
        "/Documents/Receipts/February/receipt3.txt",
    ]
