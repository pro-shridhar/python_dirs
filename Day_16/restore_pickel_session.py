globals().items()

import dill

dill.load_session("test.pkl")
globals().items()
print(a)
print(b)
