# Generated by Django 4.2.3 on 2023-07-07 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('adminID', models.AutoField(primary_key=True, serialize=False)),
                ('adminName', models.CharField(max_length=200)),
                ('adminPASSWORD', models.CharField(max_length=200)),
                ('adminEMAIL', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eventID', models.AutoField(primary_key=True, serialize=False)),
                ('eventNAME', models.CharField(max_length=200)),
                ('eventDATE', models.DateField()),
                ('eventDISCRIPTION', models.TextField()),
                ('eventLOCATION', models.CharField(max_length=200)),
                ('eventSTARTTIME', models.TimeField()),
                ('eventIMAGEURL', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('OrganizerID', models.AutoField(primary_key=True, serialize=False)),
                ('OrganizerNAME', models.CharField(max_length=200)),
                ('OrganizerEMAIL', models.EmailField(max_length=200)),
                ('OrganizerREGNO', models.CharField(max_length=200)),
                ('OrganizerPHONE', models.CharField(max_length=20)),
                ('OrganizerPASSWORD', models.CharField(max_length=200)),
                ('OrganizerNIC', models.CharField(max_length=20)),
                ('adminID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.admin')),
            ],
        ),
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('QR_ID', models.AutoField(primary_key=True, serialize=False)),
                ('QR_DATA', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SalesDashboard',
            fields=[
                ('dashboardID', models.AutoField(primary_key=True, serialize=False)),
                ('top_selling_events', models.TextField()),
                ('total_revenue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('OrganizerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.organizer')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('userNAME', models.CharField(max_length=200)),
                ('userEMAIL', models.EmailField(max_length=200)),
                ('USERPASSWORD', models.CharField(max_length=200)),
                ('userPHONE', models.CharField(max_length=20)),
                ('userNIC', models.CharField(max_length=20)),
                ('adminID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.admin')),
            ],
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('ticketT_ID', models.AutoField(primary_key=True, serialize=False)),
                ('ticketT_NAME', models.CharField(max_length=200)),
                ('ticketT_PRICE', models.DecimalField(decimal_places=2, max_digits=7)),
                ('ticketDISCRIPTION', models.TextField()),
                ('ticketT_QUANTITY', models.IntegerField()),
                ('OrganizerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.organizer')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticketID', models.AutoField(primary_key=True, serialize=False)),
                ('ticketSTATUS', models.CharField(max_length=200)),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('ticketT_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.tickettype')),
            ],
        ),
        migrations.CreateModel(
            name='SalesReport',
            fields=[
                ('reportID', models.AutoField(primary_key=True, serialize=False)),
                ('NIC', models.CharField(max_length=20)),
                ('FullName', models.CharField(max_length=200)),
                ('ticketT_NAME', models.CharField(max_length=200)),
                ('TicketQUANTITY', models.IntegerField()),
                ('TicketSUBTOTAL', models.DecimalField(decimal_places=2, max_digits=7)),
                ('dashboardID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.salesdashboard')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('paymentID', models.AutoField(primary_key=True, serialize=False)),
                ('paymentSTATUS', models.CharField(max_length=200)),
                ('FullName', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('Phone', models.CharField(max_length=20)),
                ('NIC', models.CharField(max_length=20)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.user')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderID', models.AutoField(primary_key=True, serialize=False)),
                ('orderAMOUNT', models.DecimalField(decimal_places=2, max_digits=7)),
                ('orderTIME', models.DateTimeField(auto_now_add=True)),
                ('orderSTATUS', models.CharField(max_length=200)),
                ('orderDATE', models.DateField()),
                ('QR_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.qrcode')),
                ('paymentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.payment')),
                ('ticketID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.ticket')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.user')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='OrganizerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.organizer'),
        ),
    ]