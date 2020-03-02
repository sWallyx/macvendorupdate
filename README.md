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
  -p, --python    Updates/generates python oui file with mac vendor info
  -m, --mysql     Writes the infor of the mac vendor into the sql database
  -d, --download  Just download the oui.txt file and save it in the main folder
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

### File download error

Some users had problems downloading the file from [standards-oui.ieee.org](http://standards-oui.ieee.org/oui.txt).

``` Python
Traceback (most recent call last):
  File "/usr/lib/python3.6/urllib/request.py", line 1318, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "/usr/lib/python3.6/http/client.py", line 1254, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/usr/lib/python3.6/http/client.py", line 1300, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/usr/lib/python3.6/http/client.py", line 1249, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/usr/lib/python3.6/http/client.py", line 1036, in _send_output
    self.send(msg)
  File "/usr/lib/python3.6/http/client.py", line 974, in send
    self.connect()
  File "/usr/lib/python3.6/http/client.py", line 1415, in connect
    server_hostname=server_hostname)
  File "/usr/lib/python3.6/ssl.py", line 407, in wrap_socket
    _context=self, _session=session)
  File "/usr/lib/python3.6/ssl.py", line 817, in __init__
    self.do_handshake()
  File "/usr/lib/python3.6/ssl.py", line 1077, in do_handshake
    self._sslobj.do_handshake()
  File "/usr/lib/python3.6/ssl.py", line 689, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:852)
```

This is the error they get. We are currently working in this issue. Please create an issue with you OS and Python version.

## FAQ

### Do I have Python 3?

To know if you have Python 3 in the machine run the command: `python -V`

_Note:_ Some machines may have the `python` command for Python 2 and `python3 `command for Python 3


### How can upgrade to Python 3?

* For linux: [This guide](https://jcutrer.com/linux/upgrade-python37-ubuntu1810).
* For Mac OS: [This guide](https://osxdaily.com/2018/06/13/how-install-update-python-3x-mac/).


# ToDo list

* [ ] Option for local file, and exit download
* [ ] Option to update database and remove the need of empty database
* [ ] Automatize virtual enviroment creation
* [ ] Create new install bash script to start the enviroment also

License
----

[MIT - License](LICENSE)
