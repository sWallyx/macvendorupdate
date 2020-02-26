from macvendorToMysql import updateMysql
from macVendorToPython import updatePython
import click

class DefaultHelp(click.Command):
    def __init__(self, *args, **kwargs):
        context_settings = kwargs.setdefault('context_settings', {})
        if 'help_option_names' not in context_settings:
            context_settings['help_option_names'] = ['-h', '--help']
        self.help_flag = context_settings['help_option_names'][0]
        super(DefaultHelp, self).__init__(*args, **kwargs)

    def parse_args(self, ctx, args):
        if not args:
            args = [self.help_flag]
        return super(DefaultHelp, self).parse_args(ctx, args)

@click.command(cls=DefaultHelp)
@click.option('-p', '--python', is_flag=True, help='Updates/generates python oui file with mac vendor info')
@click.option('-m', '--mysql', is_flag=True, help='Writes the infor of the mac vendor into the sql database')
def main(python = False, mysql = False):
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

    if(python):
        updatePython()

    elif(mysql):
        updateMysql()


if __name__ == '__main__':
    main()
