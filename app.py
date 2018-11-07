from flask import Flask

app = Flask(__name__)

@app.route('/fib/<int:n>')

def convert_fibonacci(n):
    return format(fibonacci(n))

def fibonacci(n):
    if n < 2:
        return 1
    return fibonacci(n -1) + fibonacci(n -2)

if __name__ == '__main__':
     app.run()