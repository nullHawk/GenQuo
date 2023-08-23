import os
import random
from django.shortcuts import render
from django.core.files import File
from django.http import HttpResponse

# Create your views here.

def generate_quote(request):
    module_dir = os.path.dirname(__file__)  
    quote_path = os.path.join(module_dir, 'quotes.dat') 
    author_path = os.path.join(module_dir, 'author.dat') 
    quotes = open(quote_path, 'r+')
    author = open(author_path, 'r+')
    authorList = author.readlines()
    quoteList = quotes.readlines()
    choice = random.randrange(0, len(quoteList))
    display_quote = quoteList[choice].strip()
    display_author = authorList[choice].strip()
    footer = "Made with ❤️ by Suryansh Shakya"
    return  render(request,"home/index.html",context={'page':'GenQuo','footer':footer,'quote':display_quote,'author':display_author})

def home(request):
    module_dir = os.path.dirname(__file__)  
    quote_path = os.path.join(module_dir, 'quotes.dat') 
    author_path = os.path.join(module_dir, 'author.dat') 
    quotes = open(quote_path, 'r+')
    author = open(author_path, 'r+')
    authorList = author.readlines()
    quoteList = quotes.readlines()
    choice = random.randrange(0, len(quoteList))
    display_quote = quoteList[choice].strip()
    display_author = authorList[choice].strip()
    footer = "Made with ❤️ by Suryansh Shakya"
    return  render(request,"home/index.html",context={'page':'GenQuo','footer':footer,'quote':display_quote,'author':display_author})
