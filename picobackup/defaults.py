import datetime
import os.path as path

home_dir = path.expanduser('~')
app_dir = path.join(home_dir, '.picobackup')

log_file = path.join(app_dir, str(datetime.datetime.now())) + '.log'
config_dir = path.join(app_dir, 'config')
push_config_file = path.join(config_dir, 'push.conf')
pull_config_file = path.join(config_dir, 'pull.conf')
