import sys
import os
import pathlib
import click

from macvendorToMysql import *
from macVendorToPython import *


@click.command()
@click.option('-p', '--python', is_flag=True, help='Updates/generates python oui file with mac vendor info')
@click.option('-m', '--mysql', is_flag=True, help='Writes the infor of the mac vendor into the sql database')
def main(python, mysql):
    print('''
    __  ___              _    __               __              __  __          __      __     
   /  |/  /___ ______   | |  / /__  ____  ____/ /___  _____   / / / /___  ____/ /___ _/ /____ 
  / /|_/ / __ `/ ___/   | | / / _ \/ __ \/ __  / __ \/ ___/  / / / / __ \/ __  / __ `/ __/ _ \ 
 / /  / / /_/ / /__     | |/ /  __/ / / / /_/ / /_/ / /     / /_/ / /_/ / /_/ / /_/ / /_/  __/
/_/  /_/\__,_/\___/     |___/\___/_/ /_/\__,_/\____/_/      \____/ .___/\__,_/\__,_/\__/\___/ 
                                                                /_/                           
     ''')

    if(python):
        updatePython()

    if(mysql):
        updateMysql()


if __name__ == '__main__':
    main()
