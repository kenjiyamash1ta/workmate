from tabulate import tabulate
from cli.parser import parse
from core.reader import read_csv
from core.filter import filter_data
from core.aggregator import aggregate_data


def main():
    args = parse()
    data = read_csv(args["file"])

    if args["where"]:
        data = filter_data(data, args["where"])

    if args["aggregate"]:
        result = aggregate_data(data, args["aggregate"])
        print(tabulate([result], headers="keys", tablefmt="grid"))
    else:
        print(tabulate(data, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
