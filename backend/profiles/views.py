# views.py
from rest_framework import generics, status, serializers
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer

class BaseUserProfileView(generics.GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def extract_error_message(self, e):
        if isinstance(e, serializers.ValidationError) and e.detail:
            # Extract the first error message string from any key in ErrorDetail
            for key, value in e.detail.items():
                if isinstance(value, list) and value:
                    return value[0]
        return str(e)

class UserProfileListCreateView(BaseUserProfileView, generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        try:
            # Handle GET request to list all user profiles
            return self.list(request, *args, **kwargs)

        except Exception as e:
            # Handle exceptions (e.g., log the error)
            error_message = self.extract_error_message(e)
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:
            # Handle POST request to create a new user profile
            serializer = UserProfileSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except serializers.ValidationError as e:
            # Handle validation error
            error_message = self.extract_error_message(e)
            return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Handle other exceptions (e.g., log the error)
            error_message = self.extract_error_message(e)
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserProfileDetailView(BaseUserProfileView, generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        try:
            # Handle GET request to retrieve details of a specific user profile
            return self.retrieve(request, *args, **kwargs)

        except UserProfile.DoesNotExist:
            # Handle the case where the requested user profile does not exist
            return Response({'error': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Handle other exceptions (e.g., log the error)
            error_message = self.extract_error_message(e)
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, *args, **kwargs):
        try:
            # Handle PUT request to update details of a specific user profile
            instance = self.get_object()
            serializer = UserProfileSerializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        except UserProfile.DoesNotExist:
            # Handle the case where the requested user profile does not exist
            return Response({'error': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)

        except serializers.ValidationError as e:
            # Handle validation error
            error_message = self.extract_error_message(e)
            return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Handle other exceptions (e.g., log the error)
            error_message = self.extract_error_message(e)
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        try:
            # Handle DELETE request to delete a specific user profile
            return self.destroy(request, *args, **kwargs)

        except UserProfile.DoesNotExist:
            # Handle the case where the requested user profile does not exist
            return Response({'error': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Handle other exceptions (e.g., log the error)
            error_message = self.extract_error_message(e)
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
