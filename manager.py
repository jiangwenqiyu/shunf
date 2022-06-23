from apps import create_app
from flask_script import Manager
import threading
from apps.common.sendEmail import begin

app = create_app()
manager = Manager(app)


if __name__ == '__main__':
    threading.Thread(target=begin).start()
    manager.run()

