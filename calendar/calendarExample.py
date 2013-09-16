try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom
import getopt
import sys
import string
import time


class CalendarExample:

  def __init__(self, email, password):
    """Creates a CalendarService and provides ClientLogin auth details to it.
    The email and password are required arguments for ClientLogin.  The
    CalendarService automatically sets the service to be 'cl', as is
    appropriate for calendar.  The 'source' defined below is an arbitrary
    string, but should be used to reference your name or the name of your
    organization, the app name and version, with '-' between each of the three
    values.  The account_type is specified to authenticate either
    Google Accounts or Google Apps accounts.  See gdata.service or
    http://code.google.com/apis/accounts/AuthForInstalledApps.html for more
    info on ClientLogin.  NOTE: ClientLogin should only be used for installed
    applications and not for multi-user web applications."""

    self.cal_client = gdata.calendar.client.CalendarClient(source='Google-Calendar_Python_Sample-1.0')
    self.cal_client.ClientLogin(email, password, self.cal_client.source);

  
  def _RetrieveEventsOnDefaultCalendar(self):

    feed = self.cal_client.GetCalendarEventFeed()
    results={"type":"calendar", "messages": []}
    #print 'Events on Primary Calendar: %s' % (feed.title.text,)
    results["messages"].append("first event: " +feed.entry[0].when[0].start)
    results["messages"].append("# events: " +str(len(feed.entry)))
    results["first_event"] = feed.entry[0].title.text
    return results


  def Run(self, delete='false'):
   
    self._RetrieveEventsOnDefaultCalendar()
      


def main():
  """Runs the CalendarExample application with the provided username and
  and password values.  Authentication credentials are required.
  NOTE: It is recommended that you run this sample using a test account."""

  # parse command line options
  try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["user=", "pw=", "delete="])
  except getopt.error, msg:
    print ('python calendarExample.py --user [username] --pw [password] ' +
        '--delete [true|false] ')
    sys.exit(2)

  user = ''
  pw = ''
  delete = 'false'

  # Process options
  for o, a in opts:
    if o == "--user":
      user = a
    elif o == "--pw":
      pw = a
    elif o == "--delete":
      delete = a

  if user == '' or pw == '':
    print ('python calendarExample.py --user [username] --pw [password] ' +
        '--delete [true|false] ')
    sys.exit(2)

  sample = CalendarExample(user, pw)
  sample.Run(delete)

if __name__ == '__main__':
  main()
