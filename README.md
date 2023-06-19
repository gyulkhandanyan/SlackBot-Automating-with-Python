# SlackBot-Automating-with-Python

## Project Description
This project automates the process of posting messages in a specific Slack channel to enhance communication and streamline the workflow within a team. It achieves this by creating a SlackBot using Python.

## Fetching Latest News
The Python code has been written to fetch the latest news from RSS feeds of three different sources: iTNews, Music, and Health. The feedparser library has been utilized to parse the **RSS feeds** and retrieve the relevant information.

## Automating Posting of News URLs
The automation of posting the fetched news URLs to the designated Slack channel has been implemented. This is achieved through a combination of a cron job (using crontab) and a command-line interface (CLI).

For iTNews, the URLs are automatically posted daily at 9 am using the -n or --news flag.
Customization options are available for Music and Health using the -m or --music and -H or --health flags.
Sending Messages to Slack Channel
To send messages to the Slack channel, a webhook is utilized. **Webhooks** provide a way to send messages to a specific channel without directly interacting with the Slack API. The Python code uses the requests library to send HTTP/1.1 requests to the webhook.

## Python Libraries Used
The project makes use of the following Python libraries:

**requests** for HTTP requests
**json** for encoding and decoding JSON data
**argparse** for handling command-line arguments
**feedparser** for parsing RSS feeds

## Summary
This project successfully automates the process of posting messages containing the latest news URLs from RSS feeds to a Slack channel. It utilizes Python, cron jobs, command-line interface, webhooks, and relevant libraries to achieve automation. The implementation improves communication and streamlines the workflow within the team.