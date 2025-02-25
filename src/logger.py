import os

class Logger:
    @staticmethod
    def log(message):
        log_file = "outputs/process.log"
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        with open(log_file, 'a') as log:
            log.write(f"{message}\n")
        print(f"LOG: {message}")