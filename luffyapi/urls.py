
from django.contrib import admin
from django.urls import path,re_path,include
from django.views.static import serve
from django.conf import settings

# xadmin的依赖
import xadmin
xadmin.autodiscover()
# xversion模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('home/', include('home.urls')),
    path('user/', include('user.urls')),
    path('user/', include('dev测试新增冲突')),
    path('user/', include('dev测试新增冲突11')),
<<<<<<< HEAD

    path('user/', include('master冲突测试')),
=======
>>>>>>> dev

    # media文件夹路径打开了
    re_path('media/(?P<path>.*)', serve,{'document_root':settings.MEDIA_ROOT}),

]
