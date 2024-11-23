import os
import sys
import markdown

def display_help():
    print("Usage: python3 file-converter.py markdown <input file> <output file>")
    print("Converts the input .md file to the output .html file.")
    sys.exit(1)

if len(sys.argv) < 4:
    display_help()

elif sys.argv[1] != "markdown":
    display_help()

else:
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    input_extension = os.path.splitext(input_file)[1]
    output_extension = os.path.splitext(output_file)[1]

    if input_extension != ".md":
        print("Input file must be a markdown file")
        sys.exit(1)

    if output_extension != ".html":
        output_file = output_file + ".html"

    with open(input_file, "r") as file:
        markdown_contents = file.read()
        html_contents = markdown.markdown(markdown_contents, extensions=["tables"])

    with open(output_file, "w") as file:
        file.write(html_contents)

    print(f"Converted {input_file} to {output_file} successfully.")

sys.exit(0)
