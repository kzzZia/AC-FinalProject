from flask import Flask, render_template, request
from algorithms import xor_cipher, caesar_cipher, rsa_basic, block_cipher, diffie_hellman, hashing

app = Flask(__name__)

@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/xor', methods=['GET', 'POST'])
def xor():
    result = ''
    log = []
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        result, log = xor_cipher.xor_cipher(text, key)
    return render_template('xor.html', result=result, log=log)

@app.route('/caesar', methods=['GET', 'POST'])
def caesar():
    result = ''
    if request.method == 'POST':
        text = request.form['text']
        shifts = list(map(int, request.form['shifts'].split()))
        action = request.form['action']
        decrypt = (action == 'decrypt')
        result = caesar_cipher.encrypt_decrypt(text, shifts, decrypt)
    return render_template('caesar.html', result=result)

@app.route('/block', methods=['GET', 'POST'])
def block():
    result = ''
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        action = request.form['action']
        result = block_cipher.encrypt_decrypt(text, key, action)
    return render_template('block.html', result=result)

@app.route('/rsa', methods=['GET', 'POST'])
def rsa():
    public = private = message = cipher = plain = table = ''
    if request.method == 'POST':
        message = request.form['message']
        p = rsa_basic.generate_prime_number()
        q = rsa_basic.generate_prime_number()
        public, private = rsa_basic.generate_keypair(p, q)
        cipher = rsa_basic.encrypt(public, message)
        plain = rsa_basic.decrypt(private, cipher)

        # Build transformation table
        table = [
            {
                "char": ch,
                "ord": ord(ch),
                "cipher": c,
                "decrypted": chr(pow(c, private[0], public[1]))
            }
            for ch, c in zip(message, cipher)
        ]

    return render_template('rsa.html', public=public, private=private,
                           message=message, cipher=cipher, plain=plain, table=table)



@app.route('/diffie', methods=['GET', 'POST'])
def diffie():
    if request.method == 'POST':
        try:
            p = int(request.form['p'])
            g = int(request.form['g'])
            a = int(request.form['a'])
            b = int(request.form['b'])
        except ValueError:
            return render_template('diffie.html', error="Invalid input")

        A = pow(g, a, p)
        B = pow(g, b, p)
        secret_A = pow(B, a, p)
        secret_B = pow(A, b, p)

        return render_template('diffie.html', p=p, g=g, a=a, b=b, A=A, B=B,
                               secret_A=secret_A, secret_B=secret_B)

    return render_template('diffie.html', p=None)

@app.route('/hash', methods=['GET', 'POST'])
def hash_view():
    result = ''
    if request.method == 'POST':
        text = request.form['text']
        algo = request.form['algorithm']
        result = hashing.hash_text(text, algo)
    return render_template('hash.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
