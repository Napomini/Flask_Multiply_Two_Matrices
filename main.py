from flask import Flask, render_template_string
import numpy as np

app = Flask(__name__)

@app.route('/')
def multiply_matrices():
    # Define the matrices
    A = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    B = [
        [13, 14],
        [15, 16],
        [17, 18],
        [19, 20]
    ]

    # Convert to NumPy arrays
    A_np = np.array(A)
    B_np = np.array(B)

    # Check if multiplication is possible
    if A_np.shape[1] != B_np.shape[0]:
        result = "Matrix multiplication not possible: Columns of A must equal rows of B."
    else:
        result_matrix = np.dot(A_np, B_np)
        result = result_matrix.tolist()

    # Simple HTML page to show result
    html = '''
    <h1>Matrix Multiplication Result</h1>
    <h3>Matrix A:</h3>
    <pre>{{ A }}</pre>
    <h3>Matrix B:</h3>
    <pre>{{ B }}</pre>
    <h3>Result:</h3>
    <pre>{{ result }}</pre>
    '''

    return render_template_string(html, A=A, B=B, result=result)

if __name__ == '__main__':
    app.run(debug=True)
