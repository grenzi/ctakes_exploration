# -*- coding: utf-8 -*-

"""
Copyright (C) 2011 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# Django
from django import forms

PORT = 1414
MAX_CHARS = 100

class CreateForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'style':'width:100%'}))
    host = forms.CharField(widget=forms.TextInput(attrs={'style':'width:50%'}))
    port = forms.CharField(initial=PORT, widget=forms.TextInput(attrs={'style':'width:20%'}))
    queue_manager = forms.CharField(widget=forms.TextInput(attrs={'style':'width:50%'}))
    channel = forms.CharField(widget=forms.TextInput(attrs={'style':'width:100%'}))
    cache_open_send_queues = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'checked':'checked'}))
    cache_open_receive_queues = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'checked':'checked'}))
    use_shared_connections = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'checked':'checked'}))
    ssl = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    ssl_cipher_spec = forms.CharField(widget=forms.TextInput(attrs={'style':'width:100%'}))
    ssl_key_repository = forms.CharField(widget=forms.TextInput(attrs={'style':'width:100%'}))
    needs_mcd = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    max_chars_printed = forms.CharField(initial=MAX_CHARS, widget=forms.TextInput(attrs={'style':'width:20%'}))

class EditForm(CreateForm):
    cache_open_send_queues = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    cache_open_receive_queues = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    use_shared_connections = forms.BooleanField(required=False, widget=forms.CheckboxInput())
