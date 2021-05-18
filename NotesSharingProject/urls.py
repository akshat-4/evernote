from django.contrib import admin
from django.urls import path
from notes.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name="home"),
    path('admin/', admin.site.urls),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('userlogin/', userlogin, name="userlogin"),
    path('login_admin/', login_admin, name="login_admin"),
    path('signup/', signup, name="signup"),
    path('admin_home/', admin_home, name="admin_home"),
    path('Logout/', Logout, name="Logout"),
    path('profile/', profile, name="profile"),
    path('changepassword/', changepassword, name="changepassword"),
    path('editprofile/', editprofile, name="editprofile"),
    path('uploadnotes/', uploadnotes, name="uploadnotes"),
    path('view_mynotes/', view_mynotes, name="view_mynotes"),
    path('pending_notes/', pending_notes, name="pending_notes"),
    path('approved_notes/', approved_notes, name="approved_notes"),
    path('rejected_notes/', rejected_notes, name="rejected_notes"),
    path('all_notes/', all_notes, name="all_notes"),
    path('user_viewallnotes/', user_viewallnotes, name="user_viewallnotes"),
    path('user_personal/', user_personal, name="user_personal"),
    path('personal_myfiles/', personal_myfiles, name="personal_myfiles"),
    path('personal_upload/', personal_upload, name="personal_upload"),
    path('personal_notepad/', personal_notepad, name="personal_notepad"),
    path('personal_notepadfiles/', personal_notepadfiles, name="personal_notepadfiles"),
    path('personal_notepaddelete/<int:pid>', personal_notepaddelete, name="personal_notepaddelete"),
    path('personal_notepadview/<int:pid>', personal_notepadview, name="personal_notepadview"),
    path('personal_fav/', personal_fav, name="personal_fav"),
    path('personal_addfav/<int:pid>', personal_addfav, name="personal_addfav"),
    path('personal_removefav/<int:pid>', personal_removefav, name="personal_removefav"),
    path('viewusers/', viewusers, name="viewusers"),
    path('delete_mynotes/<int:pid>', delete_mynotes, name="delete_mynotes"),
    path('personal_deletenotes/<int:pid>', personal_deletenotes, name="personal_deletenotes"),
    path('delete_notes/<int:pid>', delete_notes, name="delete_notes"),
    path('delete_users/<int:pid>', delete_users, name="delete_users"),
    path('assign_status/<int:pid>', assign_status, name="assign_status"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
