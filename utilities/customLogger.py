import logging
import os


class LogGen:
    @staticmethod
    def log_gen():
        # Ensure the logs directory exists
        if not os.path.exists('.\\logs'):
            try:
                os.makedirs('.\\logs')
            except PermissionError as e:
                print(f"Error creating log directory: {e}")
                raise
            except Exception as e:
                print(f"Unexpected error creating log directory: {e}")
                raise

        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
