import re


def scale_html(html, scale_percentage):
    # Convert the scale percentage to a multiplier
    scale_factor = scale_percentage / 100.0

    # Define the style attributes that need scaling
    attributes_to_scale = ['width', 'padding-top', 'padding-bottom', 'font-size']

    # Regular expression to find style attributes
    regex_pattern = r'(width|padding-top|padding-bottom|font-size):\s*([\d\.]+)px'

    # Function to scale the attribute values
    def scale_match(match):
        if match.group(1) in attributes_to_scale:
            new_value = float(match.group(2)) * scale_factor
            return f'{match.group(1)}: {new_value}px'
        return match.group(0)

    # Use regex to replace the style attributes
    scaled_html = re.sub(regex_pattern, scale_match, html)
    return scaled_html

# Example HTML input
html_input = '''
<div class="Frame3" style="width: 1920px; padding-top: 5px; padding-bottom: 5px; left: 0px; top: 0px; position: absolute; background: #00AAAA; justify-content: center; align-items: center; display: inline-flex">
  <div class="ProgramMaster2000" style="color: black; font-size: 25px; font-family: Ac437 IBM BIOS; font-weight: 400; word-wrap: break-word">Program Master 2000</div>
</div>
'''

# Input from the user
scale_percentage = float(input("Enter the scale percentage (e.g., 50 for 50%): "))

# Scale the HTML
scaled_html = scale_html(html_input, scale_percentage)
print(scaled_html)
