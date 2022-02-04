#!/usr/bin/env python3

import os
import typer
import configparser

from pathlib import Path

APP_NAME = "gscerts"
CONFIG_FILENAME = "config.ini"

class Helper(object):
    """
    Helper class
    """

    def __init__(self):
        self.app_dir = typer.get_app_dir(APP_NAME)
        self.app_config_file : Path = Path(self.app_dir) / CONFIG_FILENAME
        self.auth_info = dict()
        self.contact_info = dict()
        self.create_config_path()

    def create_config_path(self):
        """ create empty config directory """
        app_dir_path = Path(self.app_dir)
        if app_dir_path.exists():
            return 0
        else:
            app_dir_path.mkdir(parents=True, exist_ok=True)

    def write_config(self, config):
        """ write config file """
        with open(self.app_config_file, "w") as configfile:
            config.write(configfile)

    def auth(self, username, password=False):
        """ get information about authentication """
        config = configparser.ConfigParser()
        config.read(self.app_config_file)
        try:
            config.add_section("auth")
        except configparser.DuplicateSectionError:
            pass
        config["auth"]["username"] = username
        if password != "":
            config["auth"]["password"] = password
        self.write_config(config)

    def contact_info(self, first_name, last_name, phone, email):
        """ set information about contact """
        config = configparser.ConfigParser()
        config.read(self.app_config_file)
        try:
            config.add_section("contact_info")
        except configparser.DuplicateSectionError:
            pass
        contact_info = {
                "first_name": first_name,
                "last_name": last_name,
                "phone": phone,
                "email": email
                }
        config["contact_info"] = contact_info
        self.write_config(config)
