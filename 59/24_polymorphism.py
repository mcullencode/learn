import os
# In python not only do the objects support polymorphism, but the classes do as well

#Polymorphism is a way for multiple classes in a hierarchy to implement their own unique versions of a method (method is a procedure ssociatd with a class)
# This allows many classes to fulfill the same interface ot abstract base class while providing different functionality.
# i.e. say you're writing a MapReduce implementation and you want a common class to represent the input data.
# Here I define such a class with a read method that must be defined by subclasses:

# MapReduce is a processing technique and a program model for distributed computing based on java. The MapReduce algorithm
# contains two important tasks, namely Map and Reduce. Map takes a set of data and converts it into another set of data,
# where individual elements are broken down into tuples (key/value pairs). Secondly, reduce task, which takes the output
# from a map as an input and combines those data tuples into a smaller set of tuples. As the sequence of the name MapReduce
# implies, the reduce task is always performed after the map job.

class InputData(object):
    def read(self):
        raise NotImplementedError

#here i have a concrete subclass of inputdata that reads data from a file on disk.from

class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()


#[Super is used to] return a proxy object (object- particular instance of a class) that delegates method calls to a parent or
# sibling class of type. This is useful for accessing inherited methods that have been overridden in a class.
# The search order is same as that used by getattr() except that the type itself is skipped.

#You could have any number of InputData subclaasses like PathInoutData and each of them could implement
#the standard interface for read to return the bytes of data to process.

#You'd want a similar abstract interface for yhr MapReduce worker that consumes the inout data in a standard way.

class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

#Here we define a concrete subclass of Worker to implement the specific MapReduce function i want to apply: a simple newline counter

class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result == other.result


#just reached a hurdle in this implementation. We have nice set of classes with reasonable interfaces and abstractions,
#  but thats only useful once the objects are constructed. whats responsible for building the objects and ochestrating
# the MapReduce?

#interface controls the behaviours that a class implements.
# abstract class can have instance methods that implements a default behaviour

#simplest approach is to manually build and connect the objects with some helper functions. Here i list the contents
# of a directory and construct a PathInputData instance for each file it contains.

#must import os. The method listdir() returns a list containing the names of the entries in the directory given by path.
# os.join.path(path, *paths) in docs as 'join paths intelligently. The return value is the concatenation of path and any members of *paths
# with exactly one directory separator'

def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))

#next create the LineCountWorker instances using the InputData instances returned by generate _inputs

def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))

    return workers

#Execute these worker instances by fanning out the map step to multiple threads.
# Then call reduce repeatedly to combine the results into one final value

def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result

#firstly connect all pieces together in a function to run each step.

def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)


# can not import temp file and test. it works but what is problem? the issue is that the mapreduce function is not generic
# at all. If you want to write another InputData or Worker sublcass you would also have to rewrite generate_inputs,
# create_workers and mapreduce functions to match.\

#The problem boils down to needing a generic way to construct objects. In other languages you'd solve this problem with constructor polymorphism,
# requiring that each InputData subclass provides a special constructor  that can be used generically by the helper methods
#  that orchestrate MapReduce. The trouble is that python only allows for the single constructor method __init__ .
#  It's unreasonable to require every InputData subclass to have a compatible constructor.

#best way to solve this problem in python is with @classmethod polymorphism

