import threading
import time

# simulate a shared memory space
memory = {}
# creates a lock
lock = threading.Lock()

# Worker function that creates and releases objects in the shared memory
def worker(thread_id):
    # repeat 3 times
    for i in range(3):
        # acquire the lock to make sure only the locked thread can access the shared memory
        with lock:
            # create object
            obj = "Object-" + str(thread_id) + "-" + str(i)
            # makes the object True to indicate that it is in use
            memory[obj] = True
            print("Thread", thread_id, "created", obj)

        time.sleep(0.2)

    # after the loop release the lock
    with lock:
        # release the object by setting it to False
        obj = "Object-" + str(thread_id) + "-0"
        memory[obj] = False
        print("Thread", thread_id, "released", obj)

# removes objects that are no longer in use
def garbage_collector():

    # acquire the lock to make sure only the locked thread can access the shared memory
    with lock:
        for obj in list(memory):
            # If the object is no longer in use, delete it from memory
            if memory[obj] == False:
                del memory[obj]
                print("Reclaimed", obj)

# create threads
thread1 = threading.Thread(target=worker, args=(1,))
thread2 = threading.Thread(target=worker, args=(2,))

# start the threads
thread1.start()
thread2.start()

# wait for the threads to finish
thread1.join()
thread2.join()

# start garbage collector
garbage_collector()