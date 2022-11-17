from django.urls import path
from Proyecto_web_app import views

urlpatterns = [
    
    path('', views.Home, name="Home" ),
    path('servicios/', views.Servicos, name="Servicios" ),
    path('tienda/', views.Tienda, name="Tienda"),
    path('blog/', views.Blog, name="Blog"),
    path('contacto/', views.Contacto, name="Contacto"),
]
