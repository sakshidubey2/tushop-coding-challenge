def get_min_diff_in_price(goodies, num_employees):
    goodies.sort(key=lambda x: x[1])
    min_diff = float('inf')
    selected_goodies = []

    start = 0
    end = num_employees - 1
    while end < len(goodies):
        price_diff = goodies[end][1] - goodies[start][1]
        if price_diff < min_diff:
            min_diff = price_diff
            selected_goodies = goodies[start : end + 1]
        start += 1
        end += 1
    return selected_goodies, min_diff

def main(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    num_employees = int(lines[0].split()[-1])
    goodies = []
    for line in lines[2:]:
        goodie_name, price = line.strip().split(": ")
        goodies.append((goodie_name, int(price)))

    selected_goodies, min_diff = get_min_diff_in_price(goodies, num_employees)
    print(selected_goodies, min_diff)

    with open(output_file, 'w') as file:
        file.write("The goodies selected for distribution are:\n")
        for name, price in selected_goodies:
            file.write(f"{name}: {price}\n")
        file.write(f"And the difference between the chosen goodie with the highest price and the lowest price is {min_diff}")

if __name__ == "__main__":
    input_file = "sample_input.txt"
    output_file = "sample_output.txt"
    main(input_file, output_file)

