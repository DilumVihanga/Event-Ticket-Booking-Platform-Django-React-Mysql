from django.db import models

# Create your models here.


class Admin(models.Model):
    adminID = models.AutoField(primary_key=True)
    adminName = models.CharField(max_length=200)
    adminPASSWORD = models.CharField(max_length=200)
    adminEMAIL = models.EmailField(max_length=200)

    def __str__(self):
        return self.adminName


class Organizer(models.Model):
    organizerID = models.AutoField(primary_key=True)
    adminID = models.ForeignKey('Admin', on_delete=models.CASCADE)
    organizerNAME = models.CharField(max_length=200)
    organizerEMAIL = models.EmailField(max_length=200)
    organizerREGNO = models.CharField(max_length=200)
    organizerPHONE = models.CharField(max_length=20)
    organizerPASSWORD = models.CharField(max_length=200)
    organizerNIC = models.CharField(max_length=20)

    def __str__(self):
        return self.organizerNAME


class User(models.Model):
    userID = models.AutoField(primary_key=True)
    adminID = models.ForeignKey('Admin', on_delete=models.CASCADE)
    userNAME = models.CharField(max_length=200)
    userEMAIL = models.EmailField(max_length=200)
    USERPASSWORD = models.CharField(max_length=200)
    userPHONE = models.CharField(max_length=20)
    userNIC = models.CharField(max_length=20)

    def __str__(self):
        return self.userNAME


class Event(models.Model):
    eventID = models.AutoField(primary_key=True)
    organizerID = models.ForeignKey('Organizer', on_delete=models.CASCADE)
    eventNAME = models.CharField(max_length=200)
    eventDATE = models.DateField()
    eventDISCRIPTION = models.TextField()
    eventLOCATION = models.CharField(max_length=200)
    eventSTARTTIME = models.TimeField()
    eventIMAGE = models.ImageField(upload_to='uploads/images', null=True, blank=False)

    def __str__(self):
        return self.eventNAME


class TicketType(models.Model):
    ticketT_ID = models.AutoField(primary_key=True)
    organizerID = models.ForeignKey('Organizer', on_delete=models.CASCADE)
    ticketT_NAME = models.CharField(max_length=200)
    ticketT_PRICE = models.DecimalField(max_digits=7, decimal_places=2)
    ticketDISCRIPTION = models.TextField()
    ticketT_QUANTITY = models.IntegerField()

    def __str__(self):
        return self.ticketT_NAME


class Ticket(models.Model):
    ticketID = models.AutoField(primary_key=True)
    eventID = models.ForeignKey('Event', on_delete=models.CASCADE)
    ticketT_ID = models.ForeignKey('TicketType', on_delete=models.CASCADE)
    ticketSTATUS = models.CharField(max_length=200)

    def __str__(self):
        return str(self.ticketID)


class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    userID = models.ForeignKey('User', on_delete=models.CASCADE)
    paymentID = models.ForeignKey('Payment', on_delete=models.CASCADE)
    ticketID = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    qrcodeID = models.ForeignKey('QRCode', on_delete=models.CASCADE)
    orderAMOUNT = models.DecimalField(max_digits=7, decimal_places=2)
    orderTIME = models.DateTimeField(auto_now_add=True)
    orderSTATUS = models.CharField(max_length=200)
    orderDATE = models.DateField()

    def __str__(self):
        return str(self.orderID)


class Payment(models.Model):
    paymentID = models.AutoField(primary_key=True)
    userID = models.ForeignKey('User', on_delete=models.CASCADE)
    paymentSTATUS = models.CharField(max_length=200)
    fullName = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    nic = models.CharField(max_length=20)

    def __str__(self):
        return str(self.paymentID)


class QRCode(models.Model):
    qrcodeID = models.AutoField(primary_key=True)
    qrDATA = models.CharField(max_length=200)

    def __str__(self):
        return str(self.qrcodeID)


class SalesDashboard(models.Model):
    dashboardID = models.AutoField(primary_key=True)
    organizerID = models.ForeignKey('Organizer', on_delete=models.CASCADE)
    topSellingEvents = models.TextField()
    totalRevenue = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.dashboardID)


class SalesReport(models.Model):
    reportID = models.AutoField(primary_key=True)
    dashboardID = models.ForeignKey('SalesDashboard', on_delete=models.CASCADE)
    nic = models.CharField(max_length=20)
    fullName = models.CharField(max_length=200)
    ticketT_NAME = models.CharField(max_length=200)
    ticketQUANTITY = models.IntegerField()
    ticketSUBTOTAL = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.reportID)
