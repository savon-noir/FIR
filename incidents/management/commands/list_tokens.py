#!/usr/bin/env python

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class Command(BaseCommand):
    help = 'list users'

    def handle(self, *args, **options):
        tokenlist = Token.objects.all()
        for tk in tokenlist:
            u = User.objects.get(id=tk.user_id)
            self.stdout.write("{0}:{1}".format(u.username, tk.key))
