 --> Raising Exceptions

 If you need to determine whether an exception was raised but don’t intend to handle it, a simpler form of the raise statement allows you to re-raise the exception:

 --> Defining Clean-up Actions

If the finally clause executes a break, continue or return statement, exceptions are not re-raised.

If the try statement reaches a break, continue or return statement, the finally clause will execute just prior to the break, continue or return statement’s execution.

If a finally clause includes a return statement, the returned value will be the one from the finally clause’s return statement, not the value from the try clause’s return statement.


 -->  Enriching Exceptions with Notes

When an exception is created in order to be raised, it is usually initialized with information that describes the error that has occurred. There are cases where it is useful to add information after the exception was caught. For this purpose, exceptions have a method add_note(note) that accepts a string and adds it to the exception’s notes list. The standard traceback rendering includes all notes, in the order they were added, after the exception.