def main(all_num, process_num_list):
    '''
    Calculate for each number and Get even numbers.
    '''
    count = 0
    original_list = [0] * all_num
    for Str in process_num_list:
        number_range_list = Str.split(" ")
        start = int(number_range_list[0])
        end = int(number_range_list[1])
        for i in range(start-1, end):
            original_list[i] += 1
    for num in original_list:
        if (num % 2 == 0):
            count += 1
    print(count)

def read_input_file(file_name):
    '''
    Process the input data to int & list.
    '''
    with open(file_name, "r") as f:
        all_lines = f.read().split("\n")
    try:
        all_num = int(all_lines[0])
        count = int(all_lines[1])
        process_num_list = all_lines[2:-1]
    except ValueError:
        print("Oops! You should check your input is in the correct format...")
    assert len(process_num_list) == count, "The number of your process is not equl to assigned number."
    return all_num, process_num_list

if __name__ == "__main__":
    '''
    You could change the file_name depend on your input file.  
    '''
    file_name = "input.txt"
    all_num, process_num_list = read_input_file(file_name)
    main(all_num, process_num_list)
