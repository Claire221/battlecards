# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone

# class PaymentCategory(models.Model):
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50, unique=True)
#     description = models.TextField(blank=True, null=True)

#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'budgetbuddy_category'

#     def __str__(self):
#         return self.name


# class PaymentMethod(models.Model):
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50, unique=True)
#     description = models.TextField(blank=True, null=True)

#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'budgetbuddy_payment_method'

#     def __str__(self):
#         return self.name

# class BankAccountCategory(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     category_name = models.CharField(max_length=50, unique=True)
#     category_description = models.TextField(blank=True, null=True)

#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'budgetbuddy_account_category'

#     def __str__(self):
#         return self.category_name



# class BankAccount(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     account_name = models.CharField(max_length=100)
#     account_balance = models.DecimalField(max_digits=10, decimal_places=2)
#     account_description = models.CharField(max_length=500, blank=True, null=True)
#     account_category = models.ForeignKey(BankAccountCategory, on_delete=models.CASCADE, related_name='bank_account')
    
#     account_type = models.CharField(max_length=50, choices=[
#         ('checking', 'Checking'),
#         ('savings', 'Savings'),
#         ('investment', 'Investment'),
#     ])
#     bank_name = models.CharField(max_length=100, blank=True)
#     currency = models.CharField(max_length=3, default='GBP')

#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'budgetbuddy_bank_account'

#     def __str__(self):
#         return self.account_name



# class Payment(models.Model):
#     payment_frequency_choices=[
#         ('', '---------'), 
#         ('monthly', 'Monthly'),
#         ('weekly', 'Weekly'),
#         ('yearly', 'Yearly'),
#     ]
#     payment_status_choices=[
#         ('', '---------'), 
#         ('pending', 'Pending'),
#         ('completed', 'Completed'),
#     ]
#     payment_type_choices=[
#         ('', '---------'), 
#         ('deposit', 'Deposit'),
#         ('withdrawal', 'Withdrawal'),
#         ('transfer', 'Transfer'),
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="payments")
#     payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     recurring = models.BooleanField(default=False)
#     recurring_payment_frequency = models.CharField(max_length=50, choices=payment_frequency_choices, null=True, blank=True)
#     recurring_payment_start_date = models.DateField(null=True, blank=True)
#     recurring_payment_end_date = models.DateField(null=True, blank=True)
#     status = models.CharField(max_length=50, choices=payment_status_choices)
#     category = models.ForeignKey(PaymentCategory, on_delete=models.SET_NULL, null=True, blank=True)
#     linked_transfer = models.ForeignKey('Transfer', null=True, blank=True, on_delete=models.SET_NULL)
#     payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True)
#     payment_type = models.CharField(max_length=50, choices=payment_type_choices)

#     note = models.TextField(blank=True, null=True)
    
#     payment_date = models.DateField(default=timezone.now)

#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'budgetbuddy_payment'

#     def __str__(self):
#         return f"{self.payment_amount} - {self.bank_account.account_name} - {'Recurring' if self.recurring else 'One-time'}"

# class Transfer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     withdrawal_bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="withdrawal_transfer")
#     deposit_bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="deposit_transfer")
#     payment_amount = models.DecimalField(max_digits=10, decimal_places=2)

#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'budgetbuddy_transfer'

#     def __str__(self):
#         return f"{self.payment_amount} - {self.withdrawal_bank_account} -  {self.deposit_bank_account}"