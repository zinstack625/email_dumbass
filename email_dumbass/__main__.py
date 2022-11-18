#!/usr/bin/env python3

import argparse
from imap_tools import MailBox, A, errors
import logging as log
import os
import subprocess

mailbox: MailBox = None


def main():
    while (True):
        resp = mailbox.idle.wait(30)
        if resp:
            for msg in mailbox.fetch(A(seen=False)):
                for attr in msg.attachments:
                    with open(f'files/{attr.filename}', 'wb') as f:
                        f.write(attr.payload)
                    subprocess.run(['powershell', '-c', 'start', f'files/{attr.filename}'])


if __name__ == "__main__":
    cli_args = argparse.ArgumentParser()
    cli_args.add_argument('--host', required=True)
    cli_args.add_argument('-l', '--login', required=True)
    cli_args.add_argument('-p', '--password', required=True)
    args = cli_args.parse_args()
    try:
        mailbox = MailBox(args.host).login(args.login, args.password)
    except errors.MailboxLoginError:
        log.error('Unable to login into IMAP, check input arguments!')
        raise errors.MailboxLoginError
    os.mkdir('files')
    main()