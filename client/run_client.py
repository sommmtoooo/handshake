from handshake import run_instance
from multiprocessing import Process
    

# Two Client Instance
if __name__ == "__main__":
    process_1 = Process(target=run_instance)
    # process_2 = Process(target=run_instance)
    # process_3 = Process(target=run_instance)

    process_1.start()
    # process_2.start()
    # process_3.start()

    process_1.join()
    # process_2.join()
    # process_3.join()



