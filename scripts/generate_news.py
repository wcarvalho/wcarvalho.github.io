#!/usr/bin/env python3
"""
Convert news.yaml to news.html format
"""

import yaml
from pathlib import Path

def convert_yaml_to_html(yaml_file='_includes/news.yaml', html_file='_includes/news.html'):
    """Convert news YAML file to HTML format"""
    
    # Read YAML file
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)
    
    # Create HTML content
    html_lines = []
    
    # Process each year in reverse chronological order
    for year in sorted(data.keys(), reverse=True):
        year_data = data[year]
        
        # Process each month in the order they appear in the file
        # We'll need to define month order
        month_order = ['December', 'November', 'October', 'September', 'August', 
                      'July', 'June', 'May', 'April', 'March', 'February', 'January']
        
        # Get months that exist in the data
        months_in_data = list(year_data.keys())
        
        # Sort months according to calendar order (reverse for most recent first)
        sorted_months = [month for month in month_order if month in months_in_data]
        
        for month in sorted_months:
            items = year_data[month]
            
            # Handle both single items and lists
            if isinstance(items, list):
                for item in items:
                    # Flatten any nested lists and convert to string
                    if isinstance(item, list):
                        # If it's a nested list, join the items
                        item_text = " ".join(str(subitem) for subitem in item)
                        html_lines.append(f"- **{month}, {year}:** {item_text}")
                    else:
                        html_lines.append(f"- **{month}, {year}:** {item}")
            else:
                html_lines.append(f"- **{month}, {year}:** {items}")
    
    # Add a blank line at the beginning (to match the original format)
    html_content = "\n" + "\n".join(html_lines) + "\n"
    
    # Write to HTML file
    with open(html_file, 'w') as f:
        f.write(html_content)
    
    print(f"Successfully converted {yaml_file} to {html_file}")
    print(f"Generated {len(html_lines)} news items")

if __name__ == "__main__":
    convert_yaml_to_html() 