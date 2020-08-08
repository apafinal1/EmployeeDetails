from django.core.management.base import BaseCommand, CommandError
from users.models import Employee


class Command(BaseCommand):
    help = 'Prints all Employee name in the database'

    def add_arguments(self, parser):
        parser.add_argument('--total', type=int, help='Indicates the number of users created')

    def handle(self, *args, **options):
        if options['total']:
            try:
                employees = Employee.objects.all()
                print("******LIST OF USER DETAILS******")
                for employee in employees:
                    self.stdout.write(self.style.SUCCESS(employee.real_name))

            except FieldDoesNotExist:
                self.stdout.write(self.style.ERROR(
                    'Field "real_name" does not exist.'))
                

            self.stdout.write(self.style.SUCCESS(
                'Successfully printed all EMPLOYEE name '))







 
