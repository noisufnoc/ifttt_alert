import sys
import json
import urllib2

# TODO: http://docs.splunk.com/Documentation/Splunk/6.4.1/
#           AdvancedDev/ModAlertsAdvancedExample
# TODO: post to
#       https://maker.ifttt.com/trigger/{event}/with/key/d1AI5fcfPLqMMkR6keVluB
# TODO: params:
#   event
#   key
#   value1
#   value2
#   value3


def trigger_ifttt(settings):
    # stuff goes here
    api_prefix = settings.get('api_prefix')
    api_suffix = settings.get('api_suffix')
    # Need to validate key is present, else fail.
    key = settings.get('api.channel_key')

    # event =
    # value1 =
    # value2 =
    # value3 =

    print >> sys.stderr, "%s Foo: %s, Bar: %s" % (key, api_prefix, api_suffix)
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
