def main() -> None:
    # Get the file name from the user
    file_name = input("Enter name of the file: ")

    # Ensure the file has a .txt extension
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    content_lines = []

    # Keep asking for new lines of content
    while True:
        new_line = input("Enter new line of content: ")
        if new_line.lower() == "stop":
            break
        content_lines.append(new_line)

    # Write the collected content to the file
    with open(file_name, "w") as file:
        for line in content_lines:
            file.write(line + "\n")

    print(f'File "{file_name}" has been created.')

    # Run the function to create the file


main()


if __name__ == "__main__":
    main()
