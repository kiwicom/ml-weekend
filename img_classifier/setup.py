#!/usr/bin/env python

import logging
import os
import subprocess
import sys
import init_env

init_env.init()

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


PATH_TO_PACKAGE = os.environ.get("DATALAB_ROOT") + "ml-weekend/img_classifier/"

DATA_URL = "https://storage.googleapis.com/airliners/fgvc-aircraft-2013b.zip"

logging.info("Running installation...")
subprocess.call(["mkdir", os.environ.get("DATALAB_ROOT") + "data"])
subprocess.call(["mkdir", os.environ.get("DATALAB_ROOT") + "notebooks"])

logging.info("Folders created")
logging.info("Downloading dataset...")
subprocess.call(["wget", DATA_URL, "-P", os.environ.get("DATALAB_ROOT") + "data/"])

logging.info("..done")
logging.info("Unpacking archive to data/")
subprocess.call(["unzip", "-q", os.environ.get("DATALAB_ROOT") + "data/" + DATA_URL.split("/")[-1], "-d",
                 os.environ.get("DATALAB_ROOT") + "data/"])

logging.info("..done")
logging.info("Installing requirements")
subprocess.call(["pip3", "install", "-r", PATH_TO_PACKAGE+"requirements.txt"])
subprocess.call(["pip2", "install", "tensorboard"])

# logging.info("Upgrading keras")
# subprocess.call(["pip3", "install", "git+git://github.com/fchollet/keras.git", "--upgrade"])

logging.info("Copying notebook to notebooks")
subprocess.call(["cp", PATH_TO_PACKAGE + "aircrafts_cnn.ipynb", os.environ.get("DATALAB_ROOT") + "notebooks/"])
logging.info("Finished")
