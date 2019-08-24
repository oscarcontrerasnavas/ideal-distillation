from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def get_html_bs4(url):
    response = simple_get(url)

    if response is not None:
        return BeautifulSoup(response, 'html.parser')

    raise Exception('Error retrieving contents at {}'.format(url))


def scrap_properties(html_bs4, css_element, unique_property=None,
                     property_value=None):

    # Check given parameters
    if unique_property is None or property_value is None:
        return html_bs4.select_one(css_element)
    else:
        return html_bs4.find(css_element,
                             attrs={unique_property: property_value})


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """

    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """

    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """

    print(e)