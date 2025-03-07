from fastapi import FastAPI 
import random

app = FastAPI()

side_hustles = [
    "Web Scraping Services (data extraction)",
    "API Integration/Development",
    "Data Analysis/Visualization (using Pandas, Matplotlib, Seaborn)",
    "Automation Scripts (for repetitive tasks)",
    "Building Chatbots (using libraries like ChatterBot)",
    "Developing Simple Web Applications (using Flask, Django)",
    "Creating Command-Line Tools",
    "Writing Python Tutorials/Blog Posts",
    "Developing Python-based Games (using Pygame)",
    "Building Machine Learning Models (for clients)",
    "Automating Social Media Tasks (with caution and ethical considerations)",
    "Creating Excel/CSV Automation Scripts",
    "Developing Data Entry Automation Tools",
    "Building Simple Desktop Applications (using Tkinter, PyQt)",
    "Creating Python-based Trading Bots (with financial expertise)",
    "Developing Scripts for Data Cleaning/Preprocessing",
    "Building Scripts for File Management/Organization",
    "Creating Simple AI Assistants (for specific tasks)",
    "Developing educational python scripts",
    "Creating scripts to automate website testing"
]

money_quotes = [
    "The goal isn't more money. The goal is living life on your terms. - Chris Brogan",
    "Money is only a tool. It will take you wherever you wish, but it will not replace you as the driver. - Ayn Rand",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "An investment in knowledge pays the best interest. - Benjamin Franklin",
    "Don't tell me what you value, show me your budget, and I'll tell you what you value. - Joe Biden",
    "Money often costs too much. - Ralph Waldo Emerson",
    "Wealth is not about having a lot of money; it's about having a lot of options. - Chris Brogan",
    "It's not how much money you make, but how much money you keep, how hard it works for you, and how many generations you keep it for. - Robert Kiyosaki",
    "Every pound invested in your self-belief earns you hundreds more. - Rob Moore",
    "If you don’t find a way to make money while you sleep, you will work until you die. - Warren Buffett",
    "The habit of saving is itself an education; it fosters every virtue, teaches self-denial, cultivates the sense of order, trains to forethought, and so broadens the mind. - T.T. Munger",
    "Too many people spend money they haven't earned, to buy things they don't want, to impress people they don't like. - Will Smith",
    "Money is a terrible master but an excellent servant. - P.T. Barnum",
    "A successful man is one who can lay a firm foundation with the bricks others have thrown at him. - David Brinkley",
    "The rich invest their money and spend what is left; the poor spend their money and invest what is left. - Warren Buffett",
    "Formal education will make you a living; self-education will make you a fortune. - Jim Rohn",
    "Money is a guarantee that we may have what we want in the future. Though we need nothing at the moment, it insures the possibility of satisfying a necessary desire when it arises. - Aristotle",
    "The art is not in making money, but in keeping it. - Proverb",
    "Do not save what is left after spending, but spend what is left after saving. - Warren Buffett",
    "Opportunity is missed by most people because it is dressed in overalls and looks like work. - Thomas Edison"
]


@app.get("/side_hustles")
def get_side_hustles (apikey:str):
    """Returns a random side hustle!"""
    if apikey != 1234567890:
        return {"error: invalid api key"}
    return {"Side_hustle": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes(apikey):
    """Returns the random money quote"""
    if apikey != 1234567890:
        return {"error: invalid api key"}
    return {"money_quotes": random.choice(money_quotes)}