from django import forms
from django.forms.widgets import DateInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import PaymentCategory, PaymentMethod, BankAccount, Payment, Transfer, BankAccountCategory

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class PaymentCategoryForm(forms.ModelForm):
    class Meta:
        model = PaymentCategory
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter a description for the category...'}),
        }

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter a description for the payment method...'}),
        }

class BankAccountCategoryForm(forms.ModelForm):
    class Meta:
        model = BankAccountCategory
        fields = [
            'category_name', 
            'category_description', 
        ]
        widgets = {
            'category_name': forms.TextInput(attrs={'placeholder': 'Category Name'}),
            'category_description': forms.TextInput(attrs={'rows': 3, 'placeholder': 'Enter category description...'}),
        }


class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = [
            'account_name', 
            'account_balance', 
            'account_description', 
            'account_type', 
            'bank_name', 
            'currency',
            "account_category"
        ]
        widgets = {
            'account_name': forms.TextInput(attrs={'placeholder': 'Account Name'}),
            'account_balance': forms.NumberInput(attrs={'placeholder': 'Account Balance', 'step': '0.01'}),
            'account_description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter account description...'}),
            'account_type': forms.Select(choices=[
                ('checking', 'Checking'),
                ('savings', 'Savings'),
                ('investment', 'Investment'),
            ]),
            'bank_name': forms.TextInput(attrs={'placeholder': 'Bank Name'}),
            'currency': forms.TextInput(attrs={'placeholder': 'Currency (e.g., USD, GBP)', 'maxlength': '3'}),
        }

        label = {
            'account_category' : "Select category for account"
        }
        
class PaymentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['bank_account'].queryset = BankAccount.objects.filter(user=user)

        user = kwargs.pop('user', None)  # You can pass request.user to the form
        super().__init__(*args, **kwargs)

        # Optionally filter accounts by user
        accounts = BankAccount.objects.all()
        if user:
            accounts = accounts.filter(user=user)

        # Custom labels like: "Main bank 2 (£420.00)"
        self.fields['bank_account'].queryset = accounts
        self.fields['bank_account'].label_from_instance = lambda obj: f"{obj.account_name} (£{obj.account_balance})"

        self.fields['payment_amount'].queryset = accounts
        self.fields['payment_amount'].label_from_instance = lambda obj: f"{obj.account_name} (£{obj.account_balance})"

    class Meta:
        model = Payment
        fields = [
            'bank_account',
            'payment_amount',
            'recurring',
            'recurring_payment_frequency',
            'recurring_payment_start_date',
            'recurring_payment_end_date',
            'category',
            'payment_method',
            'note',
            'payment_date',
            'payment_type',
        ]
        widgets = {
            'bank_account': forms.Select(),
            'payment_amount': forms.NumberInput(attrs={'placeholder': 'Payment Amount', 'step': '0.01'}),
            'recurring': forms.Select(choices=[
                ('--------', '--------'),
                ('yes', 'Yes'),
                ('no', 'No'),
            ]),
            'recurring_payment_frequency': forms.Select(),
            'recurring_payment_start_date': forms.DateInput(attrs={'type': 'date'}),
            'recurring_payment_end_date': forms.DateInput(attrs={'type': 'date'}),
            'category': forms.Select(),
            'payment_method': forms.Select(),
            'note': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Additional notes about the payment...'}),
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
            'payment_type': forms.Select(),
        }
        labels = {
            'bank_account': "Select the bank account this payment will come from",
            'payment_amount': "What is the payment amount?",
            'recurring': "Is this a recurring payment?",
            'recurring_payment_frequency': "How often should this payment recur?",
            'recurring_payment_start_date': "Start date for the recurring payment schedule",
            'recurring_payment_end_date': "End date for the recurring payment schedule",
            'category': "Select the payment category",
            'payment_method': "Select the payment method",
            'note': "Add a note (optional)",
            'payment_date': "What date should this payment be withdrawn?",
            'payment_type': "Select the payment type",
        }

class TransferForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # You can pass request.user to the form
        super().__init__(*args, **kwargs)

        # Optionally filter accounts by user
        accounts = BankAccount.objects.all()
        if user:
            accounts = accounts.filter(user=user)

        # Custom labels like: "Main bank 2 (£420.00)"
        self.fields['withdrawal_bank_account'].queryset = accounts
        self.fields['withdrawal_bank_account'].label_from_instance = lambda obj: f"{obj.account_name} (£{obj.account_balance})"

        self.fields['deposit_bank_account'].queryset = accounts
        self.fields['deposit_bank_account'].label_from_instance = lambda obj: f"{obj.account_name} (£{obj.account_balance})"
    class Meta:
        model = Transfer
        fields = [
            'withdrawal_bank_account',
            'deposit_bank_account',
            'payment_amount',
        ]
        widgets = {
            'withdrawal_bank_account': forms.Select(),
            'deposit_bank_account': forms.Select(),
            'payment_amount': forms.NumberInput(attrs={'placeholder': 'Payment Amount', 'step': '0.01'}),

        }
