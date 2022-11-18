# DO NOT USE THIS UNDER ANY CIRCUMSTANCES

This is an idiot. It listens for new messages on email. Should the message 
contain any attachment, it will open it, no questions asked. Just imagine 
what kind of mayhem this will result in!

## Usage
- Don't
- --host: imap host to connect to. Ask you cloud email what's that!
- --login, -l: imap login. Generally is the same as your email address
- --password, -p: password, duh

Make sure powershell scripts running policy is bypassed. It won't be any more 
harmful than this piece of software.

## Example
`python -m email_dumbass --host imap.mail.ru --login 'example@mail.ru' --password 'c00l_p@$$w0rd'`

