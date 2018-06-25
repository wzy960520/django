from django.conf.urls import url

from verification import views

urlpatterns = [
    url(r'image_codes/(?P<code_id>.+)/$',views.imagecodeid.as_view())
]



