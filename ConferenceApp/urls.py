from django.urls import path
#from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('liste/', views.all_conferences, name='list_conferences'),
    path('liste/', ConferenceListView.as_view(), name='list_conferences'),
    path('detail/<int:pk>/', ConferenceDetailView.as_view(), name='conference_detail'),
    path('form/', ConferenceCreate.as_view(), name='conference-create'),
    path('<int:pk>/update/', ConferenceUpdate.as_view(), name='conference-update'),
    path('<int:pk>/delete/', ConferenceDelete.as_view(), name='conference-delete'),
    path('submissions_list/', UserSubmissionListView.as_view(), name='list_submissions'),
    path('submission_detail/<str:pk>/', DetailSubmissionView.as_view(), name='submission_detail'),
    path('add_submission/', AddSubmissionView.as_view(), name='add_submission'),
    path('update_submission/<str:pk>/', UpdateSubmissionView.as_view(), name='update_submission'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)