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

The application is made for Python 3 or higher. Check your version with `python -V`

To install the requisites you can run:

```
python setup.py install
```

## Know errors

Some users had problems installing because of the permisions. You can create a virtual enviroment for this application with (you need to have `venv` installed):

``` bash
python3 -m venv env     # Create virtual env
source env/bin/activate # Activates the enviroment
```

Quit the enviroment with `deactivate`

# ToDo list

* [ ] Option for local file, and exit download
* [ ] Option to update database and remove the need of empty database
* [ ] Automatize virtual enviroment creation
* [ ] Add venv to setup file

License
----

[MIT - License](LICENSE)
