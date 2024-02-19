import random

# List of quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt"
]


# Function to generate a random quote
def generate_quote():
    
    return random.choice(quotes)

if __name__ == "__main__":
    # Generate a random quote
    quote = generate_quote()

    # Write the quote to an HTML file
    with open("index.html", "w") as f:
        f.write(f"<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n")
        f.write("<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
        f.write("<title>Random Quote</title>\n</head>\n<body>\n")
        #f.write("<p>Quote of the moment: </p>\n")
        f.write(f"<blockquote>Quote of the Moment is : \n{quote}</blockquote>\n</body>\n</html>")
