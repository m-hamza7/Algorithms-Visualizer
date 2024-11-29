from flask import Flask, render_template, request, redirect, url_for
from algorithms import process_closest_pair, process_karatsuba
from visualizations import visualize_closest_pair, visualize_karatsuba_tree

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    file = request.files['file']
    algorithm = request.form['algorithm']
    
    if file:
        file_path = f"datasets/{file.filename}"
        file.save(file_path)

        if algorithm == "closest_pair":
            # Get points, closest pair, and distance
            points, closest_pair, distance = process_closest_pair(file_path)
            visualize_closest_pair(points, closest_pair, distance)  # Call visualization
            return redirect(url_for('index'))
        
        elif algorithm == "karatsuba":
            # Get recursion tree
            tree = process_karatsuba(file_path)
            visualize_karatsuba_tree(tree)  # Call visualization
            return redirect(url_for('index'))
    
    return "Error: No file uploaded."

if __name__ == "__main__":
    app.run(debug=True)
