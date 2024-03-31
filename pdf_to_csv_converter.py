import tabula

input_path = "March 2024 e-Statement .pdf"
output_path = "test2.csv"

# Define the area (top, left, bottom, right) in points
# For example, this might represent a rectangle 
# starting 100 points from the top, 50 points from the left, 
# extending to 500 points from the top, and 550 points from the left.
area = [200, 25, 500, 500]

# Read PDF with specified area
df = tabula.read_pdf(input_path=input_path, pages="all", area=area)

# Convert PDF into CSV with specified area
tabula.convert_into(input_path=input_path, output_path=output_path, output_format="csv", pages="all", stream=True, area=area)

