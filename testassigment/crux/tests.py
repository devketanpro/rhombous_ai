from django.test import TestCase, Client
from rest_framework import status
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
import tempfile


class CSVUploadAPITest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_csv_upload_success(self):
        # Prepare a sample CSV file for upload
        csv_content = b"Name,Age\nJohn,30\nAlice,25\n"
        csv_file = SimpleUploadedFile("data.csv", csv_content, content_type="text/csv")

        # Make a POST request to the API endpoint
        url = reverse('csv-upload')
        response = self.client.post(url, {'file': csv_file}, format='multipart')

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the expected message
        self.assertEqual(response.data, {'message': 'File uploaded successfully'})

    def test_csv_upload_invalid_file(self):
        # Prepare an invalid file for upload (e.g., non-CSV file)
        invalid_file = tempfile.NamedTemporaryFile(suffix=".txt")

        # Make a POST request to the API endpoint with the invalid file
        url = reverse('csv-upload')
        response = self.client.post(url, {'file': invalid_file}, format='multipart')

        # Check that the response status code is 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check that the response contains an error message
        self.assertIn('file', response.data)

    def test_csv_upload_missing_file(self):
        # Make a POST request to the API endpoint without providing a file
        url = reverse('csv-upload')
        response = self.client.post(url)

        # Check that the response status code is 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check that the response contains an error message
        self.assertIn('file', response.data)
