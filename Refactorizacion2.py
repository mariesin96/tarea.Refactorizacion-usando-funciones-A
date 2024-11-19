def process_string(data):
    print(f"Processing string: {data}")

def process_integer(data):
    print(f"Processing integer: {data}")

def process_list(data):
    print("Processing list:")
    for item in data:
        print(f" - {item}")


def process_data(data):
    processors = {
        str: process_string,  
        int: process_integer, 
        list: process_list  
    }
    
    processor = processors.get(type(data), lambda x: print("Unknown data type!"))
    processor(data)

# Ejemplo de uso
if __name__ == "__main__":

    process_data("Hello")  
    process_data(123)     
    process_data([1, 2, 3]) 
    process_data(3.14)     