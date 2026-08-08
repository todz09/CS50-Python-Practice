import argparse

parse = argparse.ArgumentParser(description="Meow like a cat")
parse.add_argument("-n", type=int, default=1, help="Number of times to meow")
args = parse.parse_args()

for _ in range(args.n):
    print("Meow!")