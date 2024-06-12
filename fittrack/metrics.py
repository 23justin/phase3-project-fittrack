import click
from fittrack.database import SessionLocal
from fittrack.db.models import Metric

@click.command()
@click.argument('name')
@click.argument('value', type=float)  # Specify the type for value as float
def add_metric(name, value):
    """Add a new metric."""
    session = SessionLocal()
    try:
        metric = Metric(name=name, value=value)
        session.add(metric)
        session.commit()
        click.echo(f"Metric '{name}' added with value {value}.")
    except Exception as e:
        session.rollback()
        click.echo(f"Error: Failed to add metric '{name}' with value {value}.")
        click.echo(str(e))
    finally:
        session.close()

@click.command()
def view_metrics():
    """View all metrics."""
    session = SessionLocal()
    try:
        metrics = session.query(Metric).all()
        for metric in metrics:
            click.echo(f"{metric.name}: {metric.value}")
    except Exception as e:
        click.echo("Error: Failed to retrieve metrics.")
        click.echo(str(e))
    finally:
        session.close()

# Entry point for running the CLI commands
if __name__ == '__main__':
    add_metric()
    view_metrics()
