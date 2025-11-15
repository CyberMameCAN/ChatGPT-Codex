# my_thread.py
# Python-izm の サンプルコードを参考にしています。
# https://www.python-izm.com/advanced/thread/
#
import threading
import time
from datetime import datetime
 
class MyThread(threading.Thread):
 
    def run(self):
        print('[start] Sub thread')
        sub_interval = 3
        for i in range(5):
            time.sleep(sub_interval)
            print(f'✅ sub thread: ({sub_interval}s間隔) ' + str(datetime.today()))
        print('[end] Sub thread')

def main():
    th = MyThread()
    # Start the thread
    # (新しいスレッドが作成され、そのスレッドでrunメソッドが実行される)
    th.start()
    
    time.sleep(1)

    print('[start] Main thread')
    main_interval = 7
    for i in range(3):
        time.sleep(main_interval)
        print(f'⭐ main thread: ({main_interval}s間隔)' + str(datetime.today()))
    print('[end] Main thread')


if __name__ == '__main__':
    main()
