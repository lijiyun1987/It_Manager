from django import forms
from django.db import models
from .models import Machine, Maintenance
from django.contrib.auth.models import User
import re


class MaintenanceFrom(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = '__all__'
        labels = {'mac_id':'机器编号',
                  'problem_des':'故障描述',
                  'solution':'处理描述',
                  'results':'是否解决故障',
                  'new_n':'新备件PN',
                  'new_sn':'新备件SN',
                  'old_pn':'坏件PN',
                  'old_sn':'坏件SN',
                  'date':'处理日期'
                  }
        widgets = {'mac_id':forms.TextInput(attrs={'class': 'textinput'}),
                    'date':forms.SelectDateWidget,
                   }

class OpsLogFrom(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = '__all__'
        labels = {'ops_obj':'机器编号',
                  'ops_subject':'故障描述',
                  'ops_log':'处理描述',
                  'des':'是否解决故障',
                  'date':'处理日期'
                  }
        widgets = {'ops_log':forms.TextInput(attrs={'class': 'textinput'}),
                    'date':forms.SelectDateWidget,
                   }

class  SearchForm(forms.Form):
    # keyword = forms.CharField(min_length=1)
    # keyword = forms.CharField(min_length=1, max_length=50)
    keyword = forms.CharField(min_length=1,
                              max_length=50,
                              widget=forms.TextInput(attrs={
                                  'class': 'form-control mr-sm-2',
                                  'type': 'search',
                                  'placeholder': 'Search',
                                  'aria-label': 'Search'
                              })
                              )

# class MacForm(forms.ModelForm):
#     class Meta:
#         model = Machine
#         fields = '__all__'
#         labels = {'mac_id': '机器编号',
#                   'vender': '厂家',
#                   'mac_type': '设备类型',
#                   'model_id': '设备型号',
#                   'mac_sn': '设备SN',
#                   'use_des': '使用描述',
#                   'location': '位置',
#                   'ipmi': 'IPMI地址',
#                   'level': '等级'
#                   }
#         error_messages = {'ipmi':{'invalid':'请输入正确格式的IP地址'},
#
#                           }

# from django.forms import formset_factory
# from .forms import macform
#
# macformset = formset_factory(macform, extra=2, max_num=5)

# def email_check(email):
#     pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
#     return re.match(pattern, email)
#
#
# class RegistrationForm(forms.Form):
#
#     username = forms.CharField(label='Username', max_length=50)
#     email = forms.EmailField(label='Email',)
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
#
#     # Use clean methods to define custom validation rules
#
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#
#         if len(username) < 6:
#             raise forms.ValidationError("Your username must be at least 6 characters long.")
#         elif len(username) > 50:
#             raise forms.ValidationError("Your username is too long.")
#         else:
#             filter_result = User.objects.filter(username__exact=username)
#             if len(filter_result) > 0:
#                 raise forms.ValidationError("Your username already exists.")
#
#         return username
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#
#         if email_check(email):
#             filter_result = User.objects.filter(email__exact=email)
#             if len(filter_result) > 0:
#                 raise forms.ValidationError("Your email already exists.")
#         else:
#             raise forms.ValidationError("Please enter a valid email.")
#
#         return email
#
#     def clean_password1(self):
#         password1 = self.cleaned_data.get('password1')
#
#         if len(password1) < 6:
#             raise forms.ValidationError("Your password is too short.")
#         elif len(password1) > 20:
#             raise forms.ValidationError("Your password is too long.")
#
#         return password1
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Password mismatch. Please enter again.")
#
#         return password2
#
#
# class LoginForm(forms.Form):
#
#     username = forms.CharField(label='Username', max_length=50)
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#
#     # Use clean methods to define custom validation rules
#
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#
#         if email_check(username):
#             filter_result = User.objects.filter(email__exact=username)
#             if not filter_result:
#                 raise forms.ValidationError("This email does not exist.")
#         else:
#             filter_result = User.objects.filter(username__exact=username)
#             if not filter_result:
#                            raise forms.ValidationError("This username does not exist. Please register first.")
#
#         return username

