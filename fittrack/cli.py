import click
from fittrack.database import SessionLocal, init_db
from fittrack.db.models import Activity, Metric, Nutrition, Goal, Reminder

@click.group()
def fittrack():
    """FitTrack CLI."""
    pass

@fittrack.command()
def init():
    """Initialize the database."""
    init_db()
    click.echo("Database initialized!")

@fittrack.command()
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

@fittrack.command()
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

@fittrack.command()
@click.argument('metric_name')
@click.argument('value', type=float)
def add_metric(metric_name, value):
    """Add a metric."""
    session = SessionLocal()
    try:
        metric = Metric(name=metric_name, value=value)
        session.add(metric)
        session.commit()
        click.echo(f"Metric '{metric_name}' added with value {value}.")
    except Exception as e:
        session.rollback()
        click.echo(f"Error: Failed to add metric '{metric_name}' with value {value}.")
        click.echo(str(e))
    finally:
        session.close()

@fittrack.command()
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

@fittrack.command()
@click.argument('nutrition_name')
@click.argument('calories', type=int)
def log_nutrition(nutrition_name, calories):
    """Log nutrition intake."""
    session = SessionLocal()
    try:
        nutrition = Nutrition(name=nutrition_name, calories=calories)
        session.add(nutrition)
        session.commit()
        click.echo(f"Nutrition '{nutrition_name}' logged with {calories} calories.")
    except Exception as e:
        session.rollback()
        click.echo(f"Error: Failed to log nutrition '{nutrition_name}' with {calories} calories.")
        click.echo(str(e))
    finally:
        session.close()

@fittrack.command()
def view_nutrition():
    """View all nutrition entries."""
    session = SessionLocal()
    try:
        nutritions = session.query(Nutrition).all()
        for nutrition in nutritions:
            click.echo(f"{nutrition.name}: {nutrition.calories} calories")
    except Exception as e:
        click.echo("Error: Failed to retrieve nutrition entries.")
        click.echo(str(e))
    finally:
        session.close()

@fittrack.command()
@click.argument('goal_name')
@click.argument('target', type=int)
def set_goal(goal_name, target):
    """Set a fitness goal."""
    session = SessionLocal()
    try:
        goal = Goal(name=goal_name, target=target)
        session.add(goal)
        session.commit()
        click.echo(f"Goal '{goal_name}' set with target {target}.")
    except Exception as e:
        session.rollback()
        click.echo(f"Error: Failed to set goal '{goal_name}' with target {target}.")
        click.echo(str(e))
    finally:
        session.close()

@fittrack.command()
@click.argument('reminder_name')
@click.argument('time')
def set_reminder(reminder_name, time):
    """Set a reminder."""
    session = SessionLocal()
    try:
        reminder = Reminder(name=reminder_name, time=time)
        session.add(reminder)
        session.commit()
        click.echo(f"Reminder '{reminder_name}' set for {time}.")
    except Exception as e:
        session.rollback()
        click.echo(f"Error: Failed to set reminder '{reminder_name}' for {time}.")
        click.echo(str(e))
    finally:
        session.close()

@fittrack.command()
def view_goals():
    """View all fitness goals."""
    session = SessionLocal()
    try:
        goals = session.query(Goal).all()
        for goal in goals:
            click.echo(f"{goal.name}: {goal.target}")
    except Exception as e:
        click.echo("Error: Failed to retrieve goals.")
        click.echo(str(e))
    finally:
        session.close()

@fittrack.command()
def view_reminders():
    """View all reminders."""
    session = SessionLocal()
    try:
        reminders = session.query(Reminder).all()
        for reminder in reminders:
            click.echo(f"{reminder.name}: {reminder.time}")
    except Exception as e:
        click.echo("Error: Failed to retrieve reminders.")
        click.echo(str(e))
    finally:
        session.close()

if __name__ == '__main__':
    fittrack()

