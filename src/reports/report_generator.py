import pandas as pd
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from pathlib import Path
from datetime import datetime

class ReportGenerator:
    def __init__(self, template_path='src/reports/templates'):
        self.env = Environment(loader=FileSystemLoader(template_path))
        # Add a filter to format dates and make now() function available
        self.env.globals['now'] = datetime.now

    def generate_report(self, data, recommendations, output_file):
        template = self.env.get_template('report_template.html')
        rendered_html = template.render(data=data, recommendations=recommendations)
        
        # Generate PDF from HTML
        HTML(string=rendered_html).write_pdf(output_file)
        print(f"Report generated and saved to: {output_file}")

    def save_report(self, data, recommendations, output_file):
        self.generate_report(data, recommendations, output_file)

def generate_report(data: dict, recommendations: dict, output_file: str) -> None:
    """
    Generate a soil analysis report in PDF format.
    
    Args:
        data (dict): Soil analysis data
        recommendations (dict): Analysis recommendations
        output_file (str): Path to save the PDF report
    """
    generator = ReportGenerator()
    generator.save_report(data, recommendations, output_file)

