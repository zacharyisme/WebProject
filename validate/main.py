import webapp2

form = '''
<form method="post">
     What is your Birthday?
     <br>
     <lable>Month
     <input type="text" name="month" value="%(month)s">
     </label>

     <label>Day
     <input type="text" name="day" value="%(day)s">
     </lable>

     <label>Year
     <input type="text" name="year" value="%(year)s">
     </label>
     
     <br>
     <br>
     <input type="submit">
</form>
'''


class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error":error, "month":month, "day"=day, "year"=year})


    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.write_form()

    def post(self):
        #self.write_form("That doesn't looks valid, froend!")
        self.write_form(form)

app = webapp2.WSGIApplication([
    ('/', MainPage)], debug=True)