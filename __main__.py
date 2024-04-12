import sass
import sys


def check_dependencies():
    try:
        import sass
    except ImportError:
        print("Required dependency 'libsass' is not installed.")
        print("Please install it by running: pip install libsass")
        sys.exit(1)


def compile_sass_to_css(input_file, output_file):
    try:
        compiled_css = sass.compile(filename=input_file)
        with open(output_file, 'w') as css_stylesheet:
            css_stylesheet.write(compiled_css)
        print(f"Successfully compiled {input_file} to {output_file}")
    except Exception as e:
        print(f"Error compiling SCSS: {e}")


def convert_css_to_tailwind(input_file, output_file):
    tailwind_classes = set()

    with open(input_file, 'r') as stylesheet:
        for line in stylesheet:
            # Skip empty lines and comments
            if not line.strip() or line.strip().startswith('//') or line.strip().startswith('/*'):
                continue

            # Split the line into selector and properties
            parts = line.split('{')
            if len(parts) != 2:
                continue

            selector = parts[0].strip()
            properties = parts[1].split('}')[0].strip()

            # Process properties
            for prop in properties.split(';'):
                if ':' in prop:
                    prop_name, prop_value = prop.split(':')
                    prop_name = prop_name.strip()
                    prop_value = prop_value.strip()

                    # Map properties to Tailwind classes
                    if prop_name == 'color':
                        tailwind_classes.add(f"text-{prop_value}")
                    elif prop_name == 'background-color':
                        tailwind_classes.add(f"bg-{prop_value}")
                    elif prop_name == 'font-size':
                        tailwind_classes.add(f"text-{prop_value}")
                    # Add more property mappings as needed...

    # Write the Tailwind CSS classes to the output file
    with open(output_file, 'w') as output:
        for tw_class in tailwind_classes:
            output.write(f".{tw_class} {{\n    /* Your Tailwind CSS styles here */\n}}\n\n")


if __name__ == "__main__":
    check_dependencies()
    sass_file = input("Please enter the location of the SASS file: ")
    css_file = "styles.css"
    compile_sass_to_css(sass_file, css_file)
    #convert_css_to_tailwind(css_file, "tailwind.css")
