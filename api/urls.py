from django.urls import path
from . import views
# map URL's to functions

# temporary storage for keys
gasKeys = ['BP', 'Speedway', 'SPEEDWAY']
travelKeys = ['VALVOLINE', 'IPARK']
groceryKeys = ['KROGER', 'MEIJER']
recKeys = ['SUBWAY', 'BLAZE', 'CHICK FIL A', 'DAIRY QUEEN',
           'HACIENDA', 'JIMMY JOHNS', 'SHAKE SHACK']
schoolKeys = []
leisureKeys = ['AMAZON', 'AUSBLAKE', 'INDY CITY', 'GOOGLE']
rentKeys = []
miscKeys = ['APPLE.COM', 'MISCELLANEOUS DEBIT']
incomeKeys = ['IRVING', 'INDIANA UNV CONS CP']
ignoreKeys = ['TRANSFER', 'DISCOVER']

keys = [gasKeys, travelKeys, groceryKeys, recKeys, schoolKeys,
        leisureKeys, rentKeys, miscKeys, incomeKeys, ignoreKeys]

# url configuration, always end routes with '/'
urlpatterns = [
    path('', views.home, name='home'),  # root path URL
    path('hello/', views.say_hello),
    path('autocategory/', views.auto_category, {'keys': keys})
]
