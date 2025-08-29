from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Function to check if string is a number (int, positive)
def is_number(s):
    return s.isdigit()

# Function to alternating caps a string (starting uppercase)
def alternating_caps(s):
    result = []
    upper = True
    for c in s:
        if upper:
            result.append(c.upper())
        else:
            result.append(c.lower())
        upper = not upper
    return ''.join(result)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data_json = request.get_json()
        if not data_json or 'data' not in data_json:
            return jsonify({"is_success": False, "error": "Missing 'data' key"}), 400
        
        input_array = data_json['data']
        
        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        sum_numbers = 0
        
        # Collect all alphabets for concatenation later
        all_alpha_chars = []
        
        # Process each element in input
        for elem in input_array:
            if is_number(elem):
                num = int(elem)
                sum_numbers += num
                if num % 2 == 0:
                    even_numbers.append(elem)
                else:
                    odd_numbers.append(elem)
            else:
                if re.fullmatch(r'[a-zA-Z]+', elem):
                    upper_elem = elem.upper()
                    alphabets.append(upper_elem)
                    all_alpha_chars.extend(list(upper_elem))
                else:
                    special_characters.append(elem)
        
        reversed_alpha = ''.join(all_alpha_chars[::-1])
        concat_str = alternating_caps(reversed_alpha)
        
        response = {
            "is_success": True,
            "user_id": "aditi_ranjan_20102004",
            "email": "aditiranjan8541@gmail.com",
            "roll_number": "22BCE2584",
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(sum_numbers),
            "concat_string": concat_str
        }
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run()
