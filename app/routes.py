from flask import render_template, jsonify
from app import app
from app.utils.calculator import estimate_cost

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test-calc')
def test_calc():
    result = estimate_cost(
        selected_services=["Logo & Visual Identity Design", "Website Design & Development"],
        business_scale="Small Business",
        creative_scope="Enhanced and Polished",
        content_requirements="Agency creates",
        is_urgent=False,
        has_custom_request=False
    )
    return jsonify({
        "low_estimate": result[0],
        "high_estimate": result[1]
    })
