from urllib import request


def read_text(file_link):

    # Open the file from the link provided
    data_doc = open(file_link)

    # Store the text from the opened document in this variable
    data_contents = data_doc.read()

    # Close the document since we are done with it
    data_doc.close()

    return data_contents


def profanity_screen(string_to_check):

    # Send this url to the site, replacing all spaces with the space character
    url = 'http://www.wdylike.appspot.com/?q=' + string_to_check
    url = url.replace(' ', '%20')
    
    # Store the response as an object
    f = request.urlopen(url)

    # Read the response object and save it as a variable
    page_out = f.read().decode('utf-8')

    # Close the response object since we are done with it
    f.close()

    return page_out


def main():

    quotes_file = 'movie_quotes_1.txt'

    quotes_text = read_text(quotes_file)
    quotes_profanity = profanity_screen(quotes_text)

    if 'true' in quotes_profanity:
        print('Profanity detected in %s' % quotes_file)
    elif 'false' in quotes_profanity:
        print('No profanity detected in %s' % quotes_file)


main()
