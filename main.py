import requests

def response_code(response):
    if response.status_code == 304:
        return print("Not Modified")
    elif response.status_code == 404:
        return print("Not Found")
    elif response.status_code == 301:
        return print("Moved Permanently")
    elif response.status_code == 403:
        return print("Forbidden")
    elif response.status_code == 200:
       return response.json()

def get_events(user):
    dict = {}
    response = requests.get(f"https://api.github.com/users/{user}/events")
    content = response_code(response)
    if response.status_code == 200:
        for event in content:
            if event["repo"]["url"] in dict:
                if event["type"] in dict[event["repo"]["url"]]:
                    dict[event["repo"]["url"]][event["type"]] += 1
                else:
                    dict[event["repo"]["url"]][event["type"]] = 1
            else:
                dict[event["repo"]["url"]] = {event["type"]: 1}
    
    for repo in dict:
        print(f"Repo: {repo}")
        for event in dict[repo]:
            print(f"Event: {event} Count: {dict[repo][event]}")
        print("\n")

input_user = input("Enter a username: ")
get_events(input_user)