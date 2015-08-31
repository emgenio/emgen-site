# coding=utf8
import mandrill
from imapclient import IMAPClient
from email.utils import parseaddr
from .storage.helpers import find_address_and_delete
from .config import config


def do_forward(mandrill_client, id_email, raw_data):
    try:
        id = parseaddr(str(id_email))[1].split('@')[0]
        deleted_object = find_address_and_delete(id=id)
        if deleted_object:
            to = deleted_object['to']
            result = mandrill_client.messages.send_raw(
                raw_message=raw_data, from_email='proxy@emgen.io', 
                from_name='Emgen Proxy', to=[to], async=True)
            return True
        return False
    except mandrill.Error as e:
        print(e)
        return False

    pass

def main():
    mail = IMAPClient(config['mail']['host'], use_uid=True)
    mail.login(config['mail']['user'], config['mail']['password'])
    mail.select_folder('INBOX')
    messages = mail.search(['ALL'])
    if len(messages) > 0:
        response = mail.fetch(messages, ['BODY.PEEK[HEADER.FIELDS (TO)]', 'RFC822'])
        mandrill_client = mandrill.Mandrill(config['mandrill']['password'])
        for msgnum, data in response.items():
            do_forward(mandrill_client, data[b'BODY[HEADER.FIELDS (TO)]'], data[b'RFC822'])
        mail.delete_messages(messages)
        mail.expunge()
        return True
    else:
        print('No messages')
        return False

if __name__ == '__main__':
    main()