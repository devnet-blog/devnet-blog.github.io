Title: Set logger 
Date: 4.04.2022  
Author: Damian Dec
Category: Snippets
Tags: logger, logging

#How to create useful logger

When you worked with API, SSH or other interactive interface sometimes could be hard to debug issue related to your 
code because of very limited information in the console and error messages inaccurate.

To solve that issue you can set up logger session with relevant debug information during testing your code as below:
```python
def set_logger(console_level='DEBUG', file_level='DEBUG', file_name='debug.log',
               formatter='%(asctime)-15s %(relativeCreated)6d; %(threadName)-12s; %(levelname)-8s; %(message)s', level=None):
    """
    Setup logging to file and console from root.
    Args:
        console_level: Logging level in console
        file_level: Logging level in file
        file_name: Log's filename
        formatter: Formatter for both
        level: Override file_level and console_level arguments.

    Returns: logging.Logger

    """

    import logging
    if level is not None:
        file_level = level
        console_level = level

    # MAIN LOGGER
    formatter = logging.Formatter(formatter)
    _logger = logging.getLogger()
    _logger.setLevel('NOTSET')

    # FILE HANDLER
    file_handler = logging.FileHandler(file_name)
    file_handler.setLevel(file_level)
    file_handler.setFormatter(formatter)
    _logger.addHandler(file_handler)

    # CONSOLE HANDLER
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(formatter)
    _logger.addHandler(console_handler)

    return _logger
```

In the result you can more easy find the issue in the session:
```python
2022-04-04 09:35:02,247   2851; Thread-1    ; INFO    ; Connected (version 2.0, client Cisco-1.25)
2022-04-04 09:35:02,247   2851; Thread-1    ; DEBUG   ; === Key exchange possibilities ===
2022-04-04 09:35:02,247   2851; Thread-1    ; DEBUG   ; kex algos: diffie-hellman-group1-sha1
2022-04-04 09:35:02,247   2851; Thread-1    ; DEBUG   ; server key: ssh-rsa
2022-04-04 09:35:02,247   2851; Thread-1    ; DEBUG   ; client encrypt: aes128-cbc, 3des-cbc, aes192-cbc, aes256-cbc
2022-04-04 09:35:02,248   2852; Thread-1    ; DEBUG   ; server encrypt: aes128-cbc, 3des-cbc, aes192-cbc, aes256-cbc
2022-04-04 09:35:02,248   2852; Thread-1    ; DEBUG   ; client mac: hmac-sha1, hmac-sha1-96, hmac-md5, hmac-md5-96
2022-04-04 09:35:02,248   2852; Thread-1    ; DEBUG   ; server mac: hmac-sha1, hmac-sha1-96, hmac-md5, hmac-md5-96
2022-04-04 09:35:02,248   2852; Thread-1    ; DEBUG   ; client compress: none
2022-04-04 09:35:02,248   2852; Thread-1    ; DEBUG   ; server compress: none
2022-04-04 09:35:02,248   2852; Thread-1    ; DEBUG   ; client lang: <none>
```