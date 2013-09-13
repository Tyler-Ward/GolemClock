
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

  def _PrintUserCalendars(self):
    """Retrieves the list of calendars to which the authenticated user either
    owns or subscribes to.  This is the same list as is represented in the
    Google Calendar GUI.  Although we are only printing the title of the
    calendar in this case, other information, including the color of the
    calendar, the timezone, and more.  See CalendarListEntry for more details
    on available attributes."""

    feed = self.cal_client.GetAllCalendarsFeed()
    print 'Printing allcalendars: %s' % feed.title.text
    for i, a_calendar in zip(xrange(len(feed.entry)), feed.entry):
      print '\t%s. %s' % (i, a_calendar.title.text,)

  def _PrintOwnCalendars(self):
    """Retrieves the list of calendars to which the authenticated user
    owns --
    Although we are only printing the title of the
    calendar in this case, other information, including the color of the
    calendar, the timezone, and more.  See CalendarListEntry for more details
    on available attributes."""

    feed = self.cal_client.GetOwnCalendarsFeed()
    print 'Printing owncalendars: %s' % feed.title.text
    for i, a_calendar in zip(xrange(len(feed.entry)), feed.entry):
      print '\t%s. %s' % (i, a_calendar.title.text,)

  def _PrintAllEventsOnDefaultCalendar(self):
    """Retrieves all events on the primary calendar for the authenticated user.
    In reality, the server limits the result set intially returned.  You can
    use the max_results query parameter to allow the server to send additional
    results back (see query parameter use in DateRangeQuery for more info).
    Additionally, you can page through the results returned by using the
    feed.GetNextLink().href value to get the location of the next set of
    results."""

    feed = self.cal_client.GetCalendarEventFeed()
    print 'Events on Primary Calendar: %s' % (feed.title.text,)
    for i, an_event in zip(xrange(len(feed.entry)), feed.entry):
      print '\t%s. %s' % (i, an_event.title.text,)
      for p, a_participant in zip(xrange(len(an_event.who)), an_event.who):
        print '\t\t%s. %s' % (p, a_participant.email,)
        print '\t\t\t%s' % (a_participant.value,)
        if a_participant.attendee_status:
          print '\t\t\t%s' % (a_participant.attendee_status.value,)

  def _FullTextQuery(self, text_query='Tennis'):
    """Retrieves events from the calendar which match the specified full-text
    query.  The full-text query searches the title and content of an event,
    but it does not search the value of extended properties at the time of
    this writing.  It uses the default (primary) calendar of the authenticated
    user and uses the private visibility/full projection feed.  Please see:
    http://code.google.com/apis/calendar/reference.html#Feeds
    for more information on the feed types.  Note: as we're not specifying
    any query parameters other than the full-text query, recurring events
    returned will not have gd:when elements in the response.  Please see
    the Google Calendar API query paramters reference for more info:
    http://code.google.com/apis/calendar/reference.html#Parameters"""

    print 'Full text query for events on Primary Calendar: \'%s\'' % (
        text_query,)
    query = gdata.calendar.client.CalendarEventQuery(text_query=text_query)
    feed = self.cal_client.GetCalendarEventFeed(q=query)
    for i, an_event in zip(xrange(len(feed.entry)), feed.entry):
      print '\t%s. %s' % (i, an_event.title.text,)
      print '\t\t%s. %s' % (i, an_event.content.text,)
      for a_when in an_event.when:
        print '\t\tStart time: %s' % (a_when.start,)
        print '\t\tEnd time:   %s' % (a_when.end,)

  def _DateRangeQuery(self, start_date='2007-01-01', end_date='2007-07-01'):
    """Retrieves events from the server which occur during the specified date
    range.  This uses the CalendarEventQuery class to generate the URL which is
    used to retrieve the feed.  For more information on valid query parameters,
    see: http://code.google.com/apis/calendar/reference.html#Parameters"""

    print 'Date range query for events on Primary Calendar: %s to %s' % (
        start_date, end_date,)
    query = gdata.calendar.client.CalendarEventQuery(start_min=start_date, start_max=end_date)
    feed = self.cal_client.GetCalendarEventFeed(q=query)
    for i, an_event in zip(xrange(len(feed.entry)), feed.entry):
      print '\t%s. %s' % (i, an_event.title.text,)
      for a_when in an_event.when:
        print '\t\tStart time: %s' % (a_when.start,)
        print '\t\tEnd time:   %s' % (a_when.end,)


  def Run(self, delete='false'):
   

    # Getting feeds and query results
    self._PrintUserCalendars()
    self._PrintOwnCalendars()
    self._PrintAllEventsOnDefaultCalendar()
    self._FullTextQuery()
    self._DateRangeQuery()
      


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
