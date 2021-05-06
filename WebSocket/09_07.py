import multiprocessing as mp
import time

def worker():
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)
    time.sleep(5)
    print("SubProcess End")

# 다른 파이썬 파일에서 해당 모듈을 끌어다 쓸 때
# __name__ == " __main__"부분은 제외하고 실행된다.
if __name__ == "__main__":
    # main process
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)

    # process spawning
    p = mp.Process(name="SubProcess", target=worker)
    p.start()

    print("MainProcess End")

# 5초 동안 대기하기 때문에 'SubProcess End'가 가장 마지막에 출력