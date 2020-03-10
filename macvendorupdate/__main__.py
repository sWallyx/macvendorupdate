import click
import subprocess

from macvendorupdate.modules.default_help import DefaultHelp
from macvendorupdate.to_mysql import update_mysql
from macvendorupdate.to_python import update_python
from macvendorupdate.misc_functions import download_file

@click.command(cls=DefaultHelp)
@click.option(
    '-p',
    '--python',
    is_flag=True,
    help='Updates/generates python oui file with mac vendor info'
)
@click.option(
    '-m',
    '--mysql',
    is_flag=True,
    help='Writes the information of the mac vendor into the sql database'
)
@click.option(
    '-d',
    '--download',
    is_flag=True,
    help='Just download the oui.txt file and save it in the main folder'
)
def main(python=False, mysql=False, download=False):
    """
        Gets all the mac address from standards.ieee.org and creates a python
        file or inserts the information into the database. All depends in what
        is selected.
    """
    print(r'''
    __  ___              _    __               __              __  __          __      __     
   /  |/  /___ ______   | |  / /__  ____  ____/ /___  _____   / / / /___  ____/ /___ _/ /____ 
  / /|_/ / __ `/ ___/   | | / / _ \/ __ \/ __  / __ \/ ___/  / / / / __ \/ __  / __ `/ __/ _ \ 
 / /  / / /_/ / /__     | |/ /  __/ / / / /_/ / /_/ / /     / /_/ / /_/ / /_/ / /_/ / /_/  __/
/_/  /_/\__,_/\___/     |___/\___/_/ /_/\__,_/\____/_/      \____/ .___/\__,_/\__,_/\__/\___/ 
                                                                /_/                           
     ''')

    if python:
        update_python()

    elif mysql:
        update_mysql()

    elif download:
        download_file()


if __name__ == '__main__':
    main()

   