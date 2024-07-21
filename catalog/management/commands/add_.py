from django.core.management import BaseCommand, call_command

class Command(BaseCommand):

    def handle(self, *args, **options):

        call_command('flush', '--noinput')


        call_command('loaddata', 'catalog_data.json')
        call_command('loaddata', 'product_data.json')

        self.stdout.write(self.style.SUCCESS('Successfully'))
