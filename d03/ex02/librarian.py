import os
import subprocess
import sys
import pkg_resources


def install_packages(package_list):
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", *package_list])


def main():
    env_name = 'poligon'
    libs = ['beautifulsoup4', 'pytest']
    if not os.environ.get('VIRTUAL_ENV', 'None').endswith(env_name):
        raise EnvironmentError(
            f'Script must work in venv with name: {env_name}')
    install_packages(libs)
    installed_dist = sorted(
        [f"{i.key}=={i.version}" for i in pkg_resources.working_set])
    print(*installed_dist, sep='\n')
    with open('requirements.txt', 'w') as req:
        print(*installed_dist, sep='\n', file=req)


if __name__ == "__main__":
    main()
