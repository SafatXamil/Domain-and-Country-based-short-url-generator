from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect

import ast
import json
from pathlib import Path

import tldextract as tldextract
import validators
import random

from shortener_app import resources


# functions
def gen_rand_str(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    randcode = ""
    for counter in range(length):
        randcode = randcode + random.choice(characters)
    return randcode

# declare new class object
page_resources = resources.Resources()


#function to generate short url
def generate_short_url(url):
    # initialize variable
    hostname = ""
    domain_extension = ""
    host = None
    country_ext = None
    extract = ""
    short_url = ""
    # extract host, extension
    extract = tldextract.extract(url)
    hostname = extract.domain
    domain_extension = extract.suffix

    # find host if available
    if hostname in page_resources.resv_host:
        host = page_resources.resv_host[hostname]

    # get country from domain extension
    if domain_extension in page_resources.country_extension:
        country_ext = page_resources.country_extension[domain_extension]

    # generate random string
    random_code = gen_rand_str(5)

    # use your "domain.com" instead of 
    # host and country extension not defined "http://127.0.0.1:8000//"
    if host is None and country_ext is None:
        short_url = "http://127.0.0.1:8000/" + random_code
    # host is undefined, country ext found
    elif host is None and country_ext is not None:
        short_url = "http://127.0.0.1:8000/" + country_ext + "-" + random_code
    # host found, country ext undefined
    elif host is not None and country_ext is None:
        short_url = "http://127.0.0.1:8000/" + host + "-" + random_code
    # just put the random code
    elif host is not None and country_ext is not None:
        short_url = "http://127.0.0.1:8000/" + host + "-" + country_ext + "-" + random_code
    return short_url



# Create your views here.
def index(request):

    status = ""
    new_short_url = ""

    input_url = request.POST.get('input_url')
    if input_url is None:
        input_url = ""
    input_url = input_url.strip()
    input_url = input_url.lower()


    # initialize variables for operations
    file_data = ""
    redirect_dict = dict()

    # check if host is in banned list
    extraxt = tldextract.extract(input_url)
    # if host is not in banned list
    if extraxt.domain not in page_resources.banned_host:
        try:
            with open(Path("shortener_app/redirect_url_data.txt"), 'r') as file:
                file_data = file.read().replace('\n', '')
                redirect_dict = ast.literal_eval(file_data)
        except:
            # show error
            status = "Something went wrong"

        # first validate url
        valid = validators.url(input_url)

        # if valid url
        if valid:
            # url does not exist in this system
            if input_url not in file_data:
                new_short_url = generate_short_url(input_url)
                # check if short code exists 10 times
                for counter in range(0, 10):
                    if new_short_url not in redirect_dict.values():
                        break
                    else:
                        new_short_url = generate_short_url(input_url)

                if new_short_url not in redirect_dict.values():
                    # add new url to dict
                    redirect_dict[input_url] = new_short_url
                    # string to dict
                    file_data = json.dumps(redirect_dict)
                    try:
                        write_file = open("shortener_app/redirect_url_data.txt", "w")
                        write_file.write(file_data)
                        write_file.close()
                        status = "Short url generated"
                    except:
                        # show error
                        status = "Something went wrong"
            else:
                status = "This url already exists. Short url for this url is"
                new_short_url = redirect_dict[input_url]


        else:
            status = "This url is not valid or use http:// or https:// protocol"
    else:
        # do something
        status = "We can't make a short url for this domain."

    if input_url is None:
        status = ""
    if input_url == "":
        status = ""
    context = {"status": status, "url":new_short_url}
    return render(request, "index.html", context)




def redirect(request, path):
     # initialize variables for operations
     #add your domain
    url = "http://127.0.0.1:8000/"+path
    file_data = ""
    redirect_dict = dict()
    url_found = False
    error = False
    status = ""
    redirected_url = ""
    try:
        with open(Path("shortener_app/redirect_url_data.txt"), 'r') as file:
            file_data = file.read().replace('\n', '')
            redirect_dict = ast.literal_eval(file_data)
            if url in redirect_dict.values():
                url_found = True
                for key, value in redirect_dict.items():
                    if value == url:
                        redirected_url = key
    except Exception as e:
        # do something with e
        error = True
        status = "Something went wrong"
    if error:
        return HttpResponse(status)
    else:
        if url_found:
            return HttpResponseRedirect(redirected_url)
        else:
            return HttpResponse ("Url not found")

def about(request):
    return HttpResponse("This project was developed by Safat Jamil. email: safaetxamil@yahoo.com")

# This was developed by Safat Jamil, email: safaetxamil@yahoo.com