import subprocess
import datetime
import os

# Set the path and name of the log file
log_dir = 'logs/'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

while True:
    now = datetime.datetime.now()
    log_file_name = "{}:{}:{}:{}:{}:{}.log".format(now.month, now.day, now.year, now.hour, now.minute, now.second)
    log_file_path = os.path.join(log_dir, log_file_name)

    # Run the command to detect processes and output to the log file
    process = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
    output = process.communicate()[0]

    # Write the output to the log file
    with open(log_file_path, 'wb') as f:
        f.write(output)

    # Print the output to the console
    print(output)

    # Delete old log files
    days_to_keep_logs = 30
    for filename in os.listdir(log_dir):
        file_path = os.path.join(log_dir, filename)
        creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        if (now - creation_time).days > days_to_keep_logs:
            os.remove(file_path)

