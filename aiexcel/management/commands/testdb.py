from django.core.management.base import BaseCommand
import psycopg2

class Command(BaseCommand):
    help = 'Test the database connection'

    def handle(self, *args, **options):
        try:
            connection = psycopg2.connect(
                dbname='aiexcel',
                user='rupacesigdel',
                password='rupesh@123',
                host='localhost',
                port='5432'
            )
            self.stdout.write(self.style.SUCCESS('Connection successful'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Connection failed: {str(e)}'))
