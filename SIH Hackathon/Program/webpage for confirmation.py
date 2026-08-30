from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success Submission</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f7f6;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        /* Initial Submit Button Styling */
        .submit-btn {
            background-color: #2ecc71;
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(46, 204, 113, 0.3);
            transition: background 0.2s;
        }
        .submit-btn:hover {
            background-color: #27ae60;
        }

        /* Success Card (Hidden by default) */
        .card {
            display: none;
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            text-align: center;
            max-width: 400px;
            width: 100%;
        }

        /* Animated Checkmark Container */
        .success-checkmark {
            width: 80px;
            height: 80px;
            margin: 0 auto 20px auto;
        }

        /* The Checkmark SVG - remains visible permanently */
        .checkmark {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            display: block;
            stroke-width: 4;
            stroke: #2ecc71;
            stroke-miterlimit: 10;
            box-shadow: inset 0px 0px 0px #2ecc71;
            animation: fill .4s ease-in-out .4s forwards;
        }
        .checkmark__circle {
            stroke-dasharray: 166;
            stroke-dashoffset: 166;
            stroke-width: 4;
            stroke-miterlimit: 10;
            stroke: #2ecc71;
            fill: none;
            animation: stroke 0.6s cubic-bezier(0.65, 0, 0.45, 1) forwards;
        }
        .checkmark__check {
            transform-origin: 50% 50%;
            stroke-dasharray: 48;
            stroke-dashoffset: 48;
            animation: stroke 0.3s cubic-bezier(0.65, 0, 0.45, 1) 0.6s forwards;
        }

        @keyframes stroke {
            100% { stroke-dashoffset: 0; }
        }
        @keyframes fill {
            100% { box-shadow: inset 0px 0px 0px 40px #2ecc71; }
        }

        h1 {
            color: #2c3e50;
            font-size: 24px;
            margin: 0 0 10px 0;
        }
        p {
            color: #7f8c8d;
            font-size: 16px;
            margin: 0;
        }
    </style>
</head>
<body>

    <!-- Clickable Submit Button to satisfy browser audio requirements -->
    <button id="main-submit-btn" class="submit-btn" onclick="showSuccess()">Submit Response</button>

    <!-- Success Card Container -->
    <div id="success-card" class="card">
        <div class="success-checkmark">
            <svg class="checkmark" xmlns="http://w3.org" viewBox="0 0 52 52">
                <circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none"/>
                <path class="checkmark__check" fill="none" stroke="#fff" d="M14.1 27.2l7.1 7.2 16.7-16.8"/>
            </svg>
        </div>
        <h1>Thank You!</h1>
        <p>Your response has been submitted</p>
    </div>

    <!-- Audio Element using a reliable browser-friendly audio link -->
    <audio id="success-sound" preload="auto">
        <source src="https://google.com" type="audio/ogg">
        <source src="https://mixkit.co" type="audio/wav">
    </audio>

    <script>
        function showSuccess() {
            const sound = document.getElementById('success-sound');
            const btn = document.getElementById('main-submit-btn');
            const card = document.getElementById('success-card');

            // 1. Play sound instantly upon user click
            sound.play().catch(err => console.log("Audio play failed:", err));

            // 2. Hide the submit button and reveal the permanent animated success card
            btn.style.display = 'none';
            card.style.display = 'block';
        }
    </script>

</body>
</html>
"""


@app.route('/')
def success_page():
    return render_template_string(HTML_TEMPLATE)


if __name__ == '__main__':
    app.run(debug=True)
