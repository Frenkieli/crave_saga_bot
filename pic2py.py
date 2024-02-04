import os
import base64

def pic2str(directory, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(directory):
            for filename in files:
                if filename.endswith(('.png', '.jpg', '.jpeg', '.ico', '.gif')):
                    file_path = os.path.join(root, filename)
                    with open(file_path, 'rb') as image_file:
                        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

                    # Create a valid Python variable name from the filename
                    # Use the relative path to create a more unique variable name and replace invalid characters
                    relative_path = os.path.relpath(file_path, directory)
                    var_name_base = relative_path.replace(os.path.sep, '_').replace('-', '_').replace(' ', '_')
                    var_name = os.path.splitext(var_name_base)[0]

                    f.write(f"{var_name} = '{encoded_string}'\n\n")

if __name__ == '__main__':
    pic2str('assets/images', 'src/static/pic2str.py')
