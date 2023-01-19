import argparse


def add(x, y):
    return x + y


def main():
    parser = argparse.ArgumentParser(description="Sample Python program")
    parser.add_argument("x", help="value of x", type=int)
    parser.add_argument("y", help="value of y", type=int)
    args = parser.parse_args()
    print(add(args.x, args.y))


if __name__ == "__main__":
    main()
