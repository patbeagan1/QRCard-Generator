import sys


def format_single_entry(index: int):
    url = f"https://www.gutenberg.org/ebooks/{index}"
    image_url = f"https://www.gutenberg.org/cache/epub/{index}/pg{index}.cover.medium.jpg"
    return f"{url},{image_url}\n"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Requires a starting index.")
        print(f"Usage: {sys.argv[0]} <index> [amount to gen]")
        exit(1)
    index = int(sys.argv[1])
    amount = 20
    if len(sys.argv) >= 3:
        amount = int(sys.argv[2])
    with open("out.csv", "w") as f:
        for i in range(index, index + amount):
            f.write(format_single_entry(i))
