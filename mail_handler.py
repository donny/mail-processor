from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
import config
import notifo

class IncomingMailHandler(InboundMailHandler):
	def receive(self, mail_message):
		# We don't bother with the message body, it will be too long for Notifo.
		sender = mail_message.sender # e.g. "sender <sender@example.com>"
		subject = mail_message.subject # e.g. "Hello there..."
		to = mail_message.to # e.g. "receiver@mail-processor.appspot.com"

		to = to[:to.index('@')]

		notifo.send_notification(config.NOTIFO_SERVICE, config.NOTIFO_KEY, config.NOTIFO_USER, title=to, msg=subject)

		#END

application = webapp.WSGIApplication([('/_ah/mail/.+', IncomingMailHandler)], debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()
