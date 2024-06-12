import click
from fittrack.database import SessionLocal
from fittrack.db.models import Activity

@click.command()
@click.argument('name')
@click.argument('duration', type=int)
def log_activity(name, duration):
    """Log an activity."""
    session = SessionLocal()
    try:
        activity = Activity(name=name, duration=duration)
        session.add(activity)
        session.commit()
        click.echo(f"Activity '{name}' logged with duration {duration} minutes.")
    except Exception as e:
        session.rollback()
        click.echo(f"Error: Failed to log activity '{name}' with duration {duration}.")
        click.echo(str(e))
    finally:
        session.close()

@click.command()
def view_activities():
    """View all activities."""
    session = SessionLocal()
    try:
        activities = session.query(Activity).all()
        for activity in activities:
            click.echo(f"{activity.name}: {activity.duration} minutes")
    except Exception as e:
        click.echo("Error: Failed to retrieve activities.")
        click.echo(str(e))
    finally:
        session.close()

# Grouping commands together
@click.group()
def cli():
    """CLI commands for activities."""
    pass

# Adding commands to the CLI group
cli.add_command(log_activity)
cli.add_command(view_activities)

if __name__ == "__main__":
    cli()
