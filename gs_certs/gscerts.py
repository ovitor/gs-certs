#!/usr/bin/env python3

import typer

from .helper import Helper

app = typer.Typer()

@app.command()
def auth(username:str = typer.Option("", prompt=True, envvar="GS_USERNAME"), password:str = typer.Option("", prompt=True, envvar="GS_PASSWORD")):
    helper = Helper()
    if username == "":
        typer.echo(f"Username can't be empty.")
    helper.auth(username, password)

@app.command()
def contact_info(
    first_name:str = typer.Option(""),
    last_name:str = typer.Option(""),
    phone:str = typer.Option(""),
    email:str = typer.Option("")):
    helper = Helper()
    helper.contact_info(first_name, last_name, phone, email)

@app.command()
def organization_info(
        name:str = typer.Option(""),
        address:str = typer.Option(""),
        city:str = typer.Option(""),
        region:str = typer.Option(""),
        postal_code:str = typer.Option(""),
        country:str = typer.Option(""),
        phone:str = typer.Option("")):

    helper = Helper()
    helper.contact_info(name, address, city, region, postal_code, country, phone)

@app.command()
def request_cert(csr_file: typer.FileText = typer.Option("")):
    typer.echo(f"{''.join(csr_file.readlines())}")

if __name__ == "__main__":
    app()
