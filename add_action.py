import cgi,cgitb
form = cgi.FieldStorage()

num1 = form.getvalue('num1')
num2 = form.getvalue('num2')
sum = int(num1)+int(num2)
print "Content_type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello World - First CGI Program</title>"
print "</head>"
print "<body>"
print "<h2>sum is %d"%sum,"</h2>"
print "</body>"
print "</html>"

