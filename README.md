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
* urllib
* sys
* mysql.connector
* pathlib
* os

## Requisites

The unique requisite is "click", you can run the following command to install it.

```
python setup.py install
```


License
----

MIT