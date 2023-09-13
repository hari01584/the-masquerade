import click

@click.group()
def app():
    """Masking yourself, masquerade as someone else."""

@app.command(name="extract")
@click.argument("filepath", metavar="FILE", type=click.Path(exists=True))
def load_(filepath):
    """Print the file."""
    print(f"Loading file {filepath}")

    # print("-" * 80)

    # with open(filepath, "r") as f:
    #     print(f.read())


@app.command(name="load")
@click.argument("filepath", metavar="FILE", type=click.Path(exists=True))
def load_(filepath):
    """Print the file."""
    print(f"Loading file {filepath}")
    
    # print("-" * 80)

    # with open(filepath, "r") as f:
    #     print(f.read())


@app.command(name="craft")
@click.argument("company_name")
def load_(company_name):
    """Print the file."""
    print(f"Creating a good cold emailing format for {company_name}")
    
    # What does this org/company do?
    
    # print("-" * 80)

    # with open(filepath, "r") as f:
    #     print(f.read())
    

if __name__ == "__main__":
    app()
