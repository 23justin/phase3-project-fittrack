import click
from fittrack.database import SessionLocal
from fittrack.db.models import Nutrition

@click.command()
@click.argument('item')
@click.argument('calories', type=int)
def log_nutrition(item, calories):
    """Log a nutrition item."""
    session = SessionLocal()
    try:
        nutrition = Nutrition(item=item, calories=calories)
        session.add(nutrition)
        session.commit()
        click.echo(f"Nutrition item '{item}' logged with {calories} calories.")
    except Exception as e:
        session.rollback()
        click.echo(f"Error: Failed to log nutrition item '{item}' with {calories} calories.")
        click.echo(str(e))
    finally:
        session.close()

@click.command()
def view_nutrition():
    """View all nutrition logs."""
    session = SessionLocal()
    try:
        nutrition_logs = session.query(Nutrition).all()
        if nutrition_logs:
            for log in nutrition_logs:
                click.echo(f"{log.item}: {log.calories} calories")
        else:
            click.echo("No nutrition logs found.")
    except Exception as e:
        click.echo("Error: Failed to retrieve nutrition logs.")
        click.echo(str(e))
    finally:
        session.close()

# Entry point for running the CLI commands
if __name__ == '__main__':
    log_nutrition()
    view_nutrition()
