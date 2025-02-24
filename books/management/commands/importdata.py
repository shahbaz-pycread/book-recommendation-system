from django.core.management.base import BaseCommand
from books.models import Book
import csv
class Command(BaseCommand):
    help = "Import data into database from CSV"
    
    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to the CSV file")
    
    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        print(file_path)
        # Open the file with read mode
        with open(file_path,'r') as file:
            # Read the file
            reader = csv.DictReader(file)
            for row in reader:
                # Create the data
                Book.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data Imported Successfully'))    