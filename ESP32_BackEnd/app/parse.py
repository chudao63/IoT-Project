import json, urllib, logging

def parse_body_data(input):
    try:
        return json.loads(input)
    except:
        try:
            return json.loads(urllib.unquote_plus(input))
        except:
            logging.error(f"Error Json format data: {input}")

