import os
import sys
import shutil

WORKDIR = os.path.expanduser("~/ops")
IMAGES_DIR = "/Users/mac/exercise/public/images"
DB_DIR = "/Users/mac/exercise/public/db"
ORIG_PWD=os.getcwd()


def validate():
    if os.system("which docker") or os.system("which docker-compose"):
        print "Please install docker and docker-compose then rerun the script"
        sys.exit(1)


def download_images():
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)
    if not os.path.exists(IMAGES_DIR):
        os.makedirs(IMAGES_DIR)
    os.system("curl https://s3.eu-central-1.amazonaws.com/devops-exercise/pandapics.tar.gz -o /tmp/pandapics.tar.gz")
    os.system("tar -xzvf /tmp/pandapics.tar.gz -C {}".format(IMAGES_DIR))
    os.system("rm -rf /tmp/pandapics.tar.gz")


def download_app():
    if not os.path.exists(WORKDIR):
        os.makedirs(WORKDIR)
    os.chdir(WORKDIR)
    if not os.path.exists("ops-exercise"):
        os.system("git clone https://github.com/bigpandaio/ops-exercise")
    shutil.copy2('{}/docker-compose.yml'.format(ORIG_PWD), 'ops-exercise/')


def run_app_db():
    os.chdir("ops-exercise")
    os.system("docker-compose up")


if __name__ == '__main__':
    validate()
    download_images()
    download_app()
    run_app_db()