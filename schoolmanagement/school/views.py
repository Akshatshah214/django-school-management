import logging
from rest_framework import status, views
from rest_framework.response import Response
from django.http import Http404
from .serializers import PersonDataSerializer
from .models import TPersonData
from django.http import HttpRequest, HttpResponse
from django.db.models.query import QuerySet
from school.utils.constants import (
    LOGGER_NAME,
    FETCHING_ALL_DATA_START,
    FETCHING_DATA_USING_ID_START,
    FETCHING_DATA_SUCCESS,
    UNEXPECTED_EXCEPTION,
)

logger = logging.getLogger(LOGGER_NAME)


class PersonDataDetailView(views.APIView):
    def get_object(self, pk: int) -> "QuerySet[TPersonData]":
        """To Getting the fetching the data from the DB

        Args:
            pk (int): id for the TPersonData table

        Raises:
            Http404: Data not found

        Returns:
            Queryset: Retruting the queryset object
        """
        try:
            return TPersonData.objects.filter(
                pk=pk, delete_status=False
            ).first()
        except TPersonData.DoesNotExist:
            raise Http404

    def get(self, request: HttpRequest, pk: int = None) -> HttpResponse:
        """Get full details of Person Data

        Args:
            pk (int, optional): get the data for specific id. Defaults to None.

        Returns:
            json: fetched data
        """
        try:
            if not pk:
                logger.info(FETCHING_ALL_DATA_START)
                person_data = TPersonData.objects.filter(delete_status=False)
                serializer = PersonDataSerializer(person_data, many=True)
            else:
                logger.info(FETCHING_DATA_USING_ID_START % pk)
                person_data = self.get_object(pk)
                if person_data:
                    serializer = PersonDataSerializer(person_data)
            logger.info(FETCHING_DATA_SUCCESS)
            return Response(serializer.data)
        except Exception as error:
            logger.error(UNEXPECTED_EXCEPTION % error)
            return Response(
                'Data not Found!',
                status=status.HTTP_400_BAD_REQUEST,
            )

    def post(self, request: HttpRequest) -> HttpResponse:
        """Create new data for person

        Args:
            request (request): Get the data from the request

        Raises:
            Exception: Handle the unexpected error

        Returns:
            json: Data Inserted successfully
        """
        try:
            logger.info("Upload process started!")
            serializer = PersonDataSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info("Upload process completed!")
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )
            else:
                raise Exception
        except Exception as error:
            logger.error(UNEXPECTED_EXCEPTION % error)
            return Response(
                UNEXPECTED_EXCEPTION % error,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request: HttpRequest, pk: int = None) -> HttpResponse:
        """Updating the details of Person data

        Args:
            request (request): Get the data from the request
            pk (id, optional): Update data for specific id. Defaults to None.

        Raises:
            Http404: Data not found

        Returns:
            json: Return updated data
        """
        try:
            if pk:
                logger.info(f"Updating data for {pk}!")
                person_data = self.get_object(pk)
                serializer = PersonDataSerializer(
                    person_data, data=request.data
                )
                if serializer.is_valid():
                    serializer.save()
                    logger.info("Updating data process completed!")
                    return Response(serializer.data)
            else:
                raise Http404
        except Exception as error:
            logger.error(UNEXPECTED_EXCEPTION % error)
            return Response(
                UNEXPECTED_EXCEPTION % error,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request: HttpRequest, pk: int = None) -> HttpResponse:
        """Delete the data

        Args:
            pk (int, optional): Delete data for specific id. Defaults to None.

        Raises:
            Http404: data not found

        Returns:
            json: Data deleted successfully
        """
        try:
            if pk:
                logger.info(f"Delete record for {pk}!")
                person_data = self.get_object(pk)
                if person_data:
                    if not person_data.delete_status:
                        person_data.delete_status = True
                        person_data.save()
                        logger.info("Data deleted Successfully")
                        return Response(
                            f" Successfully recored deleted for {pk}",
                            status=status.HTTP_200_OK,
                        )
                else:
                    raise Exception
        except Exception as error:
            logger.error(UNEXPECTED_EXCEPTION % error)
            return Response(
                'Data not found!',
                status=status.HTTP_400_BAD_REQUEST,
            )


# class InfoListView(views.APIView):
#     """
#     List all infos, or create a new info.
#     """

#     def get(self, request):
#         infos = TPersonData.objects.filter(delete_status=False)
#         serializer = PersonDataSerializer(infos, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PersonDataSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
