# Django-Otp-Verification
A small custom One Time Password(OTP) verification after a user registers made in Django

Just a small Tweak You have to make is by replacing the EMAIL_HOST_USER="add your email id" and below it EMAIL_HOST_PASSWORD='enter your email password'

Also in sending/views.py enter your email id in the view register....

Moreover You would also have to tweak some gmail settings if you wer using gmail as youe email for sending otp's.. You would have to decrease the gmail default security so as to make it work.
