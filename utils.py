def read_input(filename):
    input_file = open(filename, "r")
    # Works for not too large file
    inputs = [int(x) for x in input_file.read().split()]
    input_file.close()
    return inputs
