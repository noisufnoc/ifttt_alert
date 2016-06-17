import sys
import json
import urllib

# TODO: http://docs.splunk.com/Documentation/Splunk/6.4.1/
#           AdvancedDev/ModAlertsAdvancedExample
# TODO: post to
#       https://maker.ifttt.com/trigger/{event}/with/key/d1AI5fcfPLqMMkR6keVluB
# TODO: params:


def trigger_ifttt(settings):
    # stuff goes here
    api_prefix = settings.get('api_prefix')
    api_suffix = settings.get('api_suffix')
    # Need to validate key is present, else fail.
    key = settings.get('api_key')

    event = settings.get('event')
    value1 = settings.get('value1')
    value2 = settings.get('value2')
    value3 = settings.get('value3')

    url = api_prefix + event + api_suffix + key

    print >> sys.stderr, "URL: %s%s%s%s" % (api_prefix, event, api_suffix, key)
    print >> sys.stderr, "Data: %s, %s, %s" % (value1, value2, value3)

    data = urllib.urlencode(
        {"value1": value1, "value2": value2, "value3": value3}
    )
    u = urllib.urlopen(url, data)

    return True


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--execute":
        payload = json.loads(sys.stdin.read())
        print >> sys.stderr, "INFO Payload: %s" % json.dumps(payload)
        if not trigger_ifttt(payload.get('configuration')):
            print >> sys.stderr, "FATAL Failed trying to trigger IFTTT"
            sys.exit(2)
        else:
            print >> sys.stderr, "INFO IFTTT triggered successfully"
    else:
        print >> sys.stderr, "FATAL Unsupported execution mode\
            (expected --execute flag)"
        sys.exit(1)
