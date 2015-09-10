#!/usr/bin/env python

from django.core.management.base import BaseCommand, CommandError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class Command(BaseCommand):
    args = '<username username ...>'
    help = 'Creates token for specified usernames in parameters'

    def handle(self, *args, **options):
        for username in set(args):
            try:
                uobj = User.objects.get(username=username)
                try:
                    token = Token.objects.create(user=uobj)
                    self.stdout.write("{0}:{1}".format(username, token.key))
                except Exception, e:
                    self.stderr.write("Failed to create token for user {0}".format(username))
                    self.stderr.write(str(e))
            except Exception, e:
                self.stderr.write("User {0} does not exists".format(username))
                self.stderr.write(str(e))
