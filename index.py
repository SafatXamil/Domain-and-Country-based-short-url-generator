import ast
import json
from pathlib import Path

import tldextract as tldextract
import validators
import random

import resources

# declare new class object
page_resources = resources.Resources()


# functions
def gen_rand_str(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    randcode = ""
    for counter in range(length):
        randcode = randcode + random.choice(characters)
    return randcode


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

    # host and country extension not defined
    if host is None and country_ext is None:
        short_url = "domain.com/" + random_code
    # host is undefined, country ext found
    elif host is None and country_ext is not None:
        short_url = "domain.com/" + country_ext + "-" + random_code
    # host found, country ext undefined
    elif host is not None and country_ext is None:
        short_url = "domain.com/" + host + "-" + random_code
    # just put the random code
    elif host is not None and country_ext is not None:
        short_url = "domain.com/" + host + "-" + country_ext + "-" + random_code
    return short_url


# input url
url_input = "https://aliexpress.ru/wholesale?SearchText=crocse&d=y&origin=n&initiative_id=SB_20190717045559&isViewCP=y&catId=0&jump=afs"
url_input = url_input.strip()
url_input = url_input.lower()

# initialize variables for operations
file_data = ""
redirect_dict = dict()

# check if host is in banned list
extraxt = tldextract.extract(url_input)
# if host is not in banned list
if extraxt.domain not in page_resources.banned_host:
    try:
        with open(Path("redirect_url_data.txt"), 'r') as file:
            file_data = file.read().replace('\n', '')
            redirect_dict = ast.literal_eval(file_data)
    except:
        # show error
        print("error")

    # first validate url
    valid = validators.url(url_input)

    # if valid url
    if valid:
        # url does not exist in this system
        if url_input not in file_data:
            new_short_url = generate_short_url(url_input)
            # check if short code exists 10 times
            for counter in range(0, 10):
                if new_short_url not in redirect_dict.values():
                    break
                else:
                    new_short_url = generate_short_url(url_input)

            if new_short_url not in redirect_dict.values():
                # add new url to dict
                redirect_dict[url_input] = new_short_url
                # string to dict
                file_data = json.dumps(redirect_dict)
                try:
                    write_file = open("redirect_url_data.txt", "w")
                    write_file.write(file_data)
                    write_file.close()
                except:
                    # show error
                    print("error")
        else:
            print("url exists")

    else:
        print("This url is not valid or use http:// or https:// protocol")
else:
    # do something
    print("We can't make a short url for this domain.")

# This was developed by Safat Jamil, email: safaetxamil@yahoo.com
