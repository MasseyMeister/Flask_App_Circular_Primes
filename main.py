from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def circular_primes():
    limit = request.form['text']

    def check_prime(num):
        factor = 2
        while factor * factor <= num:
            if num % factor == 0:
                return False
            factor += 1
        return True

    def circulate(number):
        """returns all circulations of a number."""
        circulations = []
        digits = list(str(number))
        for i in range(len(str(number))):
            last = digits.pop()
            circulations.append(last + ''.join(digits))
            digits = [last] + digits
        return [int(x) for x in circulations]

    all_circulations = [2]
    for num in range(3, int(limit), 2):
        if check_prime(num):
            check = 0
            if circulate(num):
                circulations = circulate(num)
                for circulation in circulations:
                    if not check_prime(circulation):
                        check += 1
                if not check:
                    all_circulations.extend(circulations)
    return str(all_circulations)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
