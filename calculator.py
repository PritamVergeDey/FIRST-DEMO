print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Calculator</title>'
print '</head>'
print '<body>'
import cgi, cgitb

print """
    <h2>Simple Basic Calculator</h2>

<form name="frm" method="post">

 <select name="ope">
    <option value="Select">Select Operation</option>
    <option value="add">Addition</option>
    <option value="sub">Subtraction</option>
    <option value="mul">Multiplication</option>
    <option value="div">Division</option>
</select><br><br>


  Enter the 1st Number:<br>
  <input type="text" name="n1">
  <br>
  Enter the 2nd Number:<br>
  <input type="text" name="n2">
  <br><br>
  <input type="submit" value="Get Result" name="ok"><br><br>

</form>"""

frm=cgi.FieldStorage()
if frm.getvalue('ok'):
    n1=frm.getvalue('n1')
    n2=frm.getvalue('n2')
    ope=frm.getvalue('ope')
    if ope=='add':
        res=int(n1)+int(n2)
        print "The sum is %d"%res
    elif ope=='sub':
        sub=int(n1)-int(n2)
        print "The difference is %d"%sub
    elif ope=='mul':
        mul=int(n1)*int(n2)
        print "The product is %d"%mul
    elif ope=='div':
        div=int(n1)/int(n2)
        print "The Division is %d"%div
    else:
        print "Please select an Operation"

print '</body>'
print '</html>'