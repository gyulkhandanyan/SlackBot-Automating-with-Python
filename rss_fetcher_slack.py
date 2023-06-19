#!/usr/bin/python

import feedparser
import requests
import json
import argparse
import sys

# argpars music, health

parser = argparse.ArgumentParser(
    prog='adds music and health arguments to cli',
    description='defines health and music arguments',
    epilog='Text at the bottom of help')

parser.add_argument('-m', '--music', action='store_true')
parser.add_argument('-H', '--health', action='store_true')
parser.add_argument('-n', '--news', action='store_true')

args = parser.parse_args()

is_music = args.music
is_health = args.health
is_news = args.news


def fetch_and_parse_rss(url):
    return feedparser.parse(url)


def get_first_entry(url):
    parsed_feed = fetch_and_parse_rss(url)
    return parsed_feed.entries[0].link


def send_slack_message(payload, webhook):
    return requests.post(webhook, json.dumps(payload))


if is_music:
    link_music = get_first_entry('https://rss.app/feeds/jAOa1YTPKxhIhlZz.xml')
    webhook = "https://hooks.slack.com/services/your_slackworkplace_ID"
    payload = {"text": f"Have some fun! {link_music}"}
    send_slack_message(payload, webhook)

if is_health:
    link_health = get_first_entry('https://www.health.nsw.gov.au/_layouts/15/feed.aspx?xsl=1&web=/news&page=d6828794-f20b-4d11-839e-9edd75d483ff&wp=cf6e281c-d6f6-4c22-b78f-e6890eccd5fb&pageurl=/news/Pages/rss-minister-for-mental-health.aspx')
    webhook = "https://hooks.slack.com/services/your_slackworkplace_ID"
    payload = {"text": f"Health news are here! {link_health}"}
    send_slack_message(payload, webhook)

if is_news:
    link_news = get_first_entry('https://rss.app/feeds/jAOa1YTPKxhIhlZz.xml')
    webhook = "https://hooks.slack.com/services/your_slackworkplace_ID"
    payload = {"text": f"Morning! IT News for today! {link_news}"}
    send_slack_message(payload, webhook)




