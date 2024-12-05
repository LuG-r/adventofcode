if __name__ == '__main__':
    with open("inputs/day3_input", "r") as infile:
        do = True
        data = infile.read()
        data_ptr = 0
        result = 0 
        switch_result = 0

        while data_ptr < len(data):
            if data[data_ptr : data_ptr + 7] == "don't()":
                do = False
                data_ptr += 7
                continue
            elif data[data_ptr : data_ptr + 4] == "do()":
                do = True
                data_ptr += 4
                continue
            elif data[data_ptr : data_ptr + 4] == "mul(":
                start = data_ptr + 4
                end = data.find(')', start, start + 8)
                if end == -1:
                    data_ptr += 4
                    continue
                nums = [
                    int(x)
                    for x in data[start:end].split(",")
                    if x.isdigit() and int(x) > 0 and int(x) < 1000
                    ]
                if len(nums) == 2:
                    product = 1
                    for num in nums:
                        product *= num
                    if do:
                        switch_result += product
                    result += product
            data_ptr += 1

        print(f"Part 1 answer = {result}\nPart 2 answer = {switch_result}")