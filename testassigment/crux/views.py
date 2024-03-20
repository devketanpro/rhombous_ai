import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import CSVUploadSerializer, RecordSerializer, ColumnSerializer
from .infer_data_types import infer_and_convert_data_types
from .models import Column, Record


class CSVUploadView(APIView):
    parser_classes = (FormParser, MultiPartParser)

    def post(self, request, *args, **kwargs):

        serializer = CSVUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            df = pd.read_csv(file)
            data = infer_and_convert_data_types(df)
            columns = data.columns.tolist()
            column_types = data.dtypes.astype(str).tolist()

            for name, data_type in zip(columns, column_types):
                Column.objects.get_or_create(name=name, data_type=data_type)

            for index, row in data.iterrows():

                Record.objects.create(
                    name=row['Name'],
                    birthdate=row['Birthdate'],
                    score=row['Score'],
                    grade=row['Grade']
                )

            return Response({'success': 'file uploaded'})
        else:
            return Response(serializer.errors, status=400)


class RecordView(APIView):

    def get(self, request, *args, **kwargs):
        column_data = ColumnSerializer(Column.objects.all(), many=True)
        record_data = RecordSerializer(Record.objects.all(), many=True)

        return Response({'columns': column_data.data, 'records': record_data.data})
