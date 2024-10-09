











def read_file(filename) -> None:
    with open(filename, "r") as f:
        for line in f:
            print(line)
    with open(filename, "r") as f:
        for line in f:
            print(line, end="")

def new_file(filename) -> None:
    """
    Creates a new file and writes data to it, OR overwrites an existing file.
    """
    with open(filename, "w") as f:
        f.write("Maine Coon")

def append_file(filename, data) -> None:
    """
    Appends data to an existing file.
    """
    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "a") as f:
        f.write("\n")
        f.write(data)


def main():
    """
    Main entry point of the application.
    """
    user_submission = input("The Name of a Cat: ")
    append_file("cats.txt", user_submission)


if __name__ == "__main__":
    """
    Starts the program.
    """
    main()