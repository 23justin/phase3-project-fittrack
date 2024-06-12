import click
from fittrack.database import SessionLocal
from fittrack.db.models import Goal

@click.command()
@click.argument('name')
@click.argument('target', type=int)  # Specify the type for target as int
def set_goal(name, target):
    """Set a new goal."""
    session = SessionLocal()
    try:
        goal = Goal(name=name, target=target)
        session.add(goal)
        session.commit()
        click.echo(f"Goal '{name}' set with target {target}.")
    except Exception as e:
        session.rollback()
        click.echo(f"Error: Failed to set goal '{name}' with target {target}.")
        click.echo(str(e))
    finally:
        session.close()

@click.command()
def view_goals():
    """View all goals."""
    session = SessionLocal()
    try:
        goals = session.query(Goal).all()
        for goal in goals:
            click.echo(f"{goal.name}: target {goal.target}")
    except Exception as e:
        click.echo("Error: Failed to retrieve goals.")
        click.echo(str(e))
    finally:
        session.close()

# Entry point for running the CLI commands
if __name__ == '__main__':
    set_goal()
    view_goals()
