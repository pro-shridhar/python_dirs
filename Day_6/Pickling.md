“Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.

pickle.dump(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None)
Write the pickled representation of the object obj to the open file object file. This is equivalent to

pickle.dumps(obj, protocol=None, *, fix_imports=True, buffer_callback=None)
Return the pickled representation of the object obj as a bytes object, instead of writing it to a file.

Only the instance data are pickled. This is done on purpose, so you can fix bugs in a class or add methods to the class and still load objects that were created with an earlier version of the class

## If you find yourself faced with an unpicklable object
 then there are a couple of things that you can do. The first option is to use a third-party library such as dill.

 The dill module extends the capabilities of pickle. According to the official documentation, it lets you serialize less common types like functions with yields, nested functions, lambdas, and many others.

## Exception 
 example of unpickling object-> lambda function