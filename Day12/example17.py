from threading import Thread
from time import sleep


def output(content):
    while True:
        print(content, end='')  # This is an endless loop, so we need to kill it manually.
    # The main thread will be blocked until the daemon thread is finished.
    # So we need to kill the main thread manually.


def main():
    Thread(target=output, args=('Ping',), daemon=True).start()
    Thread(target=output, args=('Pong',), daemon=True).start()
    sleep(5)
    print('bye!')


if __name__ == '__main__':
    main()
