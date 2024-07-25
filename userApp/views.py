from io import BytesIO

import qrcode
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *


class QRCodeAPIView(APIView):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user)
        user_data = serializer.data

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(user_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        buffer.seek(0)

        file_path = f"{username}_qrcode.png"
        with open(file_path, 'wb') as f:
            f.write(buffer.getvalue())

        response = FileResponse(open(file_path, 'rb'), content_type='image/png')
        response['Content-Disposition'] = f'attachment; filename="{file_path}"'

        return response
