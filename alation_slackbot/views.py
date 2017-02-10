from django.http import HttpResponse
from alation_slackbot.get_table_from_alation_api import get_table_data
import logging
import os

def slack(request, text=None):
    if not text:
        if request.method == 'GET':
            query = request.GET.get('text', '')
        elif request.method == 'POST':
            # Maybe it's in the POST as 'text', like from Slack
            # https://api.slack.com/slash-commands
            query = request.POST.get('text', '')

    logging.info("text %s" % text)
    print "text '%s'" % text
    result_data = get_table_data(query)
    return HttpResponse("Link: %s\n%s\nDescription: %s" % (
            "%s/%s" % (os.environ.get('ALATION_BASE_URL'),
                       result_data['url']),
            result_data['title'],
            result_data['description']))
