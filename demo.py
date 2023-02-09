import sys
import requests

from generator.var_generator import generate
from generator.var_parser import parser_var_file

SEED = 1234  # optional attribute to achieve consistent output while testing
URL = "www.CTFd.io"  # URL of your CTFd server running personal challenge plugin
USERNAME = "login@mail.com"
ENABLE_ID = True  # return Challenge object (id + name) as a key instead of String containing just name
PATH = "input.yml"

"""
Post generated values to CTFd server extended by personal challenge plugin
...
Parameters
    ----------
    url : String
        url address of CTFd server
    generated_values : dict
         Challenge object as a key and generated value as value

    Returns
    -------
        Bool
            was it successful

"""


def upload_flags(url, values_dict):
    errors = []
    for key in values_dict:
        data = {"user_email": USERNAME, "flag": values_dict[key], "challenge_id": key.id}
        try:
            result = requests.post(url + "/store", data=data).json()
            if result["success"] or result["uploaded"]:
                break
            errors.append(result["message"])
            raise Exception("upload error")

        except:
            print("An error occurred, check your internet connection.",
                  file=sys.stderr)
            print("Errors : ", file=sys.stderr)
            if not errors:
                # CTFd is not responding
                print("CTFd error.",
                      file=sys.stderr)
            for current_err in errors:
                if "FOREIGN KEY (`challenge_id`)" in current_err:
                    print("Challenge " + current_err.split("'")[5] + " is missing in CTFd!",
                          file=sys.stderr)
                    return False
                if "FOREIGN KEY (`user_id`)" in current_err or \
                        "User doesn't exist." in current_err:
                    print("User " + data["user_email"] + " is missing in CTFd!",
                          file=sys.stderr)
                    return False
                print("Unknown CTFd error", file=sys.stderr)
            return False
    return True


with open(PATH) as file:
    variable_list = parser_var_file(file)
    generated_values = generate(variable_list, SEED, ENABLE_ID)

    upload_flags(URL, generated_values)  # use only with personal challenge plugin for CTFd, otherwise remove

    print(generated_values)
    # {1. generated_text: 'I always did something i was not ready to do. I think that’s how you grow. When there’s that moment of ', 3. generated_password: '6SBI1LEz', 10. generated_username: 'persona', 2. generated_port: '35608'}
