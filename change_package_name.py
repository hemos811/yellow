import os
import subprocess

# Read the new package name from the file
package_name_file = 'package-name.txt'

if os.path.exists(package_name_file):
    with open(package_name_file, 'r') as file:
        new_package_name = file.read().strip()
    if new_package_name:
        print(f'Read new package name: {new_package_name}')

        # Run the command with the new package name
        subprocess.run(['flutter', 'pub', 'run', 'change_app_package_name:main', new_package_name])
    else:
        print('Error: New package name is empty in the file.')
else:
    print(f'Error: {package_name_file} does not exist.')
