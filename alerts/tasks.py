from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import StockAlert
from stocks.services import get_combined_stock


# @shared_task
# def check_stock_alerts():
#     alerts = StockAlert.objects.filter(is_active=True, is_triggered=False)

#     for alert in alerts:
#         stock_data = get_combined_stock(alert.symbol)

#         if not stock_data:
#             continue

#         current_price = stock_data.get("price")
#         if current_price is None:
#             continue

#         should_send = False

#         if alert.alert_type == "below" and float(current_price) < alert.target_price:
#             should_send = True

#         elif alert.alert_type == "above" and float(current_price) > alert.target_price:
#             should_send = True

#         if should_send:
#             subject = f"Stock Alert: {alert.symbol}"
#             message = (
#                 f"Hello {alert.user.username},\n\n"
#                 f"Your stock {alert.symbol} has reached your alert condition.\n"
#                 f"Current Price: {current_price}\n"
#                 f"Target Price: {alert.target_price}\n"
#                 f"Alert Type: {alert.alert_type}\n\n"
#                 f"Thanks,\n"
#                 f"Stock Predictor"
#             )

#             send_mail(
#                 subject,
#                 message,
#                 settings.DEFAULT_FROM_EMAIL,
#                 [alert.email],
#                 fail_silently=False,
#             )

#             alert.is_triggered = True
#             alert.save()

#     return "done"

@shared_task
def check_stock_alerts():
    alerts = StockAlert.objects.filter(is_active=True, is_triggered=False)

    for alert in alerts:
        stock_data = get_combined_stock(alert.symbol)

        if not stock_data:
            continue

        current_price = stock_data.get("price")
        if current_price is None:
            continue

        # testing only
        if alert.symbol == "TSLA":
            current_price = 293

        should_send = False

        if alert.alert_type == "below" and float(current_price) < alert.target_price:
            should_send = True

        elif alert.alert_type == "above" and float(current_price) > alert.target_price:
            should_send = True

        if should_send:
            subject = f"Stock Alert: {alert.symbol}"
            message = (
                f"Hello {alert.user.username},\n\n"
                f"Your stock {alert.symbol} has reached your alert condition.\n"
                f"Current Price: {current_price}\n"
                f"Target Price: {alert.target_price}\n"
                f"Alert Type: {alert.alert_type}\n\n"
                f"Thanks,\n"
                f"kartik choudhary ceo of kcinovations"
            )

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [alert.email],
                fail_silently=False,
            )

            alert.is_triggered = True
            alert.save()

    return "done"