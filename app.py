from flask import Flask
from algorithms.sorter import *

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    a = Sorter([1,2,3,4,5,6,7,8])
    return str(a.insertion_sort())


if __name__ == '__main__':
    app.run()
