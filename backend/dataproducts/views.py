from dataproducts.models import ETLLogs, LulinDataProduct
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from targets.models import Target

from .serializers import ETLLogsSerializer, LulinDataProductSerializer


@extend_schema(request=None, responses=ETLLogsSerializer)
@permission_classes((AllowAny,))
@api_view(['GET'])
def get_etl_logs(request):
    etl_logs = ETLLogs.objects.all().order_by('-created_at')[:5]

    serializer = ETLLogsSerializer(etl_logs, many=True)

    return Response(serializer.data, status=200)


class LulinTargetDataView(APIView):
    @permission_classes((AllowAny,))
    def get(self, request, pk):
        if pk == 0:
            all_data = LulinDataProduct.objects.all().order_by('-mjd')

            if all_data.exists():
                latest_mjd = all_data.first().mjd
                three_days_ago_mjd = latest_mjd - 3
                data = all_data.filter(mjd__gte=three_days_ago_mjd)
            else:
                data = all_data

            serializer = LulinDataProductSerializer(data, many=True)
            return Response(serializer.data, status=200)

        target = get_object_or_404(
            Target,
            pk=pk,
            user=request.user,
            deleted_at__isnull=True
        )

        data_products = target.lulin_data_products.all()

        serializer = LulinDataProductSerializer(data_products, many=True)
        return Response(serializer.data, status=200)
