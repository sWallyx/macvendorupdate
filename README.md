# Mac Vendor Update

Diferent ways to update the mac vendor files, using the official oui.txt from [standards-oui.ieee.org](http://standards-oui.ieee.org/oui.txt). The files downloads the file and saves it in diferent ways and places for example:

  - Python file
  - MySQL database
  - ...

# Usage

### Command examples

```
python macvendorupdate --help
Usage: macvendorupdate [OPTIONS]

Options:
  -p, --python  Updates/generates python oui file with mac vendor info
  -m, --mysql   Writes the infor of the mac vendor into the sql database
  --help        Show this message and exit.
```

### Python update

To write or update a python file called oui.py

```
python macvendorupdate -p
```

### Mysql update

```
python macvendorupdate -m
```

It will ask for the database info

The structure of the table it creates/needs is:
```
SQL minimal table needed by script:
-- Table: mac_vendors
-- DROP TABLE mac_vendors;
CREATE TABLE mac_vendors
(
  oui character varying(8) NOT NULL,
  vendor character varying NOT NULL,
  id serial NOT NULL,
  CONSTRAINT pk_mac_vendors PRIMARY KEY (oui)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE mac_vendors
  OWNER TO DBUSER;
  
```

### Used modules

* re
* urllib.request
* sys
* mysql.connector
* pathlib
* os
* click

## Requisites

The application is made for Python 3 or higher. To install the requisites you can run:

```
python setup.py install
```

## Know errors

### Permision error

Some users had problems installing because of the permisions. You can create a virtual enviroment for this application with (you need to have `venv` installed):

``` bash
python3 -m venv env     # Create virtual env
source env/bin/activate # Activates the enviroment
```

Quit the enviroment with `deactivate`

## FAQ

### Do I have Python 3?

To know if you have Python 3 in the machine run the command: `python -V`

_Note:_ Some machines may have the `python` command for Python 2 and `python3 `command for Python 3


### How can upgrade to Python 3?

If you have Linux follow [this guide](https://jcutrer.com/linux/upgrade-python37-ubuntu1810).


# ToDo list

* [ ] Option for local file, and exit download
* [ ] Option to update database and remove the need of empty database
* [ ] Automatize virtual enviroment creation
* [ ] Create new install bash script to start the enviroment also

License
----

[MIT - License](LICENSE)
