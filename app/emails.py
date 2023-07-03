from flask_mail import Message
from flask import current_app, render_template


def book_purchase_confirmation(mail, user, book):
    try:
        message = Message('Confirmación De Compra De Libro',
                          sender=current_app.config['MAIL_USERNAME'],
                          recipients=['andresgc1997@outlook.com'])

        message.html = render_template(
            'emails/confirmacion_compras_libros.html', user=user, book=book)

        mail.send(message)

    except Exception as ex:
        raise Exception(ex)
