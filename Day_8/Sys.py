# try:
#     f = open("myfile.txt")
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise

# import sys

# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, "r")
#     except OSError:
#         print("cannot open", arg)
#     else:
#         print(arg, "has", len(f.readlines()), "lines")
#         f.close()


# def func():
#     raise ConnectionError


# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError("Failed to open database") from exc


def f():
    excs = [OSError("error 1"), SystemError("error 2")]
    raise ExceptionGroup("there were problems", excs)


f()
