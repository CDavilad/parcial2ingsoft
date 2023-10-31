from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular_factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

@app.route('/factorial/<int:num>', methods=['GET'])
def factorial(num):
    result = calcular_factorial(num)
    if result is not None:
        return jsonify({'factorial': result})
    else:
        return jsonify({'error': 'No se puede calcular el factorial de un número negativo'}), 400

if __name__ == '__main__':
    app.run(debug=True)
