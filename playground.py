from flask import Flask, render_template
app = Flask(__name__)                     

@app.route('/play')
def play():
    return render_template('index.html', y = 3, color = "blue")

@app.route('/play/<x>')
def play_multi(x):
    return render_template('index.html', y = int(x), color = "green")
    
@app.route('/play/<x>/<color>')                           
def play_multi_color(x, color):
    return render_template('index.html', y =int(x), color = color)

if __name__=="__main__":
    app.run(debug=True)  