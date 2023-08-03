from .controllers.app import app
from flask_migrate import Migrate, upgrade, downgrade, migrate

from coins import create_app, db

app = create_app()
app.app_context().push()

migrate = Migrate(app, db)

@app.cli.command('db_upgrade')
def db_upgrade():
    upgrade()

@app.cli.command('db_downgrade')
def db_downgrade():
    downgrade()

@app.cli.command('db_migrate')
def db_migrate():
    migrate()

if __name__ == '__main__':
    app.run()
