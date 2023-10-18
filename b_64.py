
import base64

def encode_source_code(encoded_file, output_file):
    with open(encoded_file, 'r') as encoded:
        encoded_code = encoded.read()

    # kodi base64
    encoded_code_base64 = base64.b64encode(encoded_code.encode()).decode()

    # zapissss
    with open(output_file, 'w') as output:
        output.write("# To jest zakodowany kod w base64\n")
        output.write("import base64\n")
        output.write("exec(base64.b64decode(")
        output.write(f"'{encoded_code_base64}'.encode()).decode())")

if __name__ == "__main__":
    encoded_file = "encrypted_program.py"
    output_file = "encoded_program.py"

    encode_source_code(encoded_file, output_file)
    print(f"The encoded code has been saved to {output_file}")