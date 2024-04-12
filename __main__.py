import sass
import sys

def check_dependencies():
    try:
        import sass
    except ImportError:
        print("Required dependency 'libsass' is not installed.")
        print("Please install it by running: pip install libsass")
        sys.exit(1)

def compile_scss_to_css(input_file, output_file):
    try:
        with open(input_file, 'r') as scss_file:
            compiled_css = sass.compile(string=scss_file.read())
            with open(output_file, 'w') as css_file:
                css_file.write(compiled_css)
        print(f"Successfully compiled {input_file} to {output_file}")
    except Exception as e:
        print(f"Error compiling SCSS: {e}")

if __name__ == "__main__":
    check_dependencies()
    scss_file = input("Please enter the location of the SCSS file: ")
    css_file = "styles.css"
    compile_scss_to_css(scss_file, css_file)