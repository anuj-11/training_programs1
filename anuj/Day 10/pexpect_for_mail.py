import pexpect
import sys
m = pexpect.spawn('python gmail_sample.py')
m.logfile_read = sys.stdout
m.expect("Username:")
m.sendline("anuj.285aj@gmail.com")
m.expect("Password:")
m.sendline("")
m.expect("To address :")
m.sendline("nirmalrajkumar1991@gmail.com")
m.expect("Subject :")
m.sendline("test")
m.expect("Enter the content. Your last line should be as 'end'")
m.sendline("hello")
m.sendline("end")
m.expect("test has been send to hbalasubramanian@asmltd.com")
m.close()
