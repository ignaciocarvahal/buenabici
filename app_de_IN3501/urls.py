from django.urls import path
from . import views

urlpatterns = [
	# formato: dirección_pag, función_asociada , name=nombre
    path('',        views.inicio,    name='inicio'),
    path('contacto', views.contacto, name= 'contacto'),
    path('resultado', views.resultado, name= 'resultado'),
    path("productos", views.productos, name="productos"),
    path("quienessomos", views.quienessomos, name="quienessomos"),
    path("haztupedido", views.haztupedido, name="haztupedido"),
    path('confirmacionpedido', views.confirmacionpedido, name='confirmacionpedido'),
    path('alfajores', views.alfajores, name='alfajores'),
    path('donas', views.donas, name='donas'),
    path('rollitos', views.rollitos, name='rollitos'),
]


