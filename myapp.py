#!/usr/bin/env python3
"""Programming assignment 1 for COMP590."""
import json
import requests

myheaders = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSNkIiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBybnV0IHJwcm8gcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkyMjk1NDQ0LCJpYXQiOjE2NjA3NTk0NDR9.bILcGIrPRXPWRrWBZDKRLsZdtTKKqPUpZ4NZZ-U3k5g"
}
url_prefix = "https://api.fitbit.com"


def get_name():
    """Return user's name."""
    return requests.get(
        url_prefix + "/1/user/-/profile.json", headers=myheaders
    ).json()["user"]["fullName"]


def get_heartrate():
    """Return user's most recent heartrate."""
    json_request = requests.get(
        url_prefix + "/1/user/-/activities/heart/date/today/1d/1min.json",
        headers=myheaders,
    ).json()["activities-heart-intraday"]["dataset"]
    for i in range(len(json_request)):
        if json_request[0 - i - 1]["value"] != 0:
            return (
                "Your most recent heart rate recorded was "
                + str(json_request[0 - i - 1]["value"])
                + " at time "
                + json_request[0 - i - 1]["time"]
            )


def get_steps():
    """Return user's step count for today."""
    return (
        "Your total step count for today is "
        + str(
            requests.get(
                url_prefix + "/1/user/-/activities/date/today.json", headers=myheaders,
            ).json()["summary"]["steps"]
        )
        + " steps"
    )


def get_sleep():
    """Return user's sleep information for last night."""
    minutes = requests.get(
        url_prefix + "/1.2/user/-/sleep/date/today.json", headers=myheaders
    ).json()["summary"]["totalMinutesAsleep"]
    return (
        "You slept for "
        + str(int(minutes / 60))
        + " hours and "
        + str(minutes % 60)
        + " minutes last night"
    )


def get_activeness():
    """Return user's activity level for today."""
    activity_summary = requests.get(
        url_prefix + "/1/user/-/activities/date/today.json", headers=myheaders
    ).json()["summary"]
    return (
        "Today, you were sedentary for "
        + str(activity_summary["sedentaryMinutes"])
        + " minutes, you were fairly active for "
        + str(activity_summary["fairlyActiveMinutes"])
        + " minutes, and you were very active for "
        + str(activity_summary["veryActiveMinutes"])
        + " minutes"
    )


print(get_name())
print(get_heartrate())
print(get_steps())
print(get_sleep())
print(get_activeness())
