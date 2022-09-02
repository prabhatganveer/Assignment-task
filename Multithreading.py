{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "missing-disposal",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "1--->How To Use The Thread Module To Create Threads?\n",
    "     how to detect the status of a python thread?Which method is used to identify a thread?\n",
    "ans->Define a new subclass of the Thread class.\n",
    "   ->Override the __init__(self [,args]) method to add additional arguments.\n",
    "   ->Then, override the run(self [,args]) method to implement what the thread should do when started.\n",
    "   \n",
    "   A thread can be given a name in its constructor. In addition, it can be specified via a Thread object's setName() method. \n",
    "   In addition, it should be noted that a thread is given an identification number that can be retrieved via the thread's \n",
    "   getId() method.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "trained-nursing",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "honest-artist",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "2--->What is the method that wakes up all thread waiting for the condition? \n",
    "     What are the libraries in Python that support threads?\n",
    "ans->The notifyAll() method wakes up all threads waiting for the condition variable.\n",
    "   ->Let's take a look at what the thread module has to offer. In addition to being able to spawn threads, the thread module \n",
    "     also provides a basic synchronization data structure called a lock object (a.k.a. primitive lock, simple lock, mutual \n",
    "     exclusion lock, mutex, and binary semaphore)\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "seventh-complex",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "altered-photography",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "3--->What are the lock types a Condition object can associate with?\n",
    "ans-> Condition Objects. A condition variable is always associated with some kind of lock; this can be passed in or one will be \n",
    "      created by default. Passing one in is useful when several condition variables must share the same lock.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "infinite-index",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "conservative-lewis",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "4--->How Is Python Thread Safe?\n",
    "ans->If a class or a program has immutable state then the class is necessarily thread-safe. ... Similarly, the shared state \n",
    "     in an application where the same thread mutates the state using an operation that translates into an atomic bytecode \n",
    "     instruction can be safely read by multiple reader threads.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "stainless-rental",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "responsible-baghdad",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "5--->Which Python library runs a function as thread? How does run() method is invoked?\n",
    "ans->Threading in Python is simple. It allows you to manage concurrent threads doing work at the same time. The library is \n",
    "     called “threading“, you create “Thread” objects, and they run target functions for you. You can start potentially hundreds\n",
    "     of threads that will operate in parallel.\n",
    "   ->The run() method of thread class is called if the thread was constructed using a separate Runnable object otherwise this \n",
    "     method does nothing and returns. When the run() method calls, the code specified in the run() method is executed.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "sticky-senate",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "emerging-party",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "6--->How to terminate a blocking thread? What is the method to retrieve the list of all active threads?\n",
    "ans->threading. enumerate() returns a list of all Thread objects currently alive. The list includes daemonic threads, \n",
    "     dummy thread objects created by current_thread(), and the main thread. It excludes terminated threads and threads that \n",
    "     have not yet been started.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "determined-enforcement",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "practical-rider",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "7--->Create A Thread Class To Print The Date\n",
    "ans->\n",
    "        import threading \n",
    "\n",
    "        class thread(threading.Thread): \n",
    "            def __init__(self, thread_name, thread_ID): \n",
    "                threading.Thread.__init__(self) \n",
    "                self.thread_name = thread_name \n",
    "                self.thread_ID = thread_ID \n",
    "\n",
    "                # helper function to execute the threads\n",
    "            def run(self): \n",
    "                print(str(self.thread_name) +\" \"+ str(self.thread_ID)); \n",
    "\n",
    "        thread1 = thread(\"GFG\", 1000) \n",
    "        thread2 = thread(\"GeeksforGeeks\", 2000); \n",
    "\n",
    "        thread1.start() \n",
    "        thread2.start() \n",
    "\n",
    "        print(\"Exit\") \n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "identified-taylor",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ultimate-conditioning",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "8--->What would be the impact of multithreading on a uni-processor system?\n",
    "ans->With Uniprocessor systems, multithreading helps in sharing the CPU among multiple tasks so that no one task hogs the \n",
    "     CPU till it gets completed. A good example is a game, where you have to do many things concurrently.\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dependent-paint",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "extreme-garbage",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "9--->Which thread method is used to wait until it terminates?\n",
    "     What are the states/features supported by a Lock object?\n",
    "ans->join() : When the join() method is called, the current thread will simply wait until the thread it is joining with is no \n",
    "     longer alive. Or we can say the method that you will more commonly use to wait for a thread to finish is called join( ). \n",
    "     This method waits until the thread on which it is called terminates.\n",
    "   ->Lock Object: Python Multithreading\n",
    "     Primitive lock can have two States: locked or unlocked and is initially created in unlocked state when we initialize the \n",
    "     Lock object. It has two basic methods, acquire() and release()\n",
    "'''"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
